from flask import Flask, request
import psycopg2 
import os
import pandas as pd


CREATE_HIRED_EMPLOYEES_TABLE = """CREATE TABLE IF NOT EXISTS Hired_Employees (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, datetime VARCHAR(255) NOT NULL, department_id INTEGER NOT NULL, job_id INTEGER NOT NULL);"""

CREATE_DEPARTMENTS_TABLE = """ CREATE TABLE IF NOT EXISTS Departments (id SERIAL PRIMARY KEY, department VARCHAR(255) NOT NULL);"""

CREATE_JOBS_TABLE = """ CREATE TABLE IF NOT EXISTS Jobs (id SERIAL PRIMARY KEY, job VARCHAR(255) NOT NULL);"""


INSERT_EMPLOYEES = """INSERT INTO Hired_Employees (name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s);"""

INSERT_DEPARTMENTS = """INSERT INTO Departments (department) VALUES (%s);"""

INSERT_JOBS = """INSERT INTO Jobs (job) VALUES (%s);"""

#EMPLOYEES_DETAILS = """SELECT department, job, CASE FROM Hired_Employees;"""


app = Flask(__name__)

url = 'postgresql://postgres:postgress@db:5432/test'
connection = psycopg2.connect(url)


@app.route("/api/employee", methods=['POST'])
def create_employee():
    data = request.get_json()
    name = data['name']
    datetime = data['datetime']
    department_id = data['department_id']
    job_id = data['job_id']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_HIRED_EMPLOYEES_TABLE)
            # Execute many accept a list of rows allowing us to insert multiple rows at once
            cursor.executemany(INSERT_EMPLOYEES, [
                (name, datetime, department_id, job_id)
            ])
            name = cursor.fetchone()[0]
    return {'name': name}, 201

@app.route("/api/department", methods=['POST'])
def create_department():
    data = request.get_json()
    department = data['department']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_DEPARTMENTS_TABLE)
            cursor.executemany(INSERT_DEPARTMENTS, [
                (department)
            ])
            name = cursor.fetchone()[0]
    return {'name': name}, 201

@app.route("/api/job", methods=['POST'])
def create_job():
    data = request.get_json()
    job = data['job']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_JOBS_TABLE)
            cursor.executemany(INSERT_JOBS, [
                (job)
            ])
            name = cursor.fetchone()[0]
    return {'name': name}, 201


if __name__ == "__main__":
    app.run(debug=True)
