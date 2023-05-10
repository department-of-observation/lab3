import employee_info
def test_get_employees_by_age_range():
 result = []
 result=employee_info.get_employees_by_age_range(20,26)
 test = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000},{'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
 assert (result == test)

def test_calculate_average_salary():
    result = 0
    result = employee_info.calculate_average_salary()
    test = 60166.666666666664
    assert (result == test)
def test_get_employees_by_dept():
    result = []
    result= employee_info.get_employees_by_dept('Sales')
    test=[{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},{ 'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    assert (result == test)