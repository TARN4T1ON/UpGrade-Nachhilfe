from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

import page.views as views

# @TODO: comment

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url = staticfiles_storage.url("assets/favicon.ico")
        )
    )
]
for key in views.instances:
    instance = views.instances[key]

    urlpatterns.append(
        path(
            instance.url,
            instance.handler,
            name = instance.name
        )
    )