from django.shortcuts import render
# from .models import (Company, Job, Person, App, CompanyProfile, PersonProfile)
# from django.urls import reverse_lazy
from django.views.generic import View
# Create your views here.

class homeView(View):
    def get(self, request, *args, **kwargs):
        request = self.request
        return render(request, 'home.html')