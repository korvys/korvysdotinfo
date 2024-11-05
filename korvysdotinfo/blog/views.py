from django.http import HttpResponse

# Create your views here.
def homepage_view(request):
    return HttpResponse('This is the blog')