from django.db import models
from django.contrib.auth.models import User

# it is used to keep draft and published posts separated when they are rendered out with templates
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # this class inside the model contains metadata. In particular I tell Django to sort results in
    # created_on field in descending order using the negative prefix
    class Meta:
        ordering = ['-created_on']

    # this added method overrides another of Django and has the purpose of representing the instance of the model
    # with the title
    def __str__(self):
        return self.title

