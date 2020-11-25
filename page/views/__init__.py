from page.views.index import index
from page.views.about import about

from page.views.user.register import register
from page.views.user.login import login
from page.views.user.logout import logout

instances = {
    "index": index(
        "index",
        "./index.html",
        ""
    ),
    "about": index(
        "about",
        "./about.html",
        "about"
    ),

    "register": register(
        "register",
        "./user/register.html",
        "user/register"
    ),
    "login": login(
        "login",
        "./user/login.html",
        "user/login"
    ),
    "logout": logout(
        "logout",
        "./user/logout.html",
        "user/logout"
    ),
}