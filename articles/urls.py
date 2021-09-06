from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [

    path('about/', views.about, name='about'),
    path('', views.home, name='index'),
    path('articles/', views.articleslist, name='articleslist'),

]
urlpatterns += staticfiles_urlpatterns()