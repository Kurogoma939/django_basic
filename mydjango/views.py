
from django.http import HttpResponse


def helloworld(request):
    returnobject = HttpResponse('Hello World!!')
    return returnobject