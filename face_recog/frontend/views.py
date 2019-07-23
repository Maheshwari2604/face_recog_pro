from django.shortcuts import render ,redirect
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .forms import UserForm
from .models import Users
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.
# class userview(ListModelMixin , GenericAPIView):
#     print('hey')
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()
#     print(queryset)
#     #return Response({"User": User})

#     def perform_create(self, serializer):
#         Users = get_object_or_404(Users, id=self.request.data.get('Users_id'))
#         return serializer.save(Users=Users)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



class userviewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


def register(request): 
  
    if request.method == 'POST': 
        form = UserForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return render(request,'register.html',{'msg':'Uploaded Succesfully','status':'success'}) 
    else: 
        form = UserForm() 
    return render(request, 'register.html', {'form' : form , 'msg':''})



