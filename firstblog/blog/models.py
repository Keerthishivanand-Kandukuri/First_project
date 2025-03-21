from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title with a max length of 200 characters
    content = models.TextField()  # Content field for detailed text
    created_at = models.DateTimeField(auto_now_add=True)  # Auto add current date/time on creation
    #updated_at = models.DateTimeField(auto_now=True)  # Auto update on every save

    def __str__(self):
        return self.title