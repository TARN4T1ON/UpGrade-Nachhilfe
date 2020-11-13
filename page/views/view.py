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

        self.context = None

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

    def handler(self, request : HttpRequest) -> HttpResponse:
        """Overridable Request Handler"""

        return HttpResponse(
            self.render(), 
            self.context
        )