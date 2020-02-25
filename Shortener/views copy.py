from .models import  Shorturl
from .shortener import Shortener
from .forms import URLForm ,UrlStatForm
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

SHORTCODE_MIN =  getattr(settings,"SHORTCODE_MIN",6)


def home(request,token):
    long_url  = Shorturl.objects.filter(shortcode = token)[0]
    return  redirect(long_url.url)

def index(request):
    form = URLForm(request.POST)
    short_code = ''
    if request.method == 'POST':
        if form.is_valid():
            newUrl = form.save(commit=False)
            short_code = Shortener.code_generator()
            newUrl.shortcode = short_code
            newUrl.save()

            context = {'donor': donor, 'result': result}
            return render(request, 'ibd/user_history.html', context)


        else:
            form = URLForm()
            print("Invalid URL")
    return render(request,"shortener/index.html",{'form':form,'short_code':short_code})


def stats(request):
    form = UrlStatForm()
    data  = Shorturl.objects.all()
    args = {'form':form, 'data':data}
    return render(request,"shortener/stats.html",args)
