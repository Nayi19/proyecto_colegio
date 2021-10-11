from django.views import View
from django.shortcuts import render

class landingPage(View):
    template = "Inicio.html"
    def get(self, request):
        return render(request, self.template, {})