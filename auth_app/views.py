from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # Here, to go any page of our website user login is required. So, after login we can take user directly to*
            # *their required site. Note: request.GET ==>> gives the current url.
            next_url = request.GET.get('next')

            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username and password')
            messages.error(
                request, 'Please enter valid username and password!!!!')
            return redirect('signin')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            # If username is already exist then we don't need to register such username again and again.
            user = User.objects.get(username=username)
            messages.info(request, 'Account already exist.')
            return redirect('signin')

        except User.DoesNotExist:
            User.objects.create_user(
                username=username, email=email, password=password)

            # :::::::::send_mail code:::::::::::::::
            send_mail(
                'Account Created',
                f'An account has been created for you. Your username is {username}',
                settings.EMAIL_HOST_USER,
                ['email', 'kabinbasnet22@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Account has been created.')

            return redirect('signin')

# :::::::::logout code:::::::::


def signout(request):
    logout(request)
    return redirect('home')
