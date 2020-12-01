from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

import page.views as views

# >>>
# Django URL Configuration
# >>>

urlpatterns = [
    # favicon definition
    path(
        "favicon.ico",
        RedirectView.as_view(
            url = staticfiles_storage.url("assets/favicon.ico")
        )
    )
]

# iterate over views and add to patterns

for key in views.instances:
    instance = views.instances[key]

    urlpatterns.append(
        path(
            instance.url,
            instance.handler,
            name = instance.name
        )
    )

# error handlers

handler400 = "page.views.status.status.handler400"
handler403 = "page.views.status.status.handler403"
handler404 = "page.views.status.status.handler404"
handler500 = "page.views.status.status.handler500"