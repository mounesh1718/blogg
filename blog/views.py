from django.shortcuts import render
from . import models
from blog.models import Post,Aboutus
from django.http import Http404
from django.core.paginator import Paginator
from . forms import ContactForm
import logging

# Create your views here.

def index(request):
    blog_title = "Latest Posts "
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,'index.html',{'page':page,'blog_title':blog_title})

def detail(request,slug):
    try:
     post = Post.objects.get(slug = slug)
     related_posts = Post.objects.filter(category = post.category).exclude(pk = post.id)
    except Post.DoesNotExist:
        raise Http404('The Post does not exist')
    return render(request,'detail.html',{'post':post,'related_posts':related_posts})


def contact_view(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
         name = request.POST.get('name')
         email = request.POST.get('email')
         message = request.POST.get('message')
    
         logger = logging.getLogger('Testing')
         if form.is_valid():
            logger.warning(f"The contact details is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = 'This Form is sent successfully'
            return render(request,'contact.html',{'form':form,'success_message':success_message})
         else:
             logger.warning('The contact detail is invalid')
             return render(request,'contact.html',{'form':ContactForm,'name':name,'email':email,'message':message})
    
    return render(request,'contact.html')

def about_view(request):
    about_content = Aboutus.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default content is here"
    else:
        about_content = about_content.content
    return render(request,'about.html',{'about_content':about_content})