from .models import User
from django.core.exceptions import ObjectDoesNotExist


class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_user(**kwargs):
        password = kwargs.pop('password', None)
        user = User.objects.create_user(password=password, **kwargs)
        return user

