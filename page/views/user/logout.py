from django.http import HttpRequest, HttpResponse

from django.contrib.auth import logout as _logout
from django.contrib.auth.models import User

from page.views.view import view

class logout(view):
    def get(
        self, 
        request: HttpRequest
    ) -> HttpResponse:
        response = HttpResponse()

        if request.user.is_authenticated:
            _logout(request)

            response.status_code = 301
            response["Location"] = "/"
        else:
            response.status_code = 400

        return response