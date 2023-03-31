from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, com idade:{idade}</h1>.')


def soma(request, n1, n2):
    result = int(n1) + int(n2)
    return HttpResponse(f'<h2>A soma de {n1} + {n2} = {result}.</h2>')


def subtracao(request, n1, n2):
    result = n1 - n2
    return HttpResponse(f'<h2>A subtração entre {n1} - {n2} = {result}.</h2>')


def multiplicacao(request, n1, n2):
    result = n1 * n2
    return HttpResponse(f'<h2>A subtração entre {n1} * {n2} = {result}.</h2>')


def divisao(request, n1, n2):
    result = n1 / n2
    return HttpResponse(f'<h2>A subtração entre {n1} / {n2} = {result}.</h2>')
