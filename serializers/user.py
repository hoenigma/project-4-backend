from app import marsh
from models.user import UserModel
from marshmallow import fields, ValidationError


# Password validation
def validate_password(password):
    SpecialSym = ["$", "@", "#", "%", "!"]
    # Check length
    if len(password) < 8:
        raise ValidationError("Make sure password is 8 characaters long")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password should have at least one numeral")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password should have at least one uppercase letter")
    if not any(char in SpecialSym for char in password):
        raise ValidationError("Password should have at least one of the symbols $@#!")


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    # ! Adding a pw field
    #  Add custom validation to password (validate=)
    # password = fields.String(required=True, validate=validate_password)
    project_id = fields.Nested("ProjectSchema", many=True)

    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password_hash",)
        # Fields only allowed when loading
        load_only = ("password_hash", "email", "password")
