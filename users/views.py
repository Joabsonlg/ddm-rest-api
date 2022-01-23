from django.contrib import messages
from django.contrib.sites import requests
from django.urls import reverse
from requests import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, render
from djoser.conf import django_settings


class PasswordResetView(APIView):

    def get(self, request, uid, token):
        return render(request, 'users/email/change_password.html', {'uid': uid, 'token': token})

    def reset_user_password(request, uid, token):
        if request.POST:
            password = request.POST.get('password1')
            payload = {'uid': uid, 'token': token, 'new_password': password}

            url = '{0}://{1}{2}'.format(
                django_settings.PROTOCOL, django_settings.DOMAIN, reverse('password_reset_confirm'))

            response = requests.post(url, data=payload)
            if response.status_code == 204:
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('home')
            else:
                return Response(response.json())
        else:
            return render(request, 'templates/reset_password.html')
