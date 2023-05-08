import time
import re
from handel import delete_project_from_file, find_project_by_id, get_all_project_from_file, save_project_to_the_file
name_pattern = r'^[a-zA-Z]+$'
money_pattern = r"\d{1,3}(,\d{3})*\.\d{2}"
def generate_id():
    return round(time.time())
def create():
    title = input("Enter Title : ")
    if not (re.match(name_pattern, title)):
     print('Invalid Title')
     variable_name = True
     while variable_name:
        title = input("Enter Title : ")
        if (re.match(name_pattern, title)):
            variable_name = False
    details = input("Enter Details : ")
    if not (re.match(name_pattern, details)):
     print('Invalid details')
     variable_name = True
     while variable_name:
        details = input("Enter Details : ")
        if (re.match(name_pattern, details)):
            variable_name = False
    total_target_money = input("Enter Total target : ")
    match = re.search(money_pattern, total_target_money)
    if not match:
       print('Invalid total_target_money')
       variable_name = True
       while variable_name:
        total_target_money = input("Enter Total target : ")
        if match:
            variable_name = False
    project_id = generate_id()
       

    start_time = input("Start Date (mm/dd/yyyy) : ")
    end_time = input("End Date (mm/dd/yyyy) : ")

    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')
    except ValueError:
        print('Invalid date format, please use mm/dd/yyyy')
        return None
    project_data = f"{project_id}:{title}:{details}:{total_target_money}\n"
    added = save_project_to_the_file(project_data )
    if added:
        print("---book added successfully---")
    else:
        print("=== problem happended ---> try again please ----")
create()

def display_all_projects():
    projects = get_all_project_from_file()
    if projects:
        print(projects)
        for project in projects:
            print(project)
    else:
        print('---- Error happened please try again ----')

def delete_project():
    project_id = input("Please enter the id of the book you want to delete: ") # int
    ## search if book exists in the books
    found = find_project_by_id(project_id)
    if found :
        print("--- book found ")
        removed=delete_project_from_file(found[1])
        if removed:
            print('--- book deleted successfully ---')
        else:
            print("--- problem happened while deleting the book ---")
    else:
        print("Book not found, please try again with valid id ")


