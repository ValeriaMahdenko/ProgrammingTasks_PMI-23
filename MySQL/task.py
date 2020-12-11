from flask import Flask, render_template, request, redirect, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, asc, func
import os
import json
import pymysql
from Department import Department


app = Flask(__name__)

DB_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(user='root', password='12345678', host="127.0.0.1",
                                                                       port="3306", db="departments")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DepartmentTable(Department, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(100), unique=False)
    _director_name = db.Column(db.String(20), unique=False)
    _phone_number = db.Column(db.String(20), unique=False)
    _monthly_budget = db.Column(db.Float(), unique=False)
    _yearly_budget = db.Column(db.Float(), unique=False)
    _website_url = db.Column(db.String(100), unique=False)

    def __init__(self, title, director_name, phone_number, monthly_budget, yearly_budget, website_url):
        super().__init__(title, director_name, phone_number, monthly_budget, yearly_budget, website_url)

    def to_json(self):
        d = {}
        d['id'] = self.id
        d['title'] = self.title
        d['director_name'] = self.director_name
        d['phone_number'] = self.phone_number
        d['monthly_budget'] = self.monthly_budget
        d['yearly_budget'] = self.yearly_budget
        d['website_url'] = self.website_url
        return d


@app.route('/')
def database():
    return "hello"


@app.route('/departments', methods=['POST'])
def add_date():
        try:
            userDetails = request.json
            element = DepartmentTable(title=userDetails['title'], director_name=userDetails['director_name'],
                                     phone_number=userDetails['phone_number'], monthly_budget=userDetails['monthly_budget'],
                                     yearly_budget=userDetails['yearly_budget'], website_url=userDetails['website_url'])
            db.session.add(element)
            db.session.commit()
        except ValueError as a:
            return jsonify({'status': '400', 'error': str(a)})
        return jsonify({'status': '200', 'message': 'Data is added on MySQL!',
                                'department': element.to_json()})


@app.route('/departments', methods=['GET'])
def all():
    sort_by = request.args.get('sort_by')
    sort_type = request.args.get('sort_type')
    s = request.args.get('s')
    results = DepartmentTable.query.all()
    all = ''
    json_results = []
    counter = 0
    if s or sort_by:
        for result in results:
            if s:
                all += str(result.id) + result.director_name + result.phone_number + str(result.monthly_budget) + \
                       str(result.yearly_budget) + result.website_url
                if s in str(all):
                    counter +=1
                    json_results.append(result.to_json())
                all = ''
            elif counter == 0:
                return jsonify({'status': '404', 'message': 'Department with key \"' + str(s) + '\" is not found'})
            else:
                return jsonify({'status': '400', 'message': 'wrong search attribute'})
        if sort_by:
            if sort_type == "desc":
                json_results = sorted(json_results, key=lambda el: el[sort_by], reverse=True)
            else:
                json_results = sorted(json_results, key=lambda el: el[sort_by])
        else:
            return jsonify({'status': 'No attribute ' + sort_by + " in databases!"})

        return jsonify(json_results)
    else:
        json_results = []
        for result in results:
            d = result.to_json()
            json_results.append(d)
        return jsonify(json_results)


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
