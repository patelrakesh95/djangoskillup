from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='sampleapp/index'),
    path('index/',views.renderIndex,name='sampleapp/renderIndex')
]
