import logging
import urllib.parse

from django.shortcuts import render, redirect
from django.conf import settings
import django.contrib.auth

logger = logging.getLogger('tock')


def csrf_failure(request, reason=""):
    logger.warn(
        'CSRF Failure for request [%s] for reason [%s]' %
        (
            request.META,
            reason
        )
    )
    return render(request, '403.html')


def logout(request):
    if request.user.is_authenticated():
        django.contrib.auth.logout(request)
        tock_logout_url = request.build_absolute_uri('logout')
        params = urllib.parse.urlencode({
            'redirect': tock_logout_url,
            'client_id': settings.UAA_CLIENT_ID,
        })
        return redirect(
            f'{settings.UAA_LOGOUT_URL}?{params}'
        )
    else:
        return render(request, 'logout.html')


# TODO: new function signature for Django 2.0
# def handler400(request, exception, template_name='400.html'):
def handler400(request):
    response = render(
        request,
        '400.html',
        {}
    )
    response.status_code = 400
    return response


# TODO: new function signature for Django 2.0
# def handler403(request, exception, template_name='403.html'):
def handler403(request):
    response = render(
        request,
        '403.html',
        {}
    )
    response.status_code = 403
    return response


# TODO: new function signature for Django 2.0
# def handler404(request, exception, template_name='404.html'):
def handler404(request):
    response = render(
        request,
        '404.html',
        {}
    )
    response.status_code = 404
    return response


# TODO: new function signature for Django 2.0
# def handler500(request, exception, template_name='500.html'):
def handler500(request):
    response = render(
        request,
        '500.html',
        {}
    )
    response.status_code = 500
    return response
