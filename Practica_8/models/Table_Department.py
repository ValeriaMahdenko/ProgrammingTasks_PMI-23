from app.app import db
from models.Department import Department

class TableDepartment(Department, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _user_id = db.Column(db.Integer, unique=False)
    _title = db.Column(db.String(100), unique=False)
    _director_name = db.Column(db.String(20), unique=False)
    _phone_number = db.Column(db.String(20), unique=False)
    _monthly_budget = db.Column(db.Float(), unique=False)
    _yearly_budget = db.Column(db.Float(), unique=False)
    _website_url = db.Column(db.String(100), unique=False)

    def __init__(self, user_id, title, director_name, phone_number, monthly_budget, yearly_budget, website_url):
        super().__init__(user_id, title, director_name, phone_number, monthly_budget, yearly_budget, website_url)

    def to_json(self):
        d = {}
        d['id'] = self.id
        d['user_id'] = self.user_id
        d['title'] = self.title
        d['director_name'] = self.director_name
        d['phone_number'] = self.phone_number
        d['monthly_budget'] = self.monthly_budget
        d['yearly_budget'] = self.yearly_budget
        d['website_url'] = self.website_url
        return d

