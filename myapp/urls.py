from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.projects, name='project'),
    path('contact/', views.contact, name='contact'),
    path('skills/',views.skills,name='skills'),
    path("project/<int:id>/", views.project_detail, name="project_detail"),
    path("certificate/",views.certificates,name="certificate"),
]