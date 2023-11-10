from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render (request,'msd.html')

def msd(request):
    return HttpResponse('<marquee><h1> cool captian<h1></marquee>')