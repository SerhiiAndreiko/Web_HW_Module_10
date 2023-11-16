from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return render(request, self.template_name, context={ "form": self.form_class })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Your account '{username}' was created...")
            return redirect(to="users:login")
        else:
            messages.error(request, "Not registered...")
            return render(request, self.template_name, context={"form": form})

