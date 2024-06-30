from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"{username} your account has been created. Please log in",
            )
            return redirect("auth-login")
        else:
            form = UserSignupForm()
            # Clear both password input and retains other fields
            return render(request, "users/signup.html", {"form": form})
    else:
        form = UserSignupForm()
        # Clear all field input
        return render(request, "users/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")


"""
messages.debug()
messages.info()
messages.success()
messages.warning()
messages.error()

"""
