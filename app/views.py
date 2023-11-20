from django.shortcuts import render

# Create your views here.

def forloop(request):
    d = {'name' : 'RK'}
    return render (request,'forloop.html',context=d)