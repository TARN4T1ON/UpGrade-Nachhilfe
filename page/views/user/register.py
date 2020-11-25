from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login
from django.contrib.auth.models import User

from page.views.view import view

class register(view):
    def get(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        response.content = self.render(context)
        return response

    def post(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        username = request.POST["username"]
        password = request.POST["password"]

        exists = User.objects.filter(
            username = username
        ).exists()

        if exists:
            response.content = "user already exists"
            return response

        user: User = User.objects.create(
            username = username
        )
        user.set_password(password)
        user.save()

        _login(
            request,
            user
        )

        response.content = "user created"
        return response