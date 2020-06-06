from django.contrib import admin
from django.urls import path,re_path
from . import views
app_name='polls'
urlpatterns = [
path('',views.index,name='index'),
path('results/<int:question_id>/',views.results,name='results'),
path('detail/<int:question_id>/',views.detail),
path('vote/<int:question_id>/',views.vote),
]
