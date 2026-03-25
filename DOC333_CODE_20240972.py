import re

# Initialize Variable
menu_option = "0"
students_list = []

student_id = ""
nic = ""
first_name = ""
last_name = ""
birth_date = ""
permanent_address = ""
phone_number = ""
tutorial_group = ""
center = ""
save_choice = ""
center_options = {"1": "Colombo", "2": "Galle", "3": "Kurnagala"}
update_details = ""
attendance_data = []

def validate_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date))

def update_student_details ():
                student_id = ""

                while len(student_id) != 9 or (not student_id.isdigit()):
                    student_id = str(input("Student ID : "))
                    if len(student_id) != 9:
                         print("Invalid Student ID ")
                    if not student_id.isdigit():
                         print("Student ID must be all digits")

                # Print View deatails of the student
                found = False  # Flag to check if the student was found
                for student in students_list:
                    if student["student_id"] == student_id:
                        nic = ""
                        first_name = ""
                        last_name = ""
                        birth_date = ""
                        permanent_address = ""
                        phone_number = ""
                        tutorial_group = ""
                        center = ""


                        while len(nic) != 10:
                            nic = str(input("NIC : "))
                            if len(nic) != 10:
                                print("Invalid NIC ")

                        while len(first_name) == 0 or len(first_name) > 10:
                            first_name = str(input("First Name : ")).strip()
                            if len(first_name) < 1:
                                print("First name cannot be empty.")
                            elif len(first_name) > 10:
                                print("First name must be within 10 characters")

                        while len(last_name) == 0 or len(last_name) > 15:
                            last_name = str(input("Last Name : ")).strip()
                            if len(last_name) == 0:
                                print("Last name can not be empty")
                            elif len(last_name) > 15:
                                print("Last name must be within 15 characters")

                        while not validate_date(birth_date):
                            birth_date = (input("Birth Date (YYYY-MM-DD) : ")).strip()
                            if not validate_date(birth_date):
                                print("Please enter correct date")

                        while (
                            len(permanent_address) == 0 or len(permanent_address) > 15
                        ):
                            permanent_address = input("Permanenet Address : ")
                            if len(permanent_address) > 15:
                                print("Permanent address mush be within 15 characters")
                            elif len(permanent_address) == 0:
                                print("permanent Address can not be empty.")
          
                        while len(phone_number) != 10 or (not phone_number.isdigit()):
                              phone_number = str(input("Phone Number : "))
                              if len(phone_number) != 10:
                                   print("Phone number must be 10 digits.")
                              elif not phone_number.isdigit():
                                   print("Phone Number should only have digits")

                    while (tutorial_group) == "":
                              tutorial_group = str(input("Tutorial Group : "))
                              if (tutorial_group) == 0:
                                   print("Tutorial Group can not be empty.Please enter a valid value.")


                    center_option = ""
                    while (
                            center_option != "1"
                            or center_option != "2"
                            or center_option != "3"
                        ):
                            print(
                                "[Please Enter Center Number.1:Colombo,2:Galle,3:Kurnagala]"
                            )
                            center_option = str(input("Enter Center : "))
                            if center_option == "1":
                                center = "Colombo"
                                break
                            elif center_option == "2":
                                center = "Galle"
                                break
                            elif center_option == "3":
                                center = "Kurunagala"
                                break
                            else:
                                print(
                                    "Invalid center.Please enter one of the following (1:Colombo,2:Galle,3:Kurunagala)."
                                )

                    save_choice = ""
                    while (save_choice) not in ["yes", "no"]:
                        save_choice = input("Do you want to save the details ? (yes/no)").lower()
                        if save_choice == "yes":
                            student.update(
                            {
                                "nic": nic,
                                "first_name": first_name,
                                "last_name": last_name,
                                "birth_date": birth_date,
                                "address": permanent_address,
                                "phone_number": phone_number,
                                "tutorial_group": tutorial_group,
                                "center": center,
                            }
                        )

                            print("Updated successfully")
                            
                        elif save_choice == "no":
                            print("The student details have not been updated.")
                        else:
                            print("Invalid input.Pleas enetr 'yes' or 'no'")
        

                    


# Main Menu option
while menu_option != "7":

    print("---------------------------------------IIT Campus---------------------------------------")
    print("---------------------------------------Main Menu----------------------------------------")
    print("1.Enroll a new student")
    print("2.View details of a student")
    print("3.View details of all the students according to the branch")
    print("4.Update student details")
    print("5.Mark attendance")
    print("6.View attendance")
    print("7.Exit")

    menu_option = str(input("\t\t\t\t\t\tEnter Your Choice : ")).strip()

    # Student Enrollment process

    if menu_option == "1":
        print("---------------------------------------IIT Campus---------------------------------------")
        print("----------------------------------Enroll a new student----------------------------------")

        # Inputing Student Details
        student_id = ""
        nic = ""
        first_name = ""
        last_name = ""
        birth_date = ""
        permanent_address = ""
        phone_number = ""
        tutorial_group = ""
        center = ""

        while len(student_id) != 9 or (not student_id.isdigit()):
            student_id = str(input("Student ID : "))
            if len(student_id) != 9:
                print("Invalid Student ID ")
            if not student_id.isdigit():
                print("Student ID must be all digits")

        while len(nic) != 10:
            nic = str(input("NIC : "))
            if len(nic) != 10:
                print("Invalid NIC ")

        while len(first_name) == 0 or len(first_name) > 10:
            first_name = str(input("First Name : ")).strip()
            if len(first_name) < 1:
                print("First name cannot be empty.")
            elif len(first_name) > 10:
                print("First name must be within 10 characters")

        while len(last_name) == 0 or len(last_name) > 15:
            last_name = str(input("Last Name : ")).strip()
            if len(last_name) == 0:
                print("Last name can not be empty")
            elif len(last_name) > 15:
                print("Last name must be within 15 characters")

        while not validate_date(birth_date):
            birth_date = (input("Birth Date (YYYY-MM-DD) : ")).strip()
            if not validate_date(birth_date):
                print("Please enter correct date")

        while len(permanent_address) == 0 or len(permanent_address) > 15:
            permanent_address = input("Permanenet Address : ")
            if len(permanent_address) > 15:
                print("Permanent address mush be within 15 characters")
            elif len(permanent_address) == 0:
                print("permanent Address can not be empty.")

        while len(phone_number) != 10 or (not phone_number.isdigit()):
            phone_number = str(input("Phone Number : "))
            if len(phone_number) != 10:
                print("Phone number must be 10 digits.")
            elif not phone_number.isdigit():
                print("Phone Number should only have digits")

        while (tutorial_group) == "":
            tutorial_group = str(input("Tutorial Group : "))
            if (tutorial_group) == 0:
                print("Tutorial Group can not be empty.Please enter a valid value.")

        center_option = ""
        while center_option != "1" or center_option != "2" or center_option != "3":
            print("[Please Enter Center Number.1:Colombo,2:Galle,3:Kurnagala]")
            center_option = str(input("Enter Center : "))
            print(center_option)

            if center_option == "1":
                center = "Colombo"
                break
            elif center_option == "2":
                center = "Galle"
                break
            elif center_option == "3":
                center = "Kurunagala"
                break
            else:
                print(
                    "Invalid center.Please enter one of the following (1:Colombo,2:Galle,3:Kurunagala)."
                )

        # Asking user if they want to save the details
        save_choice = ""
        while (save_choice) not in ["yes", "no"]:
            save_choice = input("Do you want to save the details ? (yes/no)").lower()
            if save_choice == "yes":
                student_detail = {
                    "student_id": student_id,
                    "nic": nic,
                    "first_name": first_name,
                    "last_name": last_name,
                    "birth_date": birth_date,
                    "address": permanent_address,
                    "phone_number": phone_number,
                    "tutorial_group": tutorial_group,
                    "center": center,
                }
                students_list.append(student_detail)
                
                print("Student details have been saved successfully.")
            elif save_choice == "no":
                print("The student details have not been saved.")
            else:
                print("Invalid input.Pleas enetr 'yes' or 'no'")
            
        student_id = ""
        nic = ""
        first_name = ""
        last_name = ""
        birth_date = ""
        permanent_address = ""
        phone_number = ""
        tutorial_group = ""
        center = ""
        center_options = {"1": "Colombo", "2": "Galle", "3": "Kurnagala"}
        save_choice = ""


    # View detais of a student process
    elif menu_option == "2":
        view_student_details = "yes"
        while view_student_details == "yes":
            student_id = ""
            while len(student_id) != 9 or (not student_id.isdigit()):
                student_id = str(input("Student ID \t\t - \t"))
                if len(student_id) != 9:
                    print("Invalid Student ID ")
                if not student_id.isdigit():
                    print("Student ID must be all digits")

            # Print View deatails of the student
            found = False  # Flag to check if the student was found
            for student in students_list:
                if student["student_id"] == student_id:
                    print("---------------------------------------IIT Campus---------------------------------------")
                    print("\-------------------------------View details of a student-------------------------------")
                    print("NIC \t\t\t - \t", student["nic"])
                    print("Phone Number \t\t - \t", student["phone_number"])
                    print("First Name \t\t - \t", student["first_name"])
                    print("Last Name \t\t - \t", student["last_name"])
                    print("Tutorial Group  \t - \t", student["tutorial_group"])
                    print("Center \t\t\t - \t", student["center"])

                    found = True
                    break

            if not found:
                print("Student ID not found.")

            view_student_details = str(
                input(" Do you want to view another student's details (Yes/No) : ")
            ).lower()

    # View details of all the students

    elif menu_option == "3":
        print("---------------------------------------IIT Campus---------------------------------------")
        print("-----------------------------View Details Of All The Students---------------------------")
        students_in_branch = []

        center = ""
        center = str(input("Branch Name \t\t - \t")).lower()
        if center == "":
            print("Invalid Branch ")

        else:
            for student in students_list:
                if student["center"].lower() == center:
                    students_in_branch.append(student)

            if len(students_in_branch):
                print(
                    f'{"Student ID":<15}|{"NIC":<15}|{"First Name":<15}|{"Last Name":<15}|{"Tutorial Group":<15}'
                )
                for student in students_in_branch:
                    print(
                    f'{student["student_id"]:<15}|{student["nic"]:<15}|{student["first_name"]:<15}{student["last_name"]:<15}|{student["tutorial_group"]:<15}'
                )
            else:
                print("No students registered in this branch")

          
            update_details = ""
            while update_details != "yes" or update_details != "no":
                         update_details = str(
                              input("Do you want to update the details (Yes/No)?")
                         ).lower()
                         if update_details == "yes":
                              update_student_details()
                         elif update_details == "no":
                              break
                         else:
                              print("Please enter valid option")

    # Update Student Details

    elif menu_option =="4":
        print("---------------------------------------IIT Campus---------------------------------------")
        print("---------------------------------Update Student Details---------------------------------")
        update_student_details()

    # Marking Attendance
    elif menu_option == "5":
        status=""
        print("---------------------------------------IIT Campus---------------------------------------")
        print("------------------------------------Mark Attendance-------------------------------------")
        center=input("Center : ").lower()
        tutorial_group=input("Tutorial Group : ").lower()
        date = ""

        while not validate_date(date):
            date = (input("Date (YYYY-MM-DD): ")).strip()
            if not validate_date(date):
                print("Please enter correct date")
        
        students_by_branch_and_group =[]
        temp_list = []

        for student in students_list:
                if (student["center"].lower() == center and student["tutorial_group"].lower() == tutorial_group):
                    students_by_branch_and_group.append(student)
        
        if len(students_by_branch_and_group) < 1:
            print("No students registered in this branch and group")
        else:
            print("Student ID \t Present/Absent")
            for student in students_by_branch_and_group:
                status = input(f'{student["student_id"]} \t').strip().lower()
                temp_list.append({
                    "student_id": student["student_id"],
                    "date": date,
                    "tutorial_group": tutorial_group,
                    "center": center,
                    "status": status
                })


    #Asking user if they want to save details
            save_choice = ""
            while save_choice not in ["yes", "no"] :
                save_choice = input("Do you want to save the details ? (yes/no)").lower()
                if save_choice == "yes":
                    attendance_data = attendance_data + temp_list
                    print("Student details have been saved successfully.")
                elif save_choice == "no":
                    print("The student details have not been saved.")
                else:
                    print("Invalid input.Pleas enetr 'yes' or 'no'")

           

                    
#View attendence on perticular date
    elif menu_option == "6":
        print("---------------------------------------IIT Campus---------------------------------------")
        print("-------------------------------------View Attendence------------------------------------")

        redirect_to_menu = "no"

        while redirect_to_menu == "no":
            start_date=""
            end_date=""
            student_id = ""
            attendance_in_range=[]

            while len(student_id) != 9 or (not student_id.isdigit()):
                student_id = str(input("Student ID : "))
                if len(student_id) != 9:
                    print("Invalid Student ID ")
                if not student_id.isdigit():
                    print("Student ID must be all digits")

            while not validate_date(start_date):
                start_date = (input("Start Date (YYYY-MM-DD): ")).strip()
                if not validate_date(start_date):
                    print("Please enter correct date")

            while not validate_date(end_date):
                end_date = (input("End Date (YYYY-MM-DD): ")).strip()
                if not validate_date(end_date):
                    print("Please enter correct date")
                                
            for attendance in attendance_data:
                if(student["student_id"] == student_id and attendance["date"] >= start_date and attendance["date"] <= end_date):
                    attendance_in_range.append(attendance)
            
            if len(attendance_in_range) < 1:
                print("No attendance records found")
            
            else:
                print("Date \t\t Present/Absent")
                for attendance in attendance_in_range:
                    print(f'{attendance["date"]} \t {attendance["status"]}')

                
            student_id = ""
            redirect_to_menu = ""
            while redirect_to_menu not in ["yes", "no"]:
                redirect_to_menu = str(input("Do you want to direct to the main menu (Yes/No)? \t : \t")).lower()
                if(redirect_to_menu != "yes" and redirect_to_menu != "no"):
                    print("Please enter valid option")
                
        
#exsithin the program
    elif menu_option == "7":
        
        print("---------------------------------------IIT Campus---------------------------------------")
        print("------------------------------------------Exit------------------------------------------")
        print("Thank you for using the IIT Student Data Mangement System")