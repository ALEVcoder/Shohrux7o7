from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def HomeContact(request):
    if request.method == 'POST':
        ism = request.POST['user']
        xabar = request.POST['xabar']
        email = request.POST['pochta']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nEmail: '+email+'\nXABAR Mazmuni:\n'+xabar

        print(ism, xabar, email)
        send_mail(
            ism,
            msg,
            email,
            ['shohruxislomov777@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html')