import os
import shutil

working = os.path.dirname(
    os.path.realpath(
        __file__
    )
)

root = os.path.dirname(
    working
)

for (path, dirs, files) in os.walk(root):
    for dir in dirs:
        if dir.lower() == "__pycache__":
            path = os.path.join(
                path,
                dir
            )

            shutil.rmtree(
                path
            )