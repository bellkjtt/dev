from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test1(request):
    return HttpResponse("blog/test1 응답!")

def test2(request,id):
    return HttpResponse(id)

def test3(request,year,mon,day):
    return HttpResponse(f'{year}년 {mon}월 {day} 일')