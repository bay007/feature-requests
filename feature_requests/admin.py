from django.contrib import admin

from .models import Comment, Feature, Vote


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'vote_count')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('feature', 'user_cookie', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('feature__title', 'user_cookie')
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('feature', 'user_cookie', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('feature__title', 'content', 'user_cookie')
    date_hierarchy = 'created_at'
