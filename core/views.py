from django.shortcuts import render

def index(requests):
    return render(requests, 'core/index.html')

def contact(requests):
    return render(requests, 'core/contact.html')
