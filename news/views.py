from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Article, Language, Category, Api


def index(request, language):
    lang = get_object_or_404(Language, code=language)
    languages = Language.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.filter(show_on_homepage=True, language=lang).order_by('-date')
    context = {"articles": articles,
               "categories": categories,
               "current": 1,
               "language": lang,
               "languages": languages,
               "title": "Neo News",
               "description1": "Neo News is a free website that offers news articles in different categories. \
                                we speak to the people and we only premote freedom of speech and real news.",
               }
    return render(request, 'index.html', context)


def category(request, language, category):
    lang = get_object_or_404(Language, code=language)
    ctg = get_object_or_404(Category, title=category)
    categories = Category.objects.all()
    articles = Article.objects.filter(show_on_homepage=True, language=lang, category=ctg).order_by('-date')
    context = {"articles": articles,
               "categories": categories,
               "language": lang,
               "category": ctg,
               "title": "Neo News - " + str(ctg),
               "current": 2,
               }
    return render(request, 'index.html', context)


def article(request, slug, language, category):
    lang = get_object_or_404(Language, code=language)
    ctg = get_object_or_404(Category, title=category)
    categories = Category.objects.all()
    article = get_object_or_404(Article, category=ctg, language=lang, slug=slug)
    article.add_ads()
    context = {"article": article,
                "categories": categories,
               "title": "Neo News - " + str(article.title),
               "description": str(article.snippet()),
               }
    return render(request, "article.html", context)


def sitemap(request):
    return render(request, "sitemap.xml", {})

@csrf_exempt
def pull(request):
    if request.method == "POST":
        try:
            key = get_object_or_404(Api, key=request.POST["key"])
        except Exception as e:
            print(e)
            return HttpResponse("403")

        try:
            category = request.POST["category"]
            language = request.POST["language"]
            count = request.POST["count"]
            context = {}

            if category != "*":
                context["category"] = get_object_or_404(Category, title=category)
            if language != "*":
                context["language"] = get_object_or_404(Language, code=language)

            articles = Article.objects.filter(**context).order_by('-date')
            if count != "*":
                articles = articles[:int(count)]


            links = []
            for article in articles:
                temp = {}
                temp["title"] = article.title
                temp["link"] = article.link()
                links.append(temp)

            return JsonResponse(links, safe=False)
        except Exception as e:
            return HttpResponse("500")
            
    return HttpResponse("404")

@csrf_exempt
def add(request):
    if request.method == "POST":
        try:
            key = get_object_or_404(Api, key=request.POST["key"])
        except Exception as e:
            print(e)
            return HttpResponse("403")

        try:
            article = Article()
            article.title = request.POST["title"]
            article.headimage = request.POST["headimage"]
            article.author = request.POST["author"]
            article.content = request.POST["content"]
            article.show_on_homepage = request.POST["show"] == "true"
            article.category = get_object_or_404(Category, title=request.POST["category"])
            article.language = get_object_or_404(Language, code=request.POST["language"])
            article.save()
            return HttpResponse("200")
        except:
            return HttpResponse("500")
            
    return HttpResponse("404")

def handler404(request, template_name="404.html"):
    categories = Category.objects.all()
    context = {
                "categories": categories,
               "title": "Neo News - Page not found",
               "description": "Page not found",
               }
    response = render(template_name, context=context)
    response.status_code = 404
    return response
