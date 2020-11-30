from page.views.index import index
from page.views.about import about

from page.views.user.register import register
from page.views.user.login import login
from page.views.user.logout import logout

instances = {
    "index": index(
        "index",
        "./index.html",
        "",
        [
            "HOME"
        ]
    ),
    "about": index(
        "about",
        "./about.html",
        "about/",
        [
            "ÜBER UNS"
        ]
    ),

    "register": register(
        "register",
        "./user/register.html",
        "user/register/",
        [
            "BENUTZER",
            "REGISTRIEREN"
        ]
    ),
    "login": login(
        "login",
        "./user/login.html",
        "user/login/",
        [
            "BENUTZER",
            "EINLOGGEN"
        ]
    ),
    "logout": logout(
        "logout",
        "./user/logout.html",
        "user/logout/",
        [
            "BENUTZER",
            "AUSLOGGEN"
        ]
    ),
}