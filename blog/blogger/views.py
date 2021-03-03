from django.shortcuts import render
from blogger.models import Article, Category
# from django.http import HttpResponse

# Create your views here.
def index(request):
	article_list = Article.objects.all()
	context_dict = {'articles': article_list}
	return render(request, 'blogger/index.html', context_dict)

def category(request, category_name_slug):
	category = Category.objects.get(slug=category_name_slug)
	article_list = category.related_articles.all()
	return render(request, 'blogger/category.html', context={'articles': article_list, 'category_name': category.name})
