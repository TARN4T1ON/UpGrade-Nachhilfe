import os
import sys

from django.core.management import execute_from_command_line

from page import settings

# @TODO: comment

def main() -> None:
    """
    Entry function
    """

    print("main()")

    # only used for debugging; cgi should have it's own parameter

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "page.settings"
    )

    # find static files, move into static_root

    execute_from_command_line(
        [
            settings.rootPage,
            "findstatic",
        ] + settings.STATICFILES_DIRS
    )

    # run server

    execute_from_command_line(
        [
            settings.rootPage,
            "runserver",
            "--insecure",
            "%s:%s" % (
                settings.url, 
                settings.port
            ),
        ]
    )

    print("main()::return")

    return

if __name__ == "__main__":
    main()