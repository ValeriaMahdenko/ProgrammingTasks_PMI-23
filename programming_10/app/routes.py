from app.app import db, app, login_manager
from flask import request, jsonify, session
from sqlalchemy import desc,  cast
from flask_login import login_user, logout_user, current_user, login_required
from models.Table_Department import DepartmentTBL
from models.User_Table import TableUser, check_password_hash
from models.Order_Table import OrderTable
from datetime import date



@login_manager.user_loader
def load_user(user_id):
    return TableUser.query.get(int(user_id))


@app.route('/', methods=['GET'])
def index():
    if 'admin' or 'user' in session:
        return current_user.first_name + " " + current_user.second_name + " - is active!"
    else:
        return "No active user!"


@app.route('/departments/login', methods=['POST'])
def login():
    email = request.json['email']
    user = TableUser.query.filter_by(_email=email).first()
    if user:
        if check_password_hash(user.password, request.json['password']):
            login_user(user)
            if user.role == 'Admin':
                session['admin'] = True
            else:
                session['user'] = True
            return 'You are successfully logged in!'
        else:
            return "Password is wrong"
    else:
        return "Email is wrong!"


@app.route('/departments/logout',  methods=['POST'])
@login_required
def logout():
    if 'admin' or 'user' in session:
        print("yes")
        logout_user()
        session.pop('admin', None)
        session.pop('user', None)
        return "You are successfully logged out"
    else:
        return "You are already logged out"


@app.route('/departments/registration', methods=['POST'])
def add_user():
    try:
        userDetails = request.json
        element = TableUser(first_name=userDetails['first_name'], second_name=userDetails['second_name'],
                            email=userDetails['email'], password=request.json["password"], role=userDetails['role'] )
        db.session.add(element)
        db.session.commit()
    except ValueError as a:
        return jsonify({'status': '400', 'error': str(a)})
    return jsonify({'status': '200', 'message': 'You are successfully registered, please log in!',
                    'user_id': element.id})


@app.route('/departments', methods=['POST'])
def add_date():
    if 'admin' in session:
        try:
            userDetails = request.json
            element = DepartmentTBL(user_id=current_user.id, title=userDetails['title'], amount=userDetails['amount'],
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
        return "You must log in first / You are not an admin"

@app.route('/orders', methods=['POST'])
def new_date():
    if 'user' in session:
        try:
            userDetails = request.json
            amount = userDetails['amount']
            id = userDetails['product_id']
            new = OrderTable(user_id=current_user.id, product_id=id, amount=amount,
                             date=date.today())
            element = DepartmentTBL.query.filter_by(id=id).first()
            if element:
                if int(amount) <= element.amount:
                    element.amount -= int(amount)
                    db.session.add(new)
                    db.session.commit()
                else:
                    return jsonify({'eror': "Quantity exceeded",
                                    "max": element.amount})
            else:
                return jsonify({'status': '404', 'message': 'Department is not found'})

        except ValueError as a:
            return jsonify({'status': '400', 'error': str(a)})
        return jsonify({'status': '200', 'message': 'Order accepted'})
    else:
        return "You must log in first / You are not user"


@app.route('/orders', methods=['GET'])
def all_orders():
    if "admin" in session:
        results = OrderTable.query
    else:
        results = OrderTable.query.filter_by(_user_id=current_user.id)
    return jsonify({'Orders': [i.to_json() for i in results],
                        'Count': results.count()})


@app.route('/orders/<string:id>', methods=['GET'])
def get_orders(id):
    if 'user' in session:
        results = OrderTable.query.filter_by(_user_id=current_user.id)
        element = results.filter_by(id=id).first()
        if not element:
            return jsonify({'status': '404', 'message': 'Order is not found'})
        else:
            return jsonify({'order': element.to_json()})
    else:
        return "You must log in first / You are not user"

@app.route('/departments', methods=['GET'])
def all():
    results = DepartmentTBL.query
    element = DepartmentTBL._title
    attribute = ['id', '_title', '_director_name', '_phone_number', '_monthly_budget', '_yearly_budget', '_website_url']
    s = request.args.get('s')
    if s:
        for col in attribute:
            element |= cast(getattr(DepartmentTBL, col), db.String).ilike('%' + s + '%')
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
    if offset != None and limit != None:
        results = results.offset(offset * limit).limit(limit).all()
        return jsonify({'Elements': [i.to_json() for i in results]})
    else:
        return jsonify({'Elements': [i.to_json() for i in results],
                        'Count': results.count()})


@app.route('/departments/<string:id>', methods=['GET'])
def get_data(id):
    if 'admin' or 'user' in session:
        element = DepartmentTBL.query.filter_by(id=id).first()
        if not element:
            return jsonify({'status': '404', 'message': 'Department is not found'})
        else:
            return jsonify({'element': element.to_json()})
    else:
        return "You must log in first"


@app.route('/departments/<int:id>', methods=['PUT'])
def update(id):
    if 'admin' in session:
        userDetails = request.json
        element_for_edit = DepartmentTBL.query.filter_by(id=id).first()
        if element_for_edit:
            try:
                element_for_edit.title = userDetails['title']
                element_for_edit.director_name = userDetails['director_name']
                element_for_edit.phone_number = userDetails['phone_number']
                element_for_edit.monthly_budget = userDetails['monthly_budget']
                element_for_edit.yearly_budget = userDetails['yearly_budget']
                element_for_edit.website_url = userDetails['website_url']
                element_for_edit.amount = userDetails['amount']
                db.session.commit()
                return jsonify({'status': '200', 'message': 'Data ' + str(id) + ' is updated on MySQL!',
                                'department': element_for_edit.to_json()})
            except ValueError as a:
                return jsonify({'status': '400', 'error': a})
        else:
            return jsonify({'status': '404', 'message': 'Department is not found'})
    else:
        return "You must log in first / You are not an admin"


@app.route('/departments/<string:id>', methods=['DELETE'])
def delete_data(id):
    if 'admin' in session:
        element = DepartmentTBL.query.filter_by(id=id).first()
        if not element:
            return jsonify({'status': '404', 'message': 'Department is not found'})
        else:
            db.session.delete(element)
            db.session.commit()
            return jsonify({'status': '200', 'message': 'Data ' + id + ' is delete on MySQL!'})
    else:
        return "You must log in first / You are not an admin"
