from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('realynx-home')
    else:
        form = UserSignupForm()
    # Render blank form if no post request(page refresh clears form) 
    # Render form instantiated with invalid POST (Aside passwords, form fields retain data)
    return render(request, "users/signup.html", {"form":form})


"""
messages.debug()
messages.info()
messages.success()
messages.warning()
messages.error()

"""