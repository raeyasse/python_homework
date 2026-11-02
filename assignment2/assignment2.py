import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    dic = {}
    rows_list = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" not in dic:
                    dic["fields"] = row
                else:
                    rows_list.append(row)
            dic["rows"] = rows_list
            return dic
        

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()
#print(employees)

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("first_name")
#print(employee_id_column)

def first_name(row_number): 
    index = column_index("first_name")
    row = employees["rows"][row_number]
    return row[index]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

employee_id_column = column_index("employee_id")
#print(employee_find(1))


def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sort_by_last_name()
#print(employees)

def employee_dict(row):
    dic = {}
    for field in employees["fields"]:
        if field != "employee_id":
            index= column_index(field)
            dic[field] = row[index]
    return dic


def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)
    return result

#print(all_employees_dict())

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Broken Enamel")
#print(custom_module.secret)

def read_minutes():
    minutes1 = {}
    minutes2 = {}

    rows1 = []
    rows2 = []

    try:
        with open("../csv/minutes1.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" not in minutes1:
                    minutes1["fields"] = row
                else:
                    rows1.append(tuple(row))

        minutes1["rows"] = rows1

        with open("../csv/minutes2.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" not in minutes2:
                    minutes2["fields"] = row
                else:
                    rows2.append(tuple(row))

        minutes2["rows"] = rows2

        return minutes1, minutes2
    except Exception as e:
        print("An exception occurred.", type(e).__name__)
        traceback.print_exc()
        raise SystemExit(1)
    
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)
minutes_set = create_minutes_set()

def create_minutes_list():
    rows = list(minutes_set)

    return list(map(
    lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y")),
    rows
))

minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_rows = list(map(lambda row: (row[0], row[1].strftime("%B %d, %Y")),
    minutes_list))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"]) 
        writer.writerows(converted_rows)    
    return converted_rows

write_sorted_list()

