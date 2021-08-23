"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from ghostpost_app import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('addpost/', views.add_post, name='addpost'),
    path('boasts/', views.boasts_view, name='boasts'),
    path('roasts/', views.roasts_view, name='roasts'),
    path('upvote/<int:post_id>/', views.upvote, name='upvote'),
    path('downvote/<int:post_id>/', views.downvote, name='downvote'),
    path('votescore/', views.vote_score_view, name='votescore'),
    # path('delete/<slug:secret>/', name='delete'),  # extra credit
    # path('private/<slug:secret>/', name='private'), # extra credit
    path('admin/', admin.site.urls),
]
