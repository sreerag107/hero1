from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def testfun(request):
    return render(request, 'site.html')
