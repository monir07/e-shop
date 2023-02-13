from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View, generic
from django.db import transaction
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class HomeView(View):
    template_name = 'eshop/index.html'

    def get(self, request, *args, **kwargs):
        
        context = {
            
        }
        return render(request, self.template_name, context)
