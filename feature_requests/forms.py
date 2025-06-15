from django import forms

from .models import Comment, Feature


class FeatureForm(forms.ModelForm):
    """Form for creating new feature requests."""
    class Meta:
        model = Feature
        fields = ['title', 'description', 'additional_context']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4}),
            'additional_context': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4, 'placeholder': 'Additional context (optional)'}),
        }
        labels = {
            'title': 'Feature Title',
            'description': 'Feature Description',
            'additional_context': 'Additional Context (Optional)',
        }


class CommentForm(forms.ModelForm):
    """Form for adding comments to feature requests."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3, 'placeholder': 'Add your thoughts on this feature...'}),
        }
        labels = {
            'content': 'Your Comment',
        }
