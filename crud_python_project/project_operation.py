from CRUD_Operation import *
from inputHelper import *
import re
email_pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
def create_p():
    title = askforstring("Enter the title of your project: ")
    details = askforstring("Enter the details of your project: ")
    target = askforInt("Enter the total target for your project (in EGP): ")
    email = input("Enter your email ")
    if not (re.search(email_pattern, email)):
      print('Invalid email address')
      variable_name = True
      while variable_name:
         email = input("Enter your email: ")
         if (re.search(email_pattern, email)):
          variable_name = False
    start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not ValidDate(start_time):
        start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not ValidDate(end_time):
        end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    id = generate_id()
    with open("projects.txt", "a") as file:
        file.write("{} {} {} {} {} {} {}\n".format(id , title, details, target, start_time, end_time, email ))
    print("Project created successfully.")


def veiw_all_project():
    projects = get_all_projects()
    if projects:
        for project in projects:
            print(project)
    else:
        print(' Error happened during veiw_all_project')

def edit_project():
    project_id = askforInt("enter id of the project to edit: ") # int
    email=input("enter your email ")
    if not (re.search(email_pattern, email)):
      print('Invalid email address')
      variable_name = True
      while variable_name:
         email = input("Enter your email: ")
         if (re.search(email_pattern, email)):
          variable_name = False
    found = find_project_by_id(project_id)
    test = str(found).split() 
    if found :
        print( "found" )
        print(test)
        if test[6]== str(email):
            delete_project_from_file(found)
            create_p()
            print("Project edited successfully.")
        else:
            print("not in your own can't edit it ")
            

def delete_project():
    project_id = askforInt("Please enter the id of the project you want to delete: ") # int
    email=input("enter your email ")
    found = find_project_by_id(project_id)
    test = str(found).split() 
    if found :
        print( "found" )
        if test[6]== str(email):
            removed=delete_project_from_file(found)
            if removed:
                print('project deleted')
            else:
                print(" problem happened while deleting ")
        else:
            print("not in your own can't  delete it ")
            return
    else:
        print("project not found, please try again with valid id ")

def search_project_using_start_time():
    start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not ValidDate(start_time):
        start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    find_project_by_start_time(start_time)
    