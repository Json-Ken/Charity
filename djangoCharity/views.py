from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse
from .models import donar

cl = MpesaClient()
stk_pus_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)

def index(request):
    return render(request,'index.html')
def contact(request):
    data = donar.objects.all()
    context = {"data": data}
    return render(request,'contact.html',context)
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def donate(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_Reference = 'KENJCARES'
        transaction_desc = 'STK Push Description'
        callback_url = stk_pus_callback_url
        r = cl.stk_push(phone_number, amount, account_Reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'donate.html')
def faq(request):
    return render(request, 'faq.html')
def water(request):
    return render(request, 'water.html')
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        location = request.POST.get('location')
        # print(name,email,message,location)
        query = donar(name=name, email=email, message=message, location=location)
        query.save()
        return redirect("/")




