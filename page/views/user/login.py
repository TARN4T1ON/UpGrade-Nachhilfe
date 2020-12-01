from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login as _login, authenticate

from django.contrib.auth.models import User

from page.views.view import view
import page.views.message as message

import page.views.user.validation as validation

class login(view):
    def post(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        response = HttpResponse()

        errors = []

        # get username or email and password from POST data
        # validate username or email and password

        username = request.POST["username"]
        validation.validateUsername(
            username,
            errors,
            False
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
            # try to authenticate user

            user = authenticate(
                request,
                username = username,
                password = password
            )

            if user == None:
                # user doesn't exist;
                # display error message on page redirect

                msg = message.message(
                    message.types.ERROR.name,
                    "Dieser Benutzer existiert nicht!",
                    response
                )

                self.redirect(
                    response,
                    "/" + self.url
                )
            else:
                # user exists
                # log in user

                if user.check_password(
                    password
                ):
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

                self.redirect(
                    response
                )
            
        return response