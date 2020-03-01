from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog_page(request):
	blogs = Blog.objects
	return  render(request,'blog.html',{'blogs':blogs})


def text_page(request,blog_id):
	#blogs = Blog.objects,,{'blogs':blogs}
	blog=get_object_or_404(Blog, pk=blog_id)
	return  render(request,'blog_text.html',{'blog':blog})