from django.shortcuts import render

# Create your views here.
def num(requests):
    return render(requests,'core/404.html')

def blog(requests):
    return render(requests,'core/blog-single.html')

def contact(requests):
    return render(requests,'core/contact.html')

def index(requests):
    return render(requests,'core/index.html')

def details(requests):
    return render(requests,'core/portfolio-details.html')
