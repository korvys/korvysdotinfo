from django.http import HttpResponse

# Create your views here.
def gallery_view(request):
    return HttpResponse('This is the gallery')