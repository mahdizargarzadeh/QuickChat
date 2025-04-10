from django.shortcuts import render
from django.views import View


# Create your views her
class Main(View):
    def get(self, request):
        return render(request, 'chat/main.html')
