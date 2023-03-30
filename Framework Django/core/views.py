from django.shortcuts import render, HttpResponse

# Create your views here.


def ninoseg(request, nome, idade=0):
    return HttpResponse(f'<h1>Hello {nome}, com idade:{idade}</h1>')
