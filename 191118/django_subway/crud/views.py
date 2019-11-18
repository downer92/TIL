from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')      
        #db저장
        article=Article()
        article.title = title
        article.content = content
        article.save()
        return render(request, "crud/created.html")
    else:
        return render(request, "crud/new.html")

# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')      
#     #db저장
#     article=Article()
#     article.title = title
#     article.content = content
#     article.save()
#     return render(request, "crud/created.html")

def index(request) : 
    # 1번째 파이썬에서 정렬하는 방법
    # articles = Article.objects.all()[::-1] # 역순으로 저장
    
    # 2번째 불러올 때 정렬시키는 법
    articles = Article.objects.order_by('-id')
    
    context = {
        "articles" : articles
    }
    return render(request, 'crud/index.html', context)

def detail(request, pk):
    # (pk=pk)가 (id__exact=pk)와 같음
    article = Article.objects.get(pk=pk)
    
    context = {
        "article" : article
    }
    return render(request, 'crud/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=="POST":
        article = Article.objects.get(pk=pk)
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(content)
        article.title = title
        article.content = content
        article.save()
        return redirect('crud:detail', pk) # redirect import
    
    else:
        context = {
            "article": article
        }
        return render(request, 'crud/update.html', context)

# def revise(request, pk):
#     article = Article.objects.get(pk=pk)
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     print(content)
#     article.title = title
#     article.content = content
#     article.save()
#     return redirect(f'crud:detail') # redirect import

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('crud:index')
    else:
        return redirect('crud:detail', article.id)
