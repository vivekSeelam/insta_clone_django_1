from django.http import HttpResponse


# Create your views here.
def index(request):
    message = f'{request.GET["cool_boy"]}'
    if message == 'vivek':
        message = "vvievk is the best"
    return HttpResponse(f"THis is wierd {message}")
















