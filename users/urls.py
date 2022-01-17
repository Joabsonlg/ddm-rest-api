from django.conf.urls import url

from users.views import PasswordResetView

urlpatterns = [
    url(r'^password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', PasswordResetView.as_view(), ),
]
