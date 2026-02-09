from django.shortcuts import render #後から使うよ
from django.http import HttpResponse #djangoから簡易的なテキストを表示する関数を引っ張ってくる

# Create your views here.
def index(request): #indexが呼び出されたら、、、
    return HttpResponse('<h1>Hey, Welcome</h1>')#HttpResponse('<h1>Hey, Welcome</h1>')をreturnする
