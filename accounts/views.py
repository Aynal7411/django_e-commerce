from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render


from .forms import UserRegisterForm, UserProfileForm, AddressForm
from .models import Address


def register(request):
   if request.method == "POST":
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user)
          messages.success(request, "Account created successfully!")
          return redirect("catalogue:product_list")
   else:
      form = UserRegisterForm()
   return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("catalogue:product_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("catalogue:product_list")

@login_required
def profile(request):
   profile = request.user.userprofile
   if request.method == "POST":
      form = UserProfileForm(request.POST, request.FILES, instance=profile)
      if form.is_valid():
       form.save()
       messages.success(request, "Profile updated!")
       return redirect("accounts:profile")
   else:
     form = UserProfileForm(instance=profile)
   return render(request, "accounts/profile.html", {"form": form})


@login_required
def address_list(request):
    addresses = request.user.addresses.all()
    return render(request, "accounts/address_list.html", {"addresses": addresses})






@login_required
def address_create(request):
   if request.method == "POST":
      form = AddressForm(request.POST)
      if form.is_valid():
         address = form.save(commit=False)
         address.user = request.user
         if address.is_default:
            request.user.addresses.update(is_default=False)
         address.save()
         messages.success(request, "Address added!")
         return redirect("accounts:address_list")
   else:
       form = AddressForm()
   return render(request, "accounts/address_form.html", {"form": form})






@login_required
def address_update(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == "POST":
       form = AddressForm(request.POST, instance=address)
       if form.is_valid():
          addr = form.save(commit=False)
          if addr.is_default:
              request.user.addresses.update(is_default=False)
          addr.save()
          messages.success(request, "Address updated!")
          return redirect("accounts:address_list")
    else:
      form = AddressForm(instance=address)
    return render(request, "accounts/address_form.html", {"form": form})




@login_required
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == "POST":
       address.delete()
       messages.success(request, "Address deleted!")
       return redirect("accounts:address_list")
    return render(request, "accounts/address_confirm_delete.html", {"address": address})