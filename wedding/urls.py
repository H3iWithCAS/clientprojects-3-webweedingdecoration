from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('blog/', views.blog, name='blog'),
    path('layanan/', views.layanan, name='layanan'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('list_bookings/', views.list_bookings, name='list_bookings'),
    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/update/<int:pk>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
]