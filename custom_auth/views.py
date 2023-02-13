from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View, generic
from django.db import transaction
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class CustomPermissionMixin(PermissionRequiredMixin):
    permission_required = ""
    allowed_roles=['ADMIN']
    def has_permission(self) -> bool:
        if self.request.user.groups.exists():
            groups = self.request.user.groups.all()
            for group in groups:
                if group.name in self.allowed_roles:
                    return True
            return False
        return False


class CommonMixin(SuccessMessageMixin, LoginRequiredMixin, CustomPermissionMixin):
    permission_required = ""
    permission_denied_message = "You don't have permission"
    title = ""

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['title'] = self.title
        return data


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_message = "User created successfully"
    title = "New user registration"
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy("user_create_form")

    def form_valid(self, form, *args, **kwargs):
        with transaction.atomic():
            form.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['form'] = self.get_form()
        return context