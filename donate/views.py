from django.shortcuts import render, redirect
from django.urls import reverse

import stripe
stripe.api_key = 'Your Secret Stripe API Key'

def donatePageView(request):
    
    context = {}
    return render(request, 'donate.html', context)

def charge(request):

    if request.method == 'POST':
        print('Information:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['name'],
            source = request.POST['stripeToken'],
            )

        charge = stripe.Charge.create(
            customer = customer,
            
            # stripe goes by cents so if input amount if 5, stripe reads as 5 cents. Minimum amount of $0.50
            amount = amount * 100,
            currency = "cad",
            description = "Donation"
            )

        return redirect(reverse('success'))

def successPageView(request):

    context = {}
    return render(request, 'success.html', context)