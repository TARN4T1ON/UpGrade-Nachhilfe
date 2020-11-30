import json
from django.http import HttpResponse
import urllib.parse as parse

TYPES = {
    "SUCCESS": 0,
    "ERROR": 1,
    "WARNING": 2,
}

COLORS = {
    0: "var(--color-accent)",
    1: "var(--color-error)",
    2: "var(--color-warning)",
}

class message:
    type: int

    message: str
    color: str

    def __init__(
        self,
        type: int,
        message: str,
        color: str = None
    ):
        self.type = type
        self.message = message

        if color == None:
            try:
                self.color = COLORS[self.type]
            except:
                self.color = COLORS[0]
        else:
            self.color = color

    def toJSON(
        self
    ) -> str:
        return json.dumps(
            {
                "type": self.type,
                "message": self.message,
                "color": self.color,
            }
        )

    def cookie(
        self,
        response: HttpResponse
    ) -> None:
        json = self.toJSON()
        encode = parse.quote_plus(json)

        response.set_cookie(
            "message",
            encode,
            None,
            None,
            "/",
            "localhost"
        )
        response.cookies["message"] = encode