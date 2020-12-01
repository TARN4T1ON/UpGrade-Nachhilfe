from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from page.views.view import view
import page.views.message as message

class login(view):
    def post(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        # get username and password from POST data

        username = request.POST["username"]
        password = request.POST["password"]

        # try to authenticate user

        user = authenticate(
            username = username,
            password = password
        )

        msg: message
        if user == None:
            # user doesn't exist;
            # display error message on page redirect

            msg = message.message(
                message.types.ERROR.name,
                "Dieser Benutzer existiert nicht!",
                response
            )

            response["Location"] = self.url
            response.status_code = 302
        else:
            # user exists
            # log in user

            _login(
                request,
                user
            )

            # display success message on page redirect

            msg = message.message(
                message.types.SUCCESS.name,
                "Erfolgreich eingeloggt!",
                response
            )

            response["Location"] = "/"
            response.status_code = 302
            
        return response