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
    path('dashboard', views.dashboard),
    path('addreview', views.createReview),
    path('editprofile', views.profile),
    path('registrationpage', views.registerPage),
    
    path('add', views.add),
    
]