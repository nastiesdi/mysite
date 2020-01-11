from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def catalog(request):
    return HttpResponse("tyt bydet catalog")

def about(request):
    return HttpResponse("<h2>tyt bydet about us</h2>")

def delivery(request):
    return HttpResponse("Dostavka")

def category(request, category_name = 'frize'):
    output = f"<h2>Category {category_name}</h2>"
    return HttpResponse(output)

def product(request, product_id = 0 ):
    name = request.GET.get("name", "fire")
    output = f'<h2>Product: {product_id}, name:{name}</h2>'
    return HttpResponse(output)
