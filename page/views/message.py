import json
import urllib.parse as parse
from enum import Enum

from django.http import HttpResponse

import page.globall as globall
import page.settings as settings

class types(Enum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"

TIME: int = 7500

class message:
    type: str

    message: str

    time: int

    def __init__(
        self,
        type: str,
        message: str,
        response: HttpResponse = None,
        time: int = TIME
    ):
        self.type = type

        self.message = message

        self.time = time

        if response != None:
            self.cookie(
                response
            )

    def toJSON(
        self
    ) -> str:
        """
        Returns JSON string of own members
        """

        return json.dumps(
            {
                "type": self.type,
                "message": self.message,
                "time": self.time,
            }
        )

    def cookie(
        self,
        response: HttpResponse
    ) -> None:
        """
        Adds message to Cookies as Session Cookie\n
        Displayed on next page load by layout
        """

        json = self.toJSON()
        encode = parse.quote(json)

        response.set_cookie(
            "message",
            encode,
            None,
            None,
            "/",
            globall.url
        )