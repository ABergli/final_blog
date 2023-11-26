# blog/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
# from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-id')  # Ordering should be applied here
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create new post
class CreatePostView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'author', 'author_name', 'content', 'updated_on', 'image', 'video']

    def form_valid(self, form):
        # Set the author if it's not set (assuming the author is the current user)
        if not form.instance.author:
            form.instance.author = self.request.user

        # Handle image and video separately
        image = self.request.FILES.get('image')
        video = self.request.FILES.get('video')

        # Check if either image or video is provided
        if image and not video:
            form.instance.image = image
        elif video and not image:
            form.instance.video = video
        elif image and video:
            form.instance.image = image

        return super().form_valid(form)


class DetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    # fields = '__all__'
    fields =['title','author_name','content', 'updated_on', 'image', 'video']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('post_list')



