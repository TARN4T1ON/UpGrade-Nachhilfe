from typing import Any
from django.template import loader, Context, Template
from django.http import HttpRequest, HttpResponse

class view:
    """View Wrapper Class"""

    name : str
    path : str
    url : str

    context : dict()

    def __init__(
        self,
        name : str,
        path : str,
        url : str
    ):
        self.name = name
        self.path = path
        self.url = url

        self.context = {}

        return

    def load(self) -> Template:
        """Loads Django Template from Self Defined Path"""

        if self.path == None:
            return None
        else:
            return loader.get_template(self.path)

    def render(self) -> str:
        """Renders Django Template using Self Defined Context"""

        return self.load().render(self.context)

    def middleware(
        self,
        request: HttpRequest
    ) -> None:
        """
        Overridable Middleware called before specific Request Handler
        """

        pass

    def handler(
        self, 
        request: HttpRequest
    ) -> HttpResponse:
        """
        Internal handler\n
        Transfers request to more specific handler
        """

        self.middleware(
            request
        )

        if request.method == "GET":
            return self.get(
                request
            )
        elif request.method == "HEAD":
            return self.head(
                request
            )
        elif request.method == "POST":
            return self.post(
                request
            )
        elif request.method == "PUT":
            return self.put(
                request
            )
        elif request.method == "DELETE":
            return self.delete(
                request
            )
        elif request.method == "CONNECT":
            return self.connect(
                request
            )
        elif request.method == "OPTIONS":
            return self.options(
                request
            )
        elif request.method == "TRACE":
            return self.trace(
                request
            )
        elif request.method == "PATCH":
            return self.patch(
                request
            )

    def get(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable GET Handler
        """

        return HttpResponse(
            self.render(),
            self.context
        )

    def head(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable HEAD Handler
        """

        return HttpResponse(
            None,
            self.context
        )

    def post(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable POST Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def put(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable PUT Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def delete(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable DELETE Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def connect(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable CONNECT Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def options(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable OPTIONS Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def trace(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable TRACE Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

    def patch(
        self,
        request: HttpRequest
    ) -> HttpResponse:
        """
        Overridable PATCH Handler
        """

        response = HttpResponse()
        response.content = ""
        response.status_code = 400
        return response

def _middleware(
    self,
    request: HttpRequest
) -> None:
    self.context["user"] = request.user.is_authenticated

    return

view.middleware = _middleware