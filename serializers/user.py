from marshmallow import fields, ValidationError, validates_schema
from app import marsh
from models.user import UserModel


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
        raise ValidationError("Password should have at least one of the symbols $@#%!")


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    # ! Adding a pw field
    #  Add custom validation to password (validate=)
    password = fields.String(required=True, validate=validate_password)
    password_confirm = fields.String(required=True)
    project_id = fields.Nested("ProjectSchema", many=True)

    # Comapre password to password confirmation
    @validates_schema
    def validate_passwords_match(self, data, **kwargs):
        if data.get("password") != data.get("password_confirm"):
            raise ValidationError("Passwords do not match")

    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password_hash",)
        # Fields only allowed when loading
        load_only = ("password_hash", "email", "password", "password_confirm")
