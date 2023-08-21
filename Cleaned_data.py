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



#########################################################################Clean the data to be inserted in the database ###################################################

#Set the colum name for each dataset
colnamesdepartment=['id', 'department']
colnamesemployee=['id', 'name', 'datetime', 'department_id', 'job_id']
colnamesjob=['id','job']

    #Files used
departments = pd.read_csv('departments.csv', names= colnamesdepartment)
Hired_employees = pd.read_csv('hired_employees.csv', names= colnamesemployee)
jobs = pd.read_csv('jobs.csv', names= colnamesjob)

    #Change data type for datetime column
Hired_employees['datetime'] = pd.to_datetime(Hired_employees['datetime'])

    #For datetime columnn, change the format to YYYY-MM-DD
Hired_employees['datetime'] = Hired_employees['datetime'].dt.strftime('%Y-%m-%d')


    #set nan values for column for hired_employees table
Hired_employees['department_id'] = Hired_employees['department_id'].fillna(0)
Hired_employees['job_id'] = Hired_employees['job_id'].fillna(0)
Hired_employees['datetime'] = Hired_employees['datetime'].fillna('0000-00-00')
Hired_employees['name'] = Hired_employees['name'].fillna('N/A')


    #For department_id column, change the data type to int
Hired_employees['department_id'] = Hired_employees['department_id'].astype(int)

    #For job_id column, change the data type to int
Hired_employees['job_id'] = Hired_employees['job_id'].astype(int)

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
departments1.to_csv('clean_departments.csv', index=False, header=False)
Hired_employees1.to_csv('clean_employees.csv', index=False, header=False)
jobs1.to_csv('clean_jobs.csv', index=False, header=False)


print(Hired_employees.dtypes)