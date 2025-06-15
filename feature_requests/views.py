import uuid

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm, FeatureForm
from .models import Comment, Feature, Vote


def get_user_cookie(request):
    """
    Get or create a unique identifier for the user using cookies.
    """
    user_cookie = request.COOKIES.get('user_id')
    if not user_cookie:
        user_cookie = str(uuid.uuid4())
    return user_cookie


def index(request):
    """
    View for the homepage that lists all feature requests.
    """
    features = Feature.objects.all().order_by('-created_at')
    form = FeatureForm()
    
    # Get the user's cookie to check for votes
    user_cookie = get_user_cookie(request)
    
    # Add a has_voted property to each feature
    for feature in features:
        feature.has_voted = feature.has_user_voted(user_cookie)
    
    context = {
        'features': features,
        'form': form,
    }
    
    response = render(request, 'feature_requests/index.html', context)
    
    # Set the cookie if it doesn't exist
    if not request.COOKIES.get('user_id'):
        response.set_cookie('user_id', user_cookie, max_age=365*24*60*60)  # Set cookie for 1 year
        
    return response


def create_feature(request):
    """
    View for creating a new feature request.
    """
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            feature = form.save()
            messages.success(request, '¡Tu solicitud de funcionalidad ha sido enviada con éxito!')
            return redirect('feature_detail', feature_id=feature.id)
    else:
        form = FeatureForm()
    
    return render(request, 'feature_requests/create_feature.html', {'form': form})


def feature_detail(request, feature_id):
    """
    View for showing the details of a feature request, including comments.
    """
    feature = get_object_or_404(Feature, id=feature_id)
    comments = feature.comments.all().order_by('-created_at')
    comment_form = CommentForm()
    
    # Check if the user has voted
    user_cookie = get_user_cookie(request)
    has_voted = feature.has_user_voted(user_cookie)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.feature = feature
            comment.user_cookie = user_cookie
            comment.save()
            messages.success(request, '¡Tu comentario ha sido añadido!')
            return redirect('feature_detail', feature_id=feature.id)
    
    context = {
        'feature': feature,
        'comments': comments,
        'comment_form': comment_form,
        'has_voted': has_voted,
    }
    
    response = render(request, 'feature_requests/feature_detail.html', context)
    
    # Set the cookie if it doesn't exist
    if not request.COOKIES.get('user_id'):
        response.set_cookie('user_id', user_cookie, max_age=365*24*60*60)  # Set cookie for 1 year
        
    return response


@require_POST
def vote_feature(request, feature_id):
    """
    View for voting on a feature.
    """
    feature = get_object_or_404(Feature, id=feature_id)
    user_cookie = get_user_cookie(request)
    
    # Check if the user has already voted
    has_voted = feature.has_user_voted(user_cookie)
    
    if has_voted:
        # Remove the vote
        Vote.objects.filter(feature=feature, user_cookie=user_cookie).delete()
        messages.success(request, '¡Tu voto ha sido eliminado!')
    else:
        # Add the vote
        try:
            Vote.objects.create(feature=feature, user_cookie=user_cookie)
            messages.success(request, '¡Gracias por tu voto! Siéntete libre de sugerir más funcionalidades.')
        except IntegrityError:
            # This shouldn't happen with our checks, but just in case
            messages.error(request, 'Ya has votado por esta funcionalidad.')
    
    # Redirect back to the referring page
    next_page = request.POST.get('next', 'index')
    return redirect(next_page)
