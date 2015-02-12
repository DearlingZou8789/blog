from django.shortcuts import render,render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import loader,Context,Template
class Person(object):
    def __init__(self,name,age,sex):
            self.name=name
            self.age=age
            self.sex=sex

    def say(self):
            return "I'm"+self.__name


def index(req,id):
    #t=loader.get_template('index.html')
    #c=Context({})
    user={'name':'zmj','age':26,'sex':'male'}
    
    #user=Person('wjl',28,'female')
    
    book_list=['python','java','php','c','web']
    return render_to_response('index.html',{'title':'my page','book_list':book_list,'user':user,'id':id})
    #return HttpResponse(t.render(c))
    #return HttpResponse('<h1>welcome to Django!</h1>')

def index1(req,id):
    t=Template('<h1>hello Django {{uname}}</h1><hr>You are the {{id}}')
    c=Context({'uname':'zmj','id':id})
    return HttpResponse(t.render(c))

def index2(req,id):
    t=loader.get_template('index.html')
    c=Context({})
    return HttpResponse(t.render(c))
