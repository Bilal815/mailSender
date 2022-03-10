from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail(
        'Saying Hello...',
        'This is just a test message',
        'test@gmail.com',
        ['a.f@coded.com'],
        fail_silently=False
    )
    return render(request, 'send/index.html')
