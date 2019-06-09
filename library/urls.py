from django.urls import path

from library import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('set_password/', views.set_password, name='set_password'),
    path('book/detail$', views.book_detail, name='book_detail'),
    path('book/action$', views.reader_operation, name='reader_operation'),
    path('search/', views.book_search, name='book_search'),
    path('profile/', views.profile, name='profile'),
    path('statistics/', views.statistics, name='statistics'),
    path('about/', views.about, name='about'),

]
