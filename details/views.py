from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Type
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#    return render(request, "home.html", {})

def TypeView(request, typeDisp):
    type_posts = Post.objects.filter(type=typeDisp)
    return render(request, 'type_display.html', {'typeDisp':typeDisp, 'type_posts':type_posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
   
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__' 

class AddTypeView(CreateView):
    model = Type
    template_name = 'add_type.html'
    fields = '__all__' 
    
class UpdatePostView(UpdateView):
    model = Post
    #form_class = EditForm
    template_name = 'update_post.html'
    fields = '__all__' 

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'  
    success_url = reverse_lazy('home') 