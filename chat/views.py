from django.shortcuts import render
from django.views import View


# Create your views her
class Main(View):
    def get(self, request):
        return render(request, 'chat/main.html')

class Login(View):
    def get(self, request):
        return render(request, 'chat/login.html')

class Register(View):
    def get(self, request):
        return render(request, 'chat/register.html')

class Logout(View):
    def get(self, request):
        # run operator
        pass

class Home(View):
    def get(self, request):
        return render(request, 'chat/home.html')

class ChatPerson(View):
    def get(self, request):
        return render(request, 'chat/chat_person.html')
