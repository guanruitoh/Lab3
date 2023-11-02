employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    result = []
    age_lower_limit=18
    age_upper_limit=50
    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
    for item in result:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(
            item["salary"])).expandtabs(15))
def test_calculate_average_salary():
    total = 0
    average = 0

    #add your implementation to calculate here
    for values in employee_data:
        total += values["salary"]
    average = total/len(employee_data)

    print(total)
    print(average)




def test_get_employees_by_dept():
    result = []
    department = "Engineering"

    # Add your implementation from here
    for employee in employee_data:
        if employee["department"].lower() == department.lower():
            result.append(employee)

    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
    for item in result:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(
            item["salary"])).expandtabs(15))
