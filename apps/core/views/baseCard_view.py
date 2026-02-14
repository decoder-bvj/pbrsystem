from django.shortcuts import render


def basecard(request):
    return render(request, 'html/components/baseCard.html')