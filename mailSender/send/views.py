from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail(
        'Saying Hello...',
        'This is just a test message',
        'Bilalahmed815@gmail.com',
        ['ahmed.faraz@codelabs.inc'],
        fail_silently=False
    )
    return render(request, 'send/index.html')