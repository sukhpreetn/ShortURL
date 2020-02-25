from django.http import HttpResponse

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
            queryset = Shorturl.objects.filter(url=newUrl)
            if queryset.exists():
                obj = Shorturl.objects.get(url=newUrl)
                return render(request,"shortener/already-exists.html",{'url':newUrl,'short_code':obj.shortcode})
            else:
                #return HttpResponse("not found")

                short_code = Shortener.code_generator()
                newUrl.shortcode = short_code
                newUrl.save()
                return render(request,"shortener/success.html",{'url':newUrl,'short_code':short_code})
            #return HttpResponse(newUrl)

        else:
            form = URLForm()
            print("Invalid URL")
    return render(request,"shortener/index.html",{'form':form,'short_code':short_code})


def stats(request):
    form = UrlStatForm()
    data  = Shorturl.objects.all()
    args = {'form':form, 'data':data}
    return render(request,"shortener/stats.html",args)
