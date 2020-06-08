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

        # Stripe only accepts int values
        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['name'],
            source = request.POST['stripeToken'],
            )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount * 100,
            currency = "usd",
            description = "Donation"
            )

        return redirect(reverse('success'))

def successPageView(request):

    context = {}
    return render(request, 'success.html', context)