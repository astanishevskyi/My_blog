"""My_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from blog.views import Index, ArticleDetail, CreateArticle, ArticleUpdateView, ArticleDeleteView, LoginFormView, \
    LogoutView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('add_article/', CreateArticle.as_view(), name='add_article'),
    path('update_article/<int:pk>', ArticleUpdateView.as_view(), name='update_article'),
    path('delete_article/<int:pk>', ArticleDeleteView.as_view(), name='delete_article'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),

    url(r'^accounts/', include('allauth.urls')),
]
