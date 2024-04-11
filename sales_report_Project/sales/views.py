from django.shortcuts import render
from django.views.generic import ListView
# Create your views here
def home_view(request):
    return render(request,'sales/home.html',{})