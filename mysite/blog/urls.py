from django.urls import path,include
from . import views

urlpatterns=[
    path("test1/", views.test1),
    path("test2/<id>/", views.test2),
    path("test3/<year>/<mon>/<day>/", views.test3),
]