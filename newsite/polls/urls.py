from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # e x: /polls/5/
    path('<int:id>', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:id>/vote/', views.vote, name='vote'),
]