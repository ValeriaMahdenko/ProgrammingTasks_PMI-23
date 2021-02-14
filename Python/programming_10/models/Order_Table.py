from flask_login import UserMixin
from app.app import db
from validation import Validation


class OrderTable(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _user_id = db.Column(db.Integer, unique=False)
    _product_id = db.Column(db.Integer, unique=False)
    _amount = db.Column(db.Integer, unique=False)
    _date = db.Column(db.String(20), unique=False)

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    @Validation.decorator_number
    def user_id(self, val):
        self._user_id = val

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    @Validation.decorator_number
    def product_id(self, val):
        self._product_id = val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    @Validation.decorator_number
    def amount(self, val):
        self._amount = val

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        self._date = val

    def to_json(self):
        d = {}
        d['id'] = self.id
        d['amount'] = self.amount
        d['user_id'] = self.user_id
        d['product_id'] = self.product_id
        d['date'] = self.date
        return d

