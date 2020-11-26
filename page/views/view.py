from django.template import loader, Context, Template
from django.http import HttpRequest, HttpResponse

import page.settings as settings
import page.views.status as status

class view:
    """View Wrapper Class"""

    name: str
    path: str
    url: str
    title: str

    def __init__(
        self,
        name: str,
        path: str,
        url: str,
        title: str = ""
    ):
        self.name = name
        self.path = path
        self.url = url

        self.title = title

        return

    def load(self) -> Template:
        """Loads Django Template from Self Defined Path"""

        if self.path == None:
            return None
        else:
            return loader.get_template(self.path)

    def render(
        self,
        context: dict()
    ) -> str:
        """Renders Django Template using Self Defined Context"""

        return self.load().render(
            context
        )

    def middleware(
        self,
        request: HttpRequest,
        context: dict()
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

        context = {}

        self.middleware(
            request,
            context
        )

        method: function = None
        if request.method == "GET":
            method = self.get
        elif request.method == "HEAD":
            method = self.head
        elif request.method == "POST":
            method = self.post
        elif request.method == "PUT":
            method = self.put
        elif request.method == "DELETE":
            method = self.delete
        elif request.method == "CONNECT":
            method = self.connect
        elif request.method == "OPTIONS":
            method = self.options
        elif request.method == "TRACE":
            method = self.trace
        elif request.method == "PATCH":
            method = self.patch

        if method != None:
            output = method(
                request,
                context
            )

            if output.status_code == 400:
                return status.handler400(
                    request
                )
            elif output.status_code == 403:
                return status.handler403(
                    request
                )
            elif output.status_code == 404:
                return status.handler404(
                    request
                )
            elif output.status_code == 500:
                return status.handler500(
                    request
                )
            else:
                return output

    def get(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        """
        Overridable GET Handler
        """

        return HttpResponse(
            self.render(
                context
            )
        )

    def head(
        self,
        request: HttpRequest,
        context: dict()
    ) -> HttpResponse:
        """
        Overridable HEAD Handler
        """

        return HttpResponse(
            None
        )

    def post(
        self,
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
        request: HttpRequest,
        context: dict()
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
    request: HttpRequest,
    context: dict()
) -> None:
    context["user"] = request.user.is_authenticated
    
    if self.title != "":
        context["title"] = settings.separator + settings.separator.join(self.title)
    else:
        context["title"] = ""

    return

view.middleware = _middleware