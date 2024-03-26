import django.urls

from . import views

app_name = 'download'

urlpatterns = [
    django.urls.path(
        '<path:path>',
        views.file,
        name='file',
    )
]