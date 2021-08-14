from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            with open('/usr/share/ipTmp','a+') as f:
                 f.write(form.cleaned_data['title'])
                 f.write('\n')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})
def homePageView(request):
    return HttpResponse('Hello, World!')
