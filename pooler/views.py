from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
# from .models import Profile, Tag, Post, Follow, Comment, Like
# from .forms import NewsPostForm, NewCommentForm

# Create your views here.
def index(request):
    '''
    View function for the landing page of the application
    '''
    title = 'CarPoolers'
    message = 'Landing Page'
    return render(request,'index.html',{"title":title,"message":message})

def driver(request):
    '''
    View function to display a registration form when the user selects the driver option
    '''
    pass
