from django import forms
from .models import  Shorturl



class URLForm(forms.ModelForm):
    class Meta:
        model = Shorturl
        fields = ['url']


class UrlStatForm(forms.ModelForm):
    class Meta:
        model = Shorturl
        labels = {
            'url'         : 'Long Url',
            'shortcode'   : 'Shortcode',
            'timestamp'   : 'Created on',
            'active   '   : 'active',
        }
        fields = "__all__"
