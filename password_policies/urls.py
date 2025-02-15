try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

try:
    # patterns was deprecated in Django 1.8
    from django.conf.urls import patterns
except ImportError:
    # patterns is unavailable in Django 1.10+
    patterns = False

from password_policies.views import (
    PasswordChangeDoneView,
    PasswordChangeFormView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetFormView,
)

urlpatterns = [
    url(
        r"^change/done/$", PasswordChangeDoneView.as_view(), name="password_change_done"
    ),
    url(r"^change/$", PasswordChangeFormView.as_view(), name="password_change"),
    url(r"^reset/$", PasswordResetFormView.as_view(), name="password_reset"),
    url(
        r"^reset/complete/$",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    url(
        r"^reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13})/([0-9A-Za-z-=_]{1,128})/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    url(r"^reset/done/$", PasswordResetDoneView.as_view(), name="password_reset_done"),
]

if patterns:
    # Django 1.7
    urlpatterns = patterns("", *urlpatterns)
