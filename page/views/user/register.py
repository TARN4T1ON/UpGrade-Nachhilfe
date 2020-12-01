from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login
from django.contrib.auth.models import User

from page.views.view import view
import page.views.message as message

import page.views.user.validation as validation

class register(view):
    def post(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        errors = []

        # get username, email and password from POST data

        username = request.POST["username"]
        validation.validateUsername(
            username,
            errors
        )

        email = request.POST["email"]
        validation.validateEmail(
            email,
            errors
        )

        password = request.POST["password"]
        validation.validatePassword(
            password,
            errors
        )

        msg: message

        # check if validation error occurred

        if len(errors) > 0:
            _msg = validation.messageCompile(
                errors
            )

            msg = message.message(
                message.types.ERROR.name,
                _msg,
                response,
                message.TIME * 2
            )

            self.redirect(
                response,
                "/" + self.url
            )

        else:
            exists = User.objects.filter(
                username = username
            ).exists()
            
            if exists:
                msg = message.message(
                    message.types.ERROR.name,
                    "Dieser Benutzer existiert bereits!",
                    response
                )

                self.redirect(
                    response,
                    "/" + self.url
                )
            else:
                user: User = User.objects.create(
                    username = username,
                    email = email
                )
                user.set_password(password)
                user.save()

                # @TODO: email verification

                _login(
                    request,
                    user
                )

                msg = message.message(
                    message.types.SUCCESS.name,
                    "Erfolgreich registriert!",
                    response
                )

                self.redirect(
                    response
                )

        return response