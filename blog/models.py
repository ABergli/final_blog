from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the 'updated_on' field before saving
        self.updated_on = timezone.now()
        if self.author and not self.author_name:
            self.author_name = self.author.username
        super(Post, self).save(*args, **kwargs)

    def display_created_on(self):
        return self.created_on.strftime('%b %d, %Y %I:%M %p')

    def display_updated_on(self):
        return self.updated_on.strftime('%b %d, %Y %I:%M %p')


    def __str__(self):
        # Display either the authenticated author's username or the non-authenticated author's name
        author = self.author.username if self.author else self.author_name
        return f"{self.title} by {author}"

    def get_absolute_url(self):
        return reverse('post_list')