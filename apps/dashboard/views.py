from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'html/pages/dashboard.html')
    #return HttpResponse("Response from the dashboard")
