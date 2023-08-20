from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

class Employee(db.Model):
  __tablename__ = 'Hired_Employees'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  datetime = db.Column(db.String(120), unique=True, nullable=False)
  department_id = db.Column(db.Integer, nullable=False)
  job_id = db.Column(db.Integer, nullable=False)

  def __init__(self, name, datetime, department_id, job_id):
    self.name = name
    self.datetime = datetime
    self.department_id = department_id
    self.job_id = job_id


db.create_all()

class EmployeeResource(Resource):
#Get one item in the database
  @app.route('/employee/<id>', methods=['GET'])
  def get_item(id):
    item = Employee.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)

# Get all items in the database
  @app.route('/employees', methods=['GET'])
  def get_items():
    items = []
    for item in db.session.query(Employee).all():
      del item.__dict__['_sa_instance_state']
      items.append(item.__dict__)
    return jsonify(items)

#Create a new item in the database
  @app.route('/employees', methods=['POST'])
  def create_employee():
    try:
      body = request.get_json()
      new_item = Employee(name=body['name'], datetime=body['datetime'], department_id=body['department_id'], job_id=body['job_id'])
      db.session.add(new_item)
      db.session.commit()
      return "item created"
    except Exception:
      return "Item could not be created" 
        
#To update an existing enployee in the database
  @app.route('/Employee/<id>', methods=['PUT'])
  def update_item(id):
    body = request.get_json()
    db.session.query(Employee).filter_by(id=id).update(
      dict(name=body['name'], datetime=body['datetime'], department_id=body['department_id'], job_id=body['job_id']))
    db.session.commit()
    return "item updated"

#To delete an existing employee in the database
  @app.route('/employee/<id>', methods=['DELETE'])
  def delete_item(id):
    db.session.query(Employee).filter_by(id=id).delete()
    db.session.commit()
    return "item deleted"


if __name__ == "__main__":
    app.run(debug=True)