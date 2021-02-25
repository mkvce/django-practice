from django.shortcuts import render
from blogger.models import Article
# from django.http import HttpResponse

# Create your views here.
def index(request):
	article_list = Article.objects.all()
	context_dict = {'articles': article_list}
	return render(request, 'blogger/index.html', context_dict)
