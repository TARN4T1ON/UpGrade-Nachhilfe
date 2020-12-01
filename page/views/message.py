import json
import urllib.parse as parse
from enum import Enum

from django.http import HttpResponse

from page import settings

class types(Enum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"

class message:
    type: str

    message: str

    def __init__(
        self,
        type: str,
        message: str,
        response: HttpResponse = None
    ):
        self.type = type
        self.message = message

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
            settings.url
        )