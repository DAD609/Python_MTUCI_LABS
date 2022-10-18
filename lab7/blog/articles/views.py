from re import U
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
  

def archive(request, pk=None):
    if pk!=None:
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return HttpResponse('Такой записи не существует!')
        return render(request, 'article.html', {"post": article })

    return render(request, 'articles.html', {"posts": Article.objects.all()})
  

def create_post(request):
   if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                article_id = Article.objects.create(text=form["text"], title=form["title"], author=request.user).id
                return redirect('article', pk=article_id)
           
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html')
        else:
            return render(request, 'create_post.html', {})

   else:
         raise Http404

def  create_user(request):
    if request.method == "POST":
        
        form= {
                    'username': request.POST["username"], 'email': request.POST["email"], 'password': request.POST["password"]
                }
        try:
            User.objects.get(username=form['username'])
        except User.DoesNotExist:
            if form["username"] and form["email"] and form["password"]:
                User.objects.create_user(form["username"], form["email"], form["password"])
            else: 
                return render(request, 'create_user.html', {'error': 'Заполни все поля'})
            return redirect('login')
        
        return HttpResponse('Имя пользователя уже существует')
    else:
        return render(request, 'create_user.html')
        
def login_user(request):
    if request.method == 'POST':
        form = {
            'username': request.POST['username'], 'password': request.POST['password']
        }
        if form["username"] and form["password"]:
            user = authenticate(username = form['username'], password=form['password'])
            if user is None:
                return render(request, 'login.html', {'error': 'Нет такого пользователя'})
            login(request, user)
            return redirect('articles')
        else:
            return render(request, 'login.html', {'error': 'Нет такого пользователя'})
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')