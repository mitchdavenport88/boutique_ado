from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdBkIFZyCWoSHERmnXfDSsfSGJclc6paQqPH2oY4rvNm2ahaY6MdCvPC1T7zQ4d6XTAJETpf2AGzoNBWZ2hGlWR00xvkCE8sk',
        'client_secret': 'sk_test_51JdBkIFZyCWoSHERuq69XzKJfCX9185xiIR9tsP3HNf96y4HBzaZ7Y2HjFFXIW15G18BSjXRvNjOn83GDUkK5w9t00cXQ3I2nr',
    }

    return render(request, template, context)
