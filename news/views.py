from django.shortcuts import render
from .models import News 
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

class HomeView(ListView):
	model 			=News
	temlate_name 	= 'news_list.html'
	ordering		=['-date']

class ArticleDetailView(DetailView):
	model 			=News
	temlate_name 	= 'news_detail.html'

class AddNewsView(CreateView):
	model 			= News
	temlate_name 	= 'news_form.html'
	fields 			= '__all__'

class DeleteNewsView(DeleteView):
	model 			= News
	temlate_name 	= 'news_confirm_delete.html'
	success_url		= reverse_lazy('home')

def news_views(request):
	obj = News.objects.all()
	context ={
		'newsobject':obj,
	}
	return render(request, "news/detail.html", context)



