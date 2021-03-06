from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import SelfPostForm
from .models import Post






# Create your views here.
"""
Shows a user's own page
"""
class IndexView(View):
    def get(self, *args, **kwargs):
        context = {}
        context['page_owner'] = self.request.user
        context['posts'] = Post.objects.filter(owner=self.request.user)
        context['create_post_form'] = SelfPostForm()
        return render(self.request, "home/index.html", context)


class CreateNewPostView(View):
    def post(self, *args, **kwargs):
        form = SelfPostForm(self.request.POST)

        if form.is_valid():
            post = Post()
            post.owner = self.request.user
            post.post_body = form.cleaned_data['post_body']

            post.save()

            messages.success(self.request, "Succesfully posted your post.")
            return redirect("home:index")
        else:
            messages.error(self.request, form.errors)
            return redirect("home:index")
