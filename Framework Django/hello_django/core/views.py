from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} com idade de {idade}.</h1>')


def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse(f'<h1>A soma entre {n1} + {n2} = {soma}.</h1>')


def subtracao(request, n1, n2):
    result = n1 - n2
    return HttpResponse(f'<h1>A subtração entre {n1} + {n2} = {result}.</h1>')


def divisao(request, n1, n2):
    result = n1 / n2
    return HttpResponse(f'<h1>A divisão entre {n1} + {n2} = {result}.</h1>')


def multiplicacao(request, n1, n2):
    result = n1 * n2
    return HttpResponse(f'<h1>A Multiplicação entre {n1} x {n2} = {result}.</h1>')

