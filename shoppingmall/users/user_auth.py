from users.models import CustomUser as User


class UserBackend(object):
    def authenticate(self, user_id=None, password=None):
        user = User.objects.filter(user_id=user_id, password=password)
        return user
