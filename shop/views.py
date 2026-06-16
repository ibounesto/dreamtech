from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . import forms, models

class ArticleUpdateView(UpdateView):
    model = models.Article
    template_name = 'shop/update_article.html'
    context_object_name = 'article'
    fields = ['name', 'description', 'image', 'price']

class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'shop/delete_article.html'
    context_object_name = 'article'
    success_url = '/'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'shop/article_detail.html'
    context_object_name = 'article'


class HomeView(ListView):
    model = models.Article
    template_name = 'shop/home.html'
    context_object_name = 'articles'


def user_articles(request):
    articles = models.Article.objects.filter(uploader=request.user)
    return render(request,'shop/user_articles.html',context={
        'articles': articles
    })

def add_to_cart(request, pk):
    article = get_object_or_404(models.Article, id=pk)
    panier = request.session.get('panier', {})
    article_id = str(article.id)
    if article_id in panier:
        panier[article_id] += 1

    else:
        panier[article_id] = 1

    request.session['panier'] = panier
    return redirect('home')

def cart(request):
    panier = request.session.get('panier', {})
    articles = models.Article.objects.filter(pk__in=panier)
    return render(request, 'shop/cart.html', context={
        'articles': articles
    })

def register_article(request):
    message = ''
    form= forms.RegisterArticleForm()

    if request.method == 'POST':
        form= forms.RegisterArticleForm(request.POST,request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.uploader = request.user
            article.save()
            return redirect('home')
        
        else:
            message = "L'article n'a pas ete ajoute"
        
    else:
        return render(request,'shop/register_article.html',context={
            'message': message,
            'form': form
        })

