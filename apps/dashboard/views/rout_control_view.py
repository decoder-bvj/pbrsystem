from django.http import HttpResponse

def router(request):
    return HttpResponse("response form the router")