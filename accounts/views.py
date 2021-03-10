from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

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


class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', 'username')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


