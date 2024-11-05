from django.http import HttpResponse

# Create your views here.
def landingpage_view(request):
    return HttpResponse('This is the landing page')