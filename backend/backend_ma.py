from .extension import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'phonenumber', 'balance', 'role', 'datejoin')