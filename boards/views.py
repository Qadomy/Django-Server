from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, \n"
                        "I'm Ali Qadomy, I'm Mobile Application Developer")
