from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request, 'mypage.html')