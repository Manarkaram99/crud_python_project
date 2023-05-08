def save_project_to_the_file(project_data):
    try:
        fileobj =open("projects.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(project_data)
        fileobj.close()
        return True

def get_all_project_from_file():
    try:
        fileobj =open("projects.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        projects = fileobj.readlines()
        return projects


def find_project_by_id(project_id):
    projects = get_all_project_from_file()
    for project in projects:
        # if str(book_id) in book:
        #     return True, book
        print(project)
        project_details = project.strip('\n').split(":")  # list book_details
        if project_details[0]==str(project_id):
            return True , project
    else:
        return False

####
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

####
def delete_project_from_file(project):
    projects= get_all_project_from_file()
    projects.remove(project)  # list
    removed = save_projects_to_file(projects)
    return removed