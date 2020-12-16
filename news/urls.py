from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('api/add/', views.add, name='add'),
    path('api/pull/', views.pull, name='pull'),
    path('<str:language>/<str:category>/<slug:slug>/', views.article, name='article'),
    path('<str:language>/<str:category>/', views.category, name='category'),
    path('<str:language>/', views.index, name='index'),
    path('', RedirectView.as_view(url='/en/')),
]
