from django.http import HttpRequest, HttpResponse

from django.contrib.auth import logout as _logout
from django.contrib.auth.models import User

from page.views.view import view
import page.views.message as message

class logout(view):
    def get(
        self, 
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        msg: message
        if request.user.is_authenticated:
            _logout(request)

            msg = message.message(
                message.types.SUCCESS.name,
                "Erfolgreich ausgeloggt!",
                response
            )

            self.redirect(
                response
            )
        else:
            msg = message.message(
                message.types.ERROR.name,
                "Nicht eingeloggt!",
                response
            )

            self.redirect(
                response
            )

        return response