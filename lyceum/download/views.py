from django.shortcuts import render
import django.http
import django.conf


# Create your views here.
def file(request, path):
    return django.http.FileResponse(
        open(django.conf.settings.MEDIA_ROOT / path, 'rb'),
        as_attachment=True,
    )
