from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('vote/<int:id>', views.vote, name='vote'),
    path('results/<int:id>', views.results, name='results'),

    
]
