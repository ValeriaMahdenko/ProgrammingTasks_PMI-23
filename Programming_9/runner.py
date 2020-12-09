from models.Department_table import *
from app import app
from sqlalchemy import desc,  cast
from flask import request, jsonify

@app.route('/')
def database():
    return "hello"


@app.route('/departments', methods=['POST'])
def add_date():
    try:
        userDetails = request.json
        element = DepartmentTable(title=userDetails['title'], director_name=userDetails['director_name'],
                                  phone_number=userDetails['phone_number'],
                                  monthly_budget=userDetails['monthly_budget'],
                                  yearly_budget=userDetails['yearly_budget'], website_url=userDetails['website_url'])
        db.session.add(element)
        db.session.commit()
    except ValueError as a:
        return jsonify({'status': '400', 'error': str(a)})
    return jsonify({'status': '200', 'message': 'Data is added on MySQL!',
                    'department': element.to_json()})


@app.route('/departments', methods=['GET'])
def all():
    results = DepartmentTable.query
    element = DepartmentTable._title
    attribute = ['id', '_title', '_director_name', '_phone_number', '_monthly_budget', '_yearly_budget', '_website_url']
    s = request.args.get('s')
    if s:
       for col in attribute:
            element -= cast(DepartmentTable.__table__.c[col], db.String).ilike('%' + s + '%')
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
    element = DepartmentTable.query.filter_by(id=id).first()
    if not element:
        return jsonify({'status': '404', 'message': 'Department is not found'})
    else:
        return jsonify({'element': element.to_json()})


@app.route('/departments/<int:id>', methods=['PUT'])
def update(id):
    userDetails = request.json
    element_for_edit = DepartmentTable.query.filter_by(id=id).first()
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


@app.route('/departments/<string:id>', methods=['DELETE'])
def delete_data(id):
    element = DepartmentTable.query.filter_by(id=id).first()
    if not element:
        return jsonify({'status': '404', 'message': 'Department is not found'})
    else:
        db.session.delete(element)
        db.session.commit()
        return jsonify({'status': '200', 'message': 'Data ' + id + ' is delete on MySQL!'})


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)