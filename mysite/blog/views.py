from django.views import generic
from .models import Post


# it rends a list with the objects of the specified model at the provided template
# only posts with status published will be shown and tey are ordered by creation date with the last post at the top
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# it provides a detailed view for a given object of the model at the provided template
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
