from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt

from models.base import BaseModel


class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    favourite_region = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=True)

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    # This is for Admin: 1 is normal user 2 is admin user
    roles = db.Column(db.Integer, nullable=False)

    # Password_hash will be saved in the database
    password_hash = db.Column(db.Text, nullable=True)

    # Opposite relationship
    projects = db.relationship("ProjectModel", back_populates="users")
    regions = db.relationship("RegionModel", back_populates="users")

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        print("hashing password", self)
        # Hash password from signup
        encoded_hashed_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_hashed_pw.decode("utf-8")

    def validate_password(self, login_password):
        # compare the hash password with the login password
        return bcrypt.check_password_hash(self.password_hash, login_password)
