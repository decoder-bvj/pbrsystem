from django.shortcuts import render

def base(request): 
    # Ensure this path is correct in your templates folder
    return render(request, 'html/pages/base.html')