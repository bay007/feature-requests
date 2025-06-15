import uuid

from django.db import models


class TimestampModel(models.Model):
    """Base model that includes created_at and updated_at fields."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Feature(TimestampModel):
    """Model for feature requests."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    additional_context = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def vote_count(self):
        """Returns the number of votes for this feature."""
        return self.votes.count()
    
    def has_user_voted(self, user_cookie):
        """Check if a user with the given cookie has voted for this feature."""
        return self.votes.filter(user_cookie=user_cookie).exists()


class Vote(TimestampModel):
    """Model for votes on feature requests."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feature = models.ForeignKey(Feature, related_name='votes', on_delete=models.CASCADE)
    user_cookie = models.CharField(max_length=64)  # Store a unique identifier for anonymous users
    
    class Meta:
        # Ensure a user can only vote once per feature
        unique_together = ['feature', 'user_cookie']
    
    def __str__(self):
        return f"Vote on {self.feature.title} by {self.user_cookie[:8]}..."


class Comment(TimestampModel):
    """Model for comments on feature requests."""
    feature = models.ForeignKey(Feature, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    user_cookie = models.CharField(max_length=64)  # Store a unique identifier for anonymous users
    
    def __str__(self):
        return f"Comment on {self.feature.title} by {self.user_cookie[:8]}..."
