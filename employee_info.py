# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
# def testing_employee():
#     print(employee_data.pop()) remove
#     #print(employee_data.count(smth)) 

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result, no .key is used
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)#result.append(item) item from variable

    return result

def calculate_average_salary():
    total = 0
    average = 0
    length=len(employee_data)
    for item in employee_data:
        total+=item["salary"]# specific key ko + chin yin do lo yay
        
    average=total/length
    return_avg=round(average,2)#Round for int/float

    #add your implementation to calculate here


    return return_avg

def get_employees_by_dept(department):
    result = []
    print(("Name" + "\t" +"Department" +"\t").expandtabs(15))# if item["department"]==department****
    for item in employee_data:
        if item["department"]== department:
            result.append(item)

            print((item["name"]+"\t"+str(item["department"])+"\t").expandtabs(15))
            
    return result

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def checking_for_myself():
    list=[]
    for key in employee_data:
        print(key["salary"])#accessing the value of that "salary" key
        print(key.keys)
        list.append(key)

def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")


    print("Q - Quit")
    #testing_employee()
    option = input("Enter selection =>")
    
    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Uper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)


    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)

    elif option == 'Q':
        quit()

def main():

    # while (True):
    #     display_main_menu()
    # employee_info=input("Enter salary to start:")
    checking_for_myself()


if __name__ == "__main__":
    main()