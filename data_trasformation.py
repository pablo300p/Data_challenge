import pandas as pd

#Set the colum name for each dataset
colnamesdepartment=['id', 'department']
colnamesemployee=['id', 'name', 'datetime', 'department_id', 'job_id']
colnamesjob=['id','job']
#Files used
departments = pd.read_csv('departments.csv', names= colnamesdepartment)
Hired_employees = pd.read_csv('hired_employees.csv', names= colnamesemployee)
jobs = pd.read_csv('jobs.csv', names= colnamesjob)

#Check Shape
departments.shape
Hired_employees.shape
jobs.shape

#Drop duplicates
departments1 = departments.drop_duplicates()
Hired_employees1 = Hired_employees.drop_duplicates()
jobs1 = jobs.drop_duplicates()

#Check data types
departments1.dtypes
Hired_employees1.dtypes
jobs1.dtypes

#Check null values
departments1.isnull().values.any()
Hired_employees1.isnull().values.any()
jobs1.isnull().values.any()

#Reset index to match the ID
departments1.reset_index(drop=True)
departments1['id'] = departments1.index

Hired_employees1.reset_index(drop=True)
Hired_employees1['id'] = Hired_employees1.index

jobs1.reset_index(drop=True)
jobs1['id'] = jobs1.index
#Save_files

