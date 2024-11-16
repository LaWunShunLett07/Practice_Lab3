import employee_info as info
def test_get_employees_by_age_range():

    test_case=info.get_employees_by_age_range(21,26)
    expected_value=[ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert test_case==expected_value

def test_calculate_average_salary():
    test_case=info.calculate_average_salary()
    expected_value=60166.67
    assert test_case==expected_value

def test_get_employees_by_dept():
    test_case=info.get_employees_by_dept("Engineering")
    expected_result=[ {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},]
    assert test_case==expected_result