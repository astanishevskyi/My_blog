from django.urls import reverse
from .models import Article
from .forms import NewArticleForm
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView


class LoginFormView(FormView):
    pass


class Index(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'detail.html'


class CreateArticle(CreateView):
    model = Article
    template_name = 'add_article.html'
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'update_article.html'
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    template_name = 'delete_article.html'

    def get_success_url(self):
        return reverse('index')

