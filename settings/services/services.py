from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_data(user_id):
    user_data = User.objects.get(id=user_id)
    return {
        "username": user_data.username,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "email": user_data.email,
        "password": user_data.password,
    }