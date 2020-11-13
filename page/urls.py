from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

import page.views as views

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url = staticfiles_storage.url("assets/favicon.ico")
        )
    )
]
for instance in views.instances:
    urlpatterns.append(
        path(
            instance.url,
            instance.handler,
            name = instance.name
        )
    )