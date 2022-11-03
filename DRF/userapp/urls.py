from django.urls import path
from .views import UserRegistrationView, UserLoginView,ProductList,ProductCreate,ProductDetail,ProductDelete

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name = "registration"),
    path('login/',UserLoginView.as_view(),name = "login"),
    path('product/',ProductList.as_view(),name = "product_list"),
    path('product/<str:pk>/',ProductDetail.as_view(),name = "product_detail"),
    path('create-product/',ProductCreate.as_view(),name = "product_create"),
    path('delete-product/<str:pk>/',ProductDelete.as_view(),name = "product_delete"),

    path('token/',TokenObtainPairView.as_view(),name = "token"),
    path('token/refresh/',TokenRefreshView.as_view(),name = "token_refresh_view"),

     

]
