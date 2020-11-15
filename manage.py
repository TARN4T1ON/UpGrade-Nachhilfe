import os
import sys

from page import settings

# @TODO: comment

def main() -> None:
    print("main()")

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "page.settings"
    )

    try:
        from django.core.management import execute_from_command_line
    except:
        raise ImportError("main()::Error could not import django.core.management.execute_from_command_line")

    execute_from_command_line(
        [
            settings.root,
            "findstatic",
        ] + settings.STATICFILES_DIRS
    )

    execute_from_command_line(sys.argv)

    return

if __name__ == "__main__":
    main()