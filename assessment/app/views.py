from django.shortcuts import render
from django.views import View
from datetime import datetime
from .models import User
class Index(View):
    def get(self,request):
        time = datetime.now()
        return render(request,'index.html',{'time':time})
    
class Submit(View):
    def post(self,request):
        time = datetime.now()
        name = request.POST.get('name')
        email = request.POST.get('email')
        user= User(name=name,email=email)
        user.save()
        return render(request,'user.html',{'name':name,'email':email,'time':time})
    
def data(request):
    records= User.objects.all()
    return render(request,'data.html',{'records':records})