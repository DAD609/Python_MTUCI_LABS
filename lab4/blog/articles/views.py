from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Article


  
def archive(request, pk=None):
    if pk!=None:
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return HttpResponse('Такой записи не существует!')
        return render(request, 'article.html', {"post": article })

    return render(request, 'articles.html', {"posts": Article.objects.all()})
  


