from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def donate(request):
    return render(request, 'donate.html')