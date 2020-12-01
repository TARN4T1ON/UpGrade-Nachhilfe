from django.template import loader, Context, Template
from django.http import HttpRequest, HttpResponse

names = {
    400: "Ungültige Anfrage",
    403: "Verboten",
    404: "Nicht Gefunden",
    500: "Interner Fehler",
}

messages = {
    400: "Die HTTP Anfrage entsprach nicht den Erwartungen",
    403: "Du besitzt nicht die benötigten Berechtigungen um auf diese Ressource zuzugreifen.",
    404: "Die angeforderte Ressource existiert nicht.",
    500: "Ein Fehler, für den du wahrscheinlich nichts kannst, ist aufgetreten.",
}

class statusContext:
    code: int
    name: str
    message: str

    def __init__(
        self,
        code: int,
        name: str = None,
        message: str = None
    ):
        self.code = code

        if name == None:
            self.name = names[self.code]
        else:
            self.name = name

        if message == None:
            self.message = messages[self.code]
        else:
            self.message = message

    def toDict(
        self
    ) -> dict():
        return {
            "code": self.code,
            "name": self.name,
            "message": self.message,
        }

def handler400(
    request: HttpRequest,
    *args,
    **argv
):
    return handler(
        statusContext(
            400
        ),
        request,
        args,
        argv
    )

def handler403(
    request: HttpRequest,
    *args,
    **argv
):
    return handler(
        statusContext(
            403
        ),
        request,
        args,
        argv
    )

def handler404(
    request: HttpRequest,
    *args,
    **argv
):
    return handler(
        statusContext(
            404
        ),
        request,
        args,
        argv
    )

def handler500(
    request: HttpRequest,
    *args,
    **argv
):
    return handler(
        statusContext(
            500
        ),
        request,
        args,
        argv
    )

def handler(
    status: statusContext,
    request: HttpRequest,
    *args,
    **argv
):
    template: Template = loader.get_template("./status.html")
    render: str = template.render(
        status.toDict()
    )

    response = HttpResponse(
        render
    )

    return response