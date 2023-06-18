from django.shortcuts import render, redirect
from .models import Donor, Donation

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donation_list.html', {'donations': donations})

def new_donation(request):
    if request.method == 'POST':
        donor_name = request.POST['donor_name']
        donor_email = request.POST['donor_email']
        donation_amount = request.POST['donation_amount']

        donor, created = Donor.objects.get_or_create(name=donor_name, email=donor_email)
        Donation.objects.create(donor=donor, amount=donation_amount)

        return redirect('donation_list')
    
    return render(request, 'new_donation.html')
