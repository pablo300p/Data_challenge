import pandas as pd

def data_review():
    #Get data:
    departments = pd.read_csv('departments.csv')
    Hired_employees = pd.read_csv('hired_employees.csv')
    jobs = pd.read_csv('jobs.csv')

    #Check Shape
    departments.shape
    Hired_employees.shape
    jobs.shape

    #Check data types
    departments.dtypes
    Hired_employees.dtypes
    jobs.dtypes

    #Check null values
    departments.isnull().values.any()
    Hired_employees.isnull().values.any()
    jobs.isnull().values.any()



def data_cleaning():
    #Set the colum name for each dataset
    colnamesdepartment=['id', 'department']
    colnamesemployee=['id', 'name', 'datetime', 'department_id', 'job_id']
    colnamesjob=['id','job']

    #Files used
    departments = pd.read_csv('departments.csv', names= colnamesdepartment)
    Hired_employees = pd.read_csv('hired_employees.csv', names= colnamesemployee)
    jobs = pd.read_csv('jobs.csv', names= colnamesjob)

    #Drop duplicates
    departments1 = departments.drop_duplicates()
    Hired_employees1 = Hired_employees.drop_duplicates()
    jobs1 = jobs.drop_duplicates()

    #Reset index to match the ID
    departments1.reset_index(drop=True)
    departments1['id'] = departments1.index

    Hired_employees1.reset_index(drop=True)
    Hired_employees1['id'] = Hired_employees1.index

    jobs1.reset_index(drop=True)
    jobs1['id'] = jobs1.index

    #Transform into dictionary to send 
    Department = departments1.to_dict(orient='records')
    Employee = Hired_employees1.to_dict(orient='records')
    Job = jobs1.to_dict(orient='records')

    return(Department, Employee, Job)
