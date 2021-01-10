from django.urls import path, include

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:submission_id>', views.result, name='result'),
    path('summary/', views.summary, name='summary'),
    path('select/', views.select, name='select'),
    path('load/',views.loaddata, name='load'),
    path('year/<int:year_id>', views.year, name='year'),
    path('team/', views.team, name = 'team'),
    path('ipynb/', views.ipynb, name = 'ipynb'),
]