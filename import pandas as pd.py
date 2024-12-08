import pandas as pd

file_path = 'EmployeeData.xlsx'
data = pd.read_excel(file_path)

sales_department = data[data['Department'] == 'Sales']
sales_count = sales_department.shape[0]
print(f"Darbinieku skaits Sales nodaļā: {sales_count}")

engineering_department = data[data['Department'] == 'Engineering']
min_age = engineering_department['Age'].min() 
print(f"Minimālais vecums darbiniekam, kas strādā Engineering nodaļā: {min_age}")

file_path = 'EmployeeData.xlsx'

data = pd.read_excel(file_path)

it_department = data[data['Department'] == 'IT']

average_age = it_department['Age'].mean()

rounded_average_age = round(average_age)

print(f"Vidējais vecums darbiniekiem, kas strādā IT nodaļā: {rounded_average_age}")


file_path = 'EmployeeData.xlsx'

data = pd.read_excel(file_path)

filtered_data = data[(data['Annual Salary'] > 0) & (data['Annual Salary'] < 100000)]

employee_count = filtered_data.shape[0]

print(f"Darbinieku skaits, kuru alga ir diapazonā 0 < alga < 100000: {employee_count}")

file_path = 'EmployeeData.xlsx'

data = pd.read_excel(file_path)

min_salary_employee = data.loc[data['Annual Salary'].idxmin()]

min_salary_age = min_salary_employee['Age']

print(f"Darbinieka, kam ir zemākā alga, vecums ir: {min_salary_age}")
