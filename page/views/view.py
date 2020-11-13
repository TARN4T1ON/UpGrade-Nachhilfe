from django.template import loader, Context, Template
from django.http import HttpRequest, HttpResponse

class view:
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
        if self.path == None:
            return None
        else:
            return loader.get_template(self.path)

    def render(self) -> str:
        return self.load().render(self.context)

    def handler(self, request : HttpRequest) -> HttpResponse:
        return HttpResponse(
            self.render(), 
            self.context
        )