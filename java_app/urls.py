from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shops/add', views.createShop),
    path('shops/<int:id>', views.oneShop),
    path('register', views.register), 
    path('login', views.login), 
    path('logout', views.logout),
    path('reviews/create', views.createReview),
    path('edit/<int:review_id>', views.editReview),
    path('update/<int:review_id>', views.updateReview),
    path('user/<int:user_id>/recipe', views.user_display),
    
]