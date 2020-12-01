import os
import sys

from django.core.management import execute_from_command_line

import page.globall as globall
import page.settings.settings as settings

# @TODO: comment

def main() -> None:
    """
    Entry function
    """

    print("main()")

    # only used for debugging; cgi should have it's own parameter

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "page.settings.settings"
    )

    # find static files, move into static_root

    execute_from_command_line(
        [
            globall.page,
            "findstatic",
        ] + settings.STATICFILES_DIRS
    )

    # run server

    execute_from_command_line(
        [
            globall.page,
            "runserver",
            "--insecure",
            "%s:%s" % (
                globall.url, 
                globall.port
            ),
        ]
    )

    print("main()::return")

    return

if __name__ == "__main__":
    main()