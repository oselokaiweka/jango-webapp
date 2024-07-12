from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Your account has been created. Please log in")
            return redirect("login")
        else:
            form = UserSignupForm()
            # Clear both password input and retains other fields
            messages.warning(request, "The password you provided is invalid.")
            return render(request, "users/signup.html", {"form": form})
    else:
        form = UserSignupForm()
        # Clear all field input
        return render(request, "users/signup.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,  # Pass in data of user on post method
            instance=request.user,  # Pass in data of logged in user on get method
        )

        profile_form = ProfileUpdateForm(
            request.POST,  # Pass in data of user on post method
            request.FILES,  # Pass in file data attached to the post method
            instance=request.user.profile,  # Pass in data of logged in user on get method
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile info has been updated!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "users/profile.html", context)


"""
messages.debug()
messages.info()
messages.success()
messages.warning()
messages.error()

"""
