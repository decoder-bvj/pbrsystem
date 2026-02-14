from django.shortcuts import render


def landing(request):
    return render(request,'html/pages/landing.html')