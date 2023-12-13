from.import views
from django.urls import path

urlpatterns = [
    #path('', views.demo, name='demo'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('values/',views.values,name='values'),

   # path('',views.demo,name='demo'),
    path('add/',views.addition,name='addition'),

    path('',views.demo,name="demo")

]