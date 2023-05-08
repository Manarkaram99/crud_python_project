import re
from  project_operation  import *
egypt_phone_pattern = "^01[0-9]{9}$"
email_pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
name_pattern = r'^[a-zA-Z]+$'
def register():
   first_name = input("Enter your first name: ")
   if not (re.match(name_pattern, first_name)):
    print('Invalid first_name')
    variable_name = True
    while variable_name:
        first_name = input("Enter your first name: ")
        if (re.match(name_pattern, first_name)):
            variable_name = False
   last_name = input("Enter your last name: ")
   if not (re.match(name_pattern, last_name)):
        print('Invalid last_name')
        variable_name = True
        while variable_name:
           last_name = input("Enter your last name: ")
           if (re.match(name_pattern, last_name)):
             variable_name = False
   email = input("Enter your email: ")
   # check if email match
   if not (re.search(email_pattern, email)):
      print('Invalid email address')
      variable_name = True
      while variable_name:
         email = input("Enter your email: ")
         if (re.search(email_pattern, email)):
          variable_name = False
   password = input("Enter your password: ")
   confirm_password = input("Confirm your password: ")
    # Check if passwords match
   if password != confirm_password:
      print("Passwords do not match. Please try again.")
      variable_name = True
      while variable_name:
         confirm_password = input("Confirm your password: ")
         if password == confirm_password:
            variable_name = False
   mobile = input("Enter your mobile phone number: ")
    # Validate phone number using regex pattern
   if not re.match(egypt_phone_pattern, mobile):
      print("Invalid phone number. Please enter a valid Egyptian phone number.")
      variable_name = True
      while variable_name:
         mobile = input("Enter your mobile phone number: ")
         if re.match(egypt_phone_pattern, mobile):
               variable_name = False
   with open("users.txt", "a") as F:
     F.write(f"{first_name} { last_name } {email} {password} {mobile} \n")
   print("Registration successful.")

##########
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    with open("users.txt", "r") as file:
        for line in file:
            user_info = line.strip().split()
            if user_info[2] == email and user_info[3] == password:
                print("Login successful.")
                print("Welcome, {} {}!".format(user_info[0], user_info[1]))
                while True:
                 print("                    Hello                    ")
                 print("                Enter no 1 to creat project       ")
                 print("                Enter no 2 to veiew  project         ")
                 print("                Enter no 3 to edit project           ")
                 print("                Enter no 4 to delete project           ")
                 print("                Enter no 5 to find_project_by_start_time           ")
                 print("                Enter no 6 to exit           ")
                 choice = input("       please enter your choice ")
                 if choice=='1':
                  create_p()
                 elif choice=='2':
                  veiw_all_project()
                 elif choice=='3':
                  edit_project()
                 elif choice=='4':
                  delete_project()
                 elif choice=='5':
                  search_project_using_start_time()
                 elif choice=='6':
                  print("             ====> Good Bye <====   ")
                  exit()
                  #return
    print("Invalid email or password. Please try again.")

