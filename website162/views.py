from django.shortcuts import render
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')
# Create your views here.
