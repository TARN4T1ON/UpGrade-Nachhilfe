from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login
from django.contrib.auth.models import User

from page.views.view import view
import page.views.message as message

class register(view):
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

        msg: message
        if exists:
            msg = message.message(
                message.types.ERROR.name,
                "Dieser Benutzer existiert bereits!",
                response
            )

            response["Location"] = self.url
            response.status_code = 302
        else:
            user: User = User.objects.create(
                username = username
            )
            user.set_password(password)
            user.save()

            _login(
                request,
                user
            )

            msg = message.message(
                message.types.SUCCESS.name,
                "Erfolgreich registriert!",
                response
            )

            response["Location"] = "/"
            response.status_code = 302

        return response