from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('', include('django.contrib.auth.urls')),
    path('proje/',views.dosya_list,name='dosya_list')
    

]