from multiprocessing import context
from re import L
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import is_valid_path

import lecture5_app
from .models import *
from .forms import *
from django.core.mail import send_mail

def home(request):
    name = get_object_or_404(Posts, pk=1)
    context = {'name': name}
    return render(request, 'lecture5_app/home.html', context=context)

def nature(request):
    return render(request, 'lecture5_app/nature.html', {'title': 'Природа Казахстана'})

def food(request):
    return render(request, 'lecture5_app/food.html', {'title': 'Национальная еда'})

def art(request):
    return render(request, 'lecture5_app/art.html', {'title': 'Национальное исскуство'})

def traditions(request):
    return render(request, 'lecture5_app/traditions.html', {'title': 'Традиции'})

def sport(request):
    all_sport=Sport.objects.all()
    return render(request, 'lecture5_app/sport.html', {'lecture5_app': all_sport})

def index(request):
    all_lecture5_app=Lecture5_app.objects.all()
    return render(request, 'lecture5_app/index.html', {'lecture5_app': all_lecture5_app})

def upload(request):
    upload=PostCreate()
    if request.method == 'POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Error, reload on <a href = "{{url : 'index'}}"> reload</a>""")
    else:
        return render(request, 'lecture5_app/upload_form.html', {'upload_form':upload})

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Lecture5_app.objects.get(id = post_id)
    except Lecture5_app.DoesNotExist:
        return redirect('index')
    post_form = PostCreate(request.POST or None, instance=post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('index')
    return render(request, 'lecture5_app/upload_form.html', {'upload_form':post_form})

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Lecture5_app.objects.get(id = post_id)
    except Lecture5_app.DoesNotExist:
        return redirect('index')
    post_sel.delete()
    return redirect('index')


def upload_sp(request):
    upload=PostCreateSp()
    if request.method == 'POST':
        upload = PostCreateSp(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('sport')
        else:
            return HttpResponse("""Error, reload on <a href = "{{url : 'sport'}}"> reload</a>""")
    else:
        return render(request, 'lecture5_app/upload_form_sp.html', {'upload_form':upload})

def update_post_sp(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Sport.objects.get(id = post_id)
    except Sport.DoesNotExist:
        return redirect('sport')
    post_form = PostCreateSp(request.POST or None, instance=post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('sport')
    return render(request, 'lecture5_app/upload_form_sp.html', {'upload_form':post_form})

def delete_post_sp(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Sport.objects.get(id = post_id)
    except Sport.DoesNotExist:
        return redirect('sport')
    post_sel.delete()
    return redirect('sport')
    
def polls(request):
    return render(request, 'lecture5_app/polls.html')

def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'lecture5_app/post.html', context=context)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Posts.objects.create(**form.cleaned_data)
                return redirect('welcome')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = AddPostForm()
    return render(request, 'lecture5_app/addpage.html', {'title':'Регистрация', 'form': form})

def welcome(request):
    name = Posts.objects.latest()
    context = {'name': name}
    return render(request, 'lecture5_app/welcome.html', context=context)

def send_message(request):
    send_mail("WEb programming:back end", "My content",
              "200103313@stu.sdu.edu.kz",
              ["200103313@stu.sdu.edu.kz", "malikahamity27@gmail.com"],
              fail_silently=False, html_message="<b>Bold text</b><i> Italic text </i>")
    return render(request, 'lecture5_app/successfull.html')

#class AuthorListView(generic.ListView):
    #model = Author
    #paginate_by = 10
