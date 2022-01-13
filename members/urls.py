from django.urls import path
from .views import join
from .views import member_views

urlpatterns = [
    
    path('list/', member_views, name='members'),
    path('join/', join, name='join'),

]