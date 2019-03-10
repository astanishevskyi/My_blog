from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from .forms import NewArticleForm
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView, View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


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


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
