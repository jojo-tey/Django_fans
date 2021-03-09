from django.shortcuts import render, redirect
from tier.forms import NewTierForm

from tier.models import Tier

# Create your views here.


def NewTier(request):
    user = request.user

    if request.method == "POST":
        form = NewTierForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            can_message = form.cleaned_data.get('can_message')

            Tier.objects.create(description=description,
                                price=price, user=user, can_message=can_message)
            return redirect('index')
    else:
        form = NewTierForm()

    context = {
        'form': form,
    }

    return render(request, 'newtier.html', context)
