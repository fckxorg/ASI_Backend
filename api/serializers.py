from django.contrib.auth.models import User
import base64

class UserSerializer:
    @staticmethod
    def serialize(user):
        not_needed_keys = ["last_login", "password", "is_superuser", "is_staff", "is_active", "date_joined", "_password", "_state"]
        data = vars(user)
        additional_data = vars(user.profile)
        try:
            # string slice required to fix python byte-object to string cast
            additional_data["avatar"] = str(base64.b64encode(user.profile.avatar.read()))[2:-1]
        except FileNotFoundError:
            additional_data["avatar"] = "None"
        except ValueError:
            additional_data["avatar"] = "None"
        keys = list(data.keys())
        for key in keys:
            if key in not_needed_keys:
                del data[key]
        del additional_data["id"]
        del additional_data["user_id"]
        del additional_data["_state"]

        result = {**data, **additional_data}
        return result
