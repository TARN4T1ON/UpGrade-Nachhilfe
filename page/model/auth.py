from typing import Any, Optional

from django.db.models.base import Model

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class email(ModelBackend):
    """
    Authentication Backend allowing for Username = Username and Username = Email authentication
    """

    def authenticate(
        self, 
        request: Any, 
        username: Optional[str], 
        password: Optional[str], 
        **kwargs: Any
    ) -> Optional[AbstractBaseUser]:
        model: Model = get_user_model()
        
        user: User
        try:
            user = model.objects.get(
                username = username
            )
        except:
            try:
                user = model.objects.get(
                    email = username
                )
            except:
                return None

        if user.check_password(
            password
        ):
            return user
        else:
            return None
