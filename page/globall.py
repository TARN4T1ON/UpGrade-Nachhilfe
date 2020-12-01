import os



# >>>
# Global
# >>>



# page root
page = os.path.realpath(
    os.path.dirname(
        __file__
    )
)

# project root
root = os.path.realpath(
    os.path.dirname(
        page
    )
)



# >>>
# Website
# >>>


url = "localhost"
port = 8000

separator = " :: "