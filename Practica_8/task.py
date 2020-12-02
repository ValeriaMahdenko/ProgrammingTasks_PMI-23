from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc,  cast
from flask_login import login_user, logout_user, current_user, login_required
import pymysql
from Department import Department
from UserTable import *
from flask_login import LoginManager


app = Flask(__name__)

DB_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(user='root', password='12345678', host="127.0.0.1",
                                                                       port="3306", db="department")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)


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


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'


@login_manager.user_loader
def load_user(user_id):
    return UserTable.query.get(int(user_id))


@app.route('/', methods=['POST'])
@login_required
def index():
    if 'loggedin' in session:
        return current_user.first_name + " " + current_user.second_name + " - is active!"


@app.route('/departments/login', methods=['POST'])
def login():
    email = request.json['email']
    user = UserTable.query.filter_by(_email=email).first()
    if user:
        if check_password_hash(user.password, request.json['password']):
            login_user(user)
            session['loggedin'] = True
            return 'You are successfully logged in!'
        else:
            return "Password is wrong"
    else:
        return "Email is wrong!"


@app.route('/departments/logout',  methods=['POST'])
@login_required
def logout():
    if 'loggedin' in session:
        logout_user()
        session.pop('loggedin', None)
        return "You are successfully logged out"
    else:
        return "You are already logged out"


@app.route('/departments/registration', methods=['POST'])
def add_user():
    try:
        userDetails = request.json
        element = UserTable(first_name=userDetails['first_name'], second_name=userDetails['second_name'],
                            email=userDetails['email'], password=request.json["password"] )
        db.session.add(element)
        db.session.commit()
    except ValueError as a:
        return jsonify({'status': '400', 'error': str(a)})
    return jsonify({'status': '200', 'message': 'You are successfully registered, please log in!',
                    'user_id': element.id})


@app.route('/departments', methods=['POST'])
def add_date():
    if 'loggedin' in session:
        try:
            userDetails = request.json
            element = TableDepartment(user_id=current_user.id, title=userDetails['title'],
                                      director_name=userDetails['director_name'], phone_number=userDetails['phone_number'],
                                      monthly_budget=userDetails['monthly_budget'], yearly_budget=userDetails['yearly_budget'],
                                      website_url=userDetails['website_url'])
            db.session.add(element)
            db.session.commit()
        except ValueError as a:
            return jsonify({'status': '400', 'error': str(a)})
        return jsonify({'status': '200', 'message': 'Data is added on MySQL!',
                        'department': element.to_json()})
    else:
        return "You must log in first!"


@app.route('/departments', methods=['GET'])
def all():
    results = TableDepartment.query
    element = TableDepartment._title
    attribute = ['id', '_title', '_director_name', '_phone_number', '_monthly_budget', '_yearly_budget', '_website_url']
    s = request.args.get('s')
    if s:
       for col in attribute:
            element -= cast(TableDepartment.__table__.c[col], db.String).ilike(f'{s}%')
       results = results.filter(element)

    sort_by = request.args.get('sort_by')
    sort_type = request.args.get('sort_type')
    if sort_by:
        all = ''
        for i in attribute:
            all+=i
        if sort_by not in all:
            return jsonify({'status': '505', 'error': 'No attribute ' + sort_by + " in databases!"})
        elif sort_type == "desc":
                results = results.order_by(desc(sort_by))
        else:
                results = results.order_by(sort_by)
    offset = request.args.get('offset', type=int)
    limit = request.args.get('limit', type=int)
    if 'loggedin' in session:
        results = results.filter_by(_user_id=current_user.id)

    if offset != None and limit != None:
        results = results.offset(offset * limit).limit(limit).all()
        return jsonify({'Elements': [i.to_json() for i in results]})
    else:
        return jsonify({'Elements': [i.to_json() for i in results],
                        'Count': results.count()})


@app.route('/departments/<string:id>', methods=['GET'])
def get_data(id):
    if 'loggedin' in session:
        results = TableDepartment.query.filter_by(_user_id=current_user.id)
        element = results.filter_by(id=id).first()
        if not element:
            return jsonify({'status': '404', 'message': 'Department is not found'})
        else:
            return jsonify({'element': element.to_json()})
    else:
        return "You must log in first!"


@app.route('/departments/<int:id>', methods=['PUT'])
def update(id):
    if 'loggedin' in session:
        userDetails = request.json
        results = TableDepartment.query.filter_by(_user_id=current_user.id)
        element_for_edit = results.filter_by(id=id).first()
        if element_for_edit:
            try:
                element_for_edit.title = userDetails['title']
                element_for_edit.director_name = userDetails['director_name']
                element_for_edit.phone_number = userDetails['phone_number']
                element_for_edit.monthly_budget = userDetails['monthly_budget']
                element_for_edit.yearly_budget = userDetails['yearly_budget']
                element_for_edit.website_url = userDetails['website_url']
                db.session.commit()
                return jsonify({'status': '200', 'message': 'Data ' + str(id) + ' is updated on MySQL!',
                                'department': element_for_edit.to_json()})
            except ValueError as a:
                return jsonify({'status': '400', 'error': a})
        else:
            return jsonify({'status': '404', 'message': 'Department is not found'})
    else:
        return "You must log in first!"


@app.route('/departments/<string:id>', methods=['DELETE'])
def delete_data(id):
    if 'loggedin' in session:
        results = TableDepartment.query.filter_by(_user_id=current_user.id)
        element = results.filter_by(id=id).first()
        if not element:
            return jsonify({'status': '404', 'message': 'Department is not found'})
        else:
            db.session.delete(element)
            db.session.commit()
            return jsonify({'status': '200', 'message': 'Data ' + id + ' is delete on MySQL!'})
    else:
        return "You must log in first!"


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
