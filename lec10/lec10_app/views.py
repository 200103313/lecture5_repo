from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from lec10_app.models import Posts

# Create your views here.
def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context={'post': post}
    return render(request, 'lec10_app/post.html', context=context)