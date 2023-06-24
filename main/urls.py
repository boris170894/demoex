from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.graduateInfoView.as_view(), name='graduate'),
    path("", views.index, name='index'),
    #path("grad", views.grad_list, name = 'list'),
    #path("<slug:slug>/", views.show_info, name = "graduate"),
] 