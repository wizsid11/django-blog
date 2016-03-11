from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
		
	#if request.method == "POST":
	#	print request.POST.get("content")
	#	print request.POST.get("title")
	context = {
		"form": form,
	}
	return render(request, "post_form.html",context)

def post_detail(request,slug=None):
	#instance=Post.object.get(id=1)
	instance = get_object_or_404(Post, slug=slug)
	context={
		"title":instance.title,
		"instance": instance
	}
	return render(request, "post_detail.html",context)

def post_list(request):
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var='page'
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context={
			"object_list": queryset,
			"title": "Welcome Folks!!",
			"page_request_var": page_request_var
		}
	#if request.user.is_authenticated():
	#	context={
	#		"title":"My User List"
	#	}
	#else:
	#	context={
	#		"title":"List"
	#	}
	return render(request, "post_list.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"title":instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html",context)	

def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")


   
   	