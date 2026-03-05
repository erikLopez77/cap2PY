from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class MyView(View):
    def get(self,request):
        return render(request,"mytemplate.html")    
    
    def post(self,request):
        name=request.POST("name")
        return HttpResponse(name)