from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/new/', views.create_feature, name='create_feature'),
    path('features/<uuid:feature_id>/', views.feature_detail, name='feature_detail'),
    path('features/<uuid:feature_id>/vote/', views.vote_feature, name='vote_feature'),
]
