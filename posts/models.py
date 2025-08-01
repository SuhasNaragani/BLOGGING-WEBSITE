# posts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .tasks import post_published_notification

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True) # ADDED: Image field for posts

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if not is_new:
            original = Post.objects.get(pk=self.pk)

        original_slug = slugify(self.title)
        new_slug = original_slug

        counter = 1
        while Post.objects.filter(slug=new_slug).exclude(pk=self.pk).exists():
            new_slug = f'{original_slug}-{counter}'
            counter += 1
        self.slug = new_slug

        super().save(*args, **kwargs)

        if (is_new and self.status == 'published') or \
           (not is_new and self.status == 'published' and original.status == 'draft'):
            post_published_notification.delay(self.id, self.title)

    def __str__(self):
        return self.title

# ADD THIS MODEL BACK INTO THE FILE
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'