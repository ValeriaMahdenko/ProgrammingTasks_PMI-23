from validation import Validation
from app.app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class UserTable(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _first_name = db.Column(db.String(20), unique=False)
    _second_name = db.Column(db.String(20), unique=False)
    _email = db.Column(db.String(100), unique=False)
    _password = db.Column(db.String(1000), unique=False)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    @Validation.decorator_string
    def first_name(self, val):
        self._first_name = val

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    @Validation.decorator_string
    def second_name(self, val):
        self._second_name = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val, method='sha256')

    @property
    def email(self):
        return self._email

    @email.setter
    @Validation.decorator_email
    def email(self, val):
        self._email = val

    def to_json(self):
        d = {}
        d['user_id'] = self.user_id
        d['first_name'] = self.first_name
        d['second_name'] = self.second_name
        d['email'] = self.email
        d['password'] = self.password
        return d

