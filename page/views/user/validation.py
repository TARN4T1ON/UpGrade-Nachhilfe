from django.core.validators import validate_email

# >>>
# Username
# >>>



# @TODO: more general validation?

USERNAME_MIN_LENGTH = 4
USERNAME_MAX_LENGTH = 64
USERNAME_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"

def validateUsername(
    username: str,
    errors: list,
    alphabet: bool = True
):
    if username == None or username == "":
        errors.append(
            "Der Benutzername ist ein Pflichtfeld!"
        )
    else:
        _length = len(username)

        if _length < USERNAME_MIN_LENGTH:
            errors.append(
                "Die Länge des eingegeben Benutzernames ist kleiner als die Mindestlänge von %s Buchstaben!" % (USERNAME_MIN_LENGTH)
            )
        if _length > USERNAME_MAX_LENGTH:
            errors.append(
                "Die Länge des eingegeben Benutzernames ist größer als die Maximallänge von %s Buchstaben!" % (USERNAME_MAX_LENGTH)
            )

        if alphabet:
            chars = []
            for char in username:
                if char not in USERNAME_ALPHABET and char not in chars:
                    chars.append(char)

            if len(chars) > 0:
                if len(chars) == 1:
                    errors.append(
                        "Der Buchstabe \"%s\" ist innerhalb des Benutzernamens ungültig!" % (", ".join(chars))
                    )
                else:
                    errors.append(
                        "Die Buchstaben \"%s\" sind innerhalb des Benutzernamens ungültig!" % (", ".join(chars))
                    )



# >>>
# E-Mail
# >>>



EMAIL_MIN_LENGTH = 3
EMAIL_MAX_LENGTH = 320

def validateEmail(
    email: str,
    errors: list
):
    if email == None or email == "":
        errors.append(
            "Die E-Mail ist ein Pflichtfeld!"
        )
    else:
        _length = len(email)

        if _length < EMAIL_MIN_LENGTH:
            errors.append(
                "Die Länge der eingegeben E-Mail ist kleiner als die Mindestlänge von %s Buchstaben!" % (EMAIL_MIN_LENGTH)
            )
        if _length > EMAIL_MAX_LENGTH:
            errors.append(
                "Die Länge der eingegeben E-Mail ist größer als die Maximallänge von %s Buchstaben!" % (EMAIL_MAX_LENGTH)
            )
        
        try:
            validate_email(
                email
            )
        except:
            errors.append(
                "Die eingegebene E-Mail ist ungültig!"
            )



# >>>
# Password
# >>>



PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 128

def validatePassword(
    password: str,
    errors: list
):
    if password == None or password == "":
        errors.append(
            "Das Passwort ist ein Pflichtfeld!"
        )
    else:
        _length = len(password)

        if _length < PASSWORD_MIN_LENGTH:
            errors.append(
                "Die Länge des eingegeben Passwortes ist kleiner als die Mindestlänge von %s Buchstaben!" % (PASSWORD_MIN_LENGTH)
            )
        if _length > PASSWORD_MAX_LENGTH:
            errors.append(
                "Die Länge des eingegeben Passwortes ist größer als die Maximallänge von %s Buchstaben!" % (PASSWORD_MAX_LENGTH)
            )

def messageCompile(
    errors: list
) -> str:
    message: str = ""

    _length = len(errors)
    if _length > 0:
        if _length == 1:
            message = errors[0]
        else:
            message = "Mehrere Dinge sind schief gelaufen: "
            message += "<ul>"

            for error in errors:
                message += "<li>%s</li>" % (error)

            message += "</ul>"

    return message