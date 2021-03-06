from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from accounts.forms import SignupForm


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # make user login
            auth_login(request, user)

            # move to HOME page
            return redirect('home')
    return render(request, 'signup.html', {'form': form})
