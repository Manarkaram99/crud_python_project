import time
import datetime
def find_project_by_id(project_id):
    projects = get_all_projects()
    for project in projects:
        print(project)
        project_details = project.strip('\n').split(" ")  
        if project_details[0]==str(project_id):
            return project
    else:
        return False
    
def save_projects_to_file(listofprojects):
    try:
        fileobj =open("projects.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(listofprojects)
        fileobj.close()
        return True


    
def delete_project_from_file(project):
    projects= get_all_projects()
    projects.remove(project)  
    removed = save_projects_to_file(projects)
    return removed


# Function to validate date format
def ValidDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d_%H:%M:%S')
        return True
    except ValueError:
        return False

def get_all_projects():
    try:
        fileobj =open("projects.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        users = fileobj.readlines()
        return users

#######
def find_project_by_start_time(start_time):
    projects = get_all_projects()
    for project in projects:
       # print(project)
        project_details = project.strip('\n').split(" ")  
        if project_details[4]==str(start_time):
            print(project)
    else:
        return False
