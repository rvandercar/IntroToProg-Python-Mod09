# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# rvandercar.12/18/2020.changed the code to complete my assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules (Done)
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file should not be imported for use")

# Main Body of Script  ---------------------------------------------------- #
# Variables #
lstEmployeeTable = []  # Employee list
lstFileData = []  # string object in list
# TODO: Add Data Code to the Main body
#
# Load data from file into a list when program starts

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()

# Get user's menu option choice
    strOption = Eio.input_menu_options()

# Show user current data in the list of employee objects
    if strOption == "1":
       Eio.print_current_list_items(lstEmployeeTable)
       continue

    # Let user add data to the list of employee objects
    elif strOption == "2":
        lstEmployeeTable.append(Eio.input_employee_data())
        continue
    # let user save current data to file
    elif strOption == "3":
        Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)

    # Let user exit program
    elif strOption == "4":
        break
# Main Body of Script  ---------------------------------------------------- #
