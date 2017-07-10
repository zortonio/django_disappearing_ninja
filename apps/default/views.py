from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "default/index.html")

def ninjas(request):
    return render(request, "default/ninjas.html")

def ninja(request, color):
    print color
    context = {
        'color': color
    }
    return render(request, "default/ninja.html", context)
