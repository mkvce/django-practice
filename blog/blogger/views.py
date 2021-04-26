from django.shortcuts import render
from blogger.models import Article, Category
from blogger.forms import UserForm, AuthorForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import reverse


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    context_dict = {'articles': article_list}
    return render(request, 'blogger/index.html', context_dict)


def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    article_list = category.related_articles.all()
    context_dict = {'articles': article_list, 'category_name': category.nick_name}
    return render(request, 'blogger/category.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        author_form = AuthorForm(data=request.POST)
        if user_form.is_valid() and author_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            author = author_form.save(commit=False)
            author.user = user
            if 'picture' in request.FILES:
                author.picture = request.FILES['picture']
            author.save()
            registered = True
        else:
            print(user_form.errors, author_form.errors)
    else:
        user_form = UserForm()
        author_form = AuthorForm()
    context_dict = {
        'user_form': user_form,
        'author_form': author_form,
        'registered': registered,
    }
    return render(request, 'blogger/register.html', context_dict)


def user_login(request):
    user_not_found = False
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # logged_in = True
                return HttpResponseRedirect(reverse('blogger:index'))
            else:
                return HttpResponse("حساب کاربری شما غیر فعال شده است.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            user_not_found = True
    elif request.user.is_authenticated:
        return HttpResponse("شما قبلا وارد شده اید!")
    login_form = UserLoginForm()
    context_dict = {'login_form': login_form, 'user_not_found': user_not_found}
    return render(request, 'blogger/login.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogger:login'))
