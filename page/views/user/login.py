from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from page.views.view import view

class login(view):
    def get(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        response = HttpResponse()

        response.content = self.render()
        return response

    def post(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        response = HttpResponse()

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            username = username,
            password = password
        )

        if user == None:
            response.content = "invalid user"
        else:
            _login(
                request,
                user
            )

            response.content = "authenticated user %s" % user.username
            
        return response