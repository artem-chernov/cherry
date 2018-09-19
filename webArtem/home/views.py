from django.shortcuts import render
from .forms import OrderForm, NewOrderForm
from django.http import HttpResponse
from .models import Order



def home(request):
    form = NewOrderForm()
    if request.method == 'POST' and request.is_ajax():
        print("server_ok")
        form = NewOrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            return HttpResponse(status=200)
    return render(request, 'home.html', {'form':form})
