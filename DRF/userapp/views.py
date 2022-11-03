from django.shortcuts import render
from .serializers import UserRegistrationSerializer, UserLoginSerializer,ProductSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import BasicAuthentication, BaseAuthentication

##
from rest_framework import generics
from .models import Product

from django.contrib.auth import authenticate
from .renderers import UserRenderer


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request, format = None):
        serializer =  UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'registration success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    
     def post(self,request, format = None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email= email,password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'login success'},status=status.HTTP_200_OK)
            else:  
                return Response({'errors':{'field-errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)  


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class ProductDelete(generics.RetrieveDestroyAPIView):
       authentication_classes = [BasicAuthentication]
       permission_classes=[IsAdminUser]
       queryset = Product.objects.all()
       serializer_class = ProductSerializer