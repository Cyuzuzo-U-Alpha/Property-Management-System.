# properties/views.py
from django.http import HttpResponse

from .forms import PropertySearchForm
from django.shortcuts import render, redirect

from .models import Property


def home(request):
    return HttpResponse("Welcome to the Property Management System!")

def property_list(request):
    form = PropertySearchForm(request.GET)
    properties = Property.objects.all()

    # If the form is valid, apply the filters
    if form.is_valid():
        location = form.cleaned_data.get('location')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        # Apply filters only if the corresponding field has data
        if location:
            properties = properties.filter(address__icontains=location)
        if price_min:
            properties = properties.filter(rent__gte=price_min)
        if price_max:
            properties = properties.filter(rent__lte=price_max)

    # Render the template with the properties and the search form
    return render(request, 'property_list.html', {
        'properties': properties,
        'form': form
    })


def property_detail(request):
    return render(request, 'property_detail.html', {'property': property})

from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.password.role != 'Admin':
        return redirect('home')
    return render(request, 'dashboard/admin_dashboard.html')


def search_properties(request):
    query = request.GET.get('q', '')
    properties = Property.objects.filter(name__icontains=query) if query else Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})