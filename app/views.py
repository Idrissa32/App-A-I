from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from blog import settings
from .token import generatorToken
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
# Create your views here.

def register(request):
    if request.method =="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request,"Ce nom a ete deja pris")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request,"Ce emai a deja un compt")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, 'Le nom doit etre alphanumeric')
            return redirect('register')
        
        if password != password1:
            messages.error(request, 'Les deux mot de passe ne coincident pas.')
            return redirect('register')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'Votre compte a ete cree avec success')
        #envoie d'email de bienvenue
        subject = "Bienvenue sur notre site"
        message = "Bienvenue "+ my_user.first_name + " " + my_user.last_name+ "\n Nous somme heureux de vous compter parmi nous\n\n\n Merci \n\n speed"
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        #Email de confirmation
        current_site = get_current_site(request)
        email_subject = "Confirmation de l'adrees email sur notre site"
        messageConfirm = render_to_string("emailcomfirm.html", {
            "name":my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token':generatorToken.make_token(my_user)

        })

        email = EmailMessage(
            email_subject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('login')
    return render(request, 'app/register.html')

def logIn(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return redirect('index')
        elif my_user.is_active == False:
            messages.error(request, "Vous n'avez pas activer votre compte veuille activer votre compte avant de vous connecter.")
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')
    return render(request, 'app/login.html')

def logOut(request):
    logout(request)
    return redirect('home')

def activate(request, uidb64, token ):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, User.DoesNotExist):
        user = None

    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Votre compte a ete activate felicitation connectez-vous maintenant")
        return redirect('login')
    else:
        messages.error(request, "Echec d'actvation")
        return redirect('home')

