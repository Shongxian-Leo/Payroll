import json
def addEmployee():
    try: #execption pseudocode
        with open("APU_Assignment.json", 'r') as FILE: #find the file name and read it
            file_content = FILE.read()
            if not file_content.strip(): #if there is no any character inside
                Employees_data = {} #create a dictionary
            else:
                Employees_data = json.loads(file_content) #if information exist, it will read the content
    except FileNotFoundError: #avoid the error of if "Apu_assignment" file did not exist
        Employees_data = {} #if not exist it will create a dictionary

    while True: #looping
        month = input("Please enter the month you want to enter:").capitalize()
        if month not in Employees_data:
            Employees_data[month] = []

        while True:
            add_employees = input(f"Do you want to add new employees data? (yes/no)").lower()
            if add_employees != 'yes':
                break
            Name = input("Please enter employee name: ")
            Emp_ID = input("Please enter employee ID: ")
            Department = input("Please enter the department you belong to: ")
            Basic_Salary = int(input("Please enter the basic salary: "))
            Allowance = int(input("Please enter the allowance: "))
            Bonus = int(input("Please enter the bonus: "))
            OT = int(input("Please enter the OT: "))

            input_data = {
                'Name': Name,
                'Employee_ID': Emp_ID,
                'Department': Department,
                'Basic Salary': Basic_Salary,
                'Allowance': Allowance,
                'Bonus': Bonus,
                'OT': OT,

            }
            Employees_data[month].append(input_data)

        additional_month = input("Do you want to continue add data for another month: (yes/no) ").lower()

        if additional_month != 'yes': #whether desire to repeat process
            break

    with open('APU_Assignment.json', 'w') as FILE:
        json.dump(Employees_data, FILE)


def generateSalary():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}

    month_check = input("Which month of payslip you want to generate?\n").capitalize()
    if month_check in Employees_data:
        check_employee = input("What is the employee ID you want to calculate?\n")
        employee_found = False

        for emp_data in Employees_data[month_check]:
            if check_employee == emp_data["Employee_ID"]:
                employee_found = True
                data = ['Commission (5% of total salary before EPF, below RM2000)',
                        'Tax (6% before EPF, Exceed RM 3000)',
                        'Net Salary',
                        'Total Salary',
                        'EPF (11%)'] #For updateEmployees' function

                for i in data:
                    emp_data.pop(i, None)
                Total_sal = (emp_data.get('Basic Salary',0) + emp_data.get('Allowance', 0) + emp_data.get('Bonus', 0) +
                             emp_data.get('OT', 0))
                # print(Total_sal)
                if Total_sal < 2000:
                    Commission = Total_sal * 0.05
                    Total_salary = Total_sal + Commission
                    EPF = Total_salary * 0.11
                    Net_salary = Total_salary - EPF
                    emp_data.update({
                        'Total Salary': Total_sal,
                        'Commission (5% of total salary before EPF, below RM2000)': Commission,
                        'EPF (11%)': EPF,
                        "Net Salary": Net_salary
                    })
                elif Total_sal > 3000:
                    tax = Total_sal * 0.06
                    Total_salary = Total_sal - tax
                    EPF = Total_salary * 0.11
                    Net_salary = Total_salary - EPF
                    emp_data.update({
                        'Total Salary': Total_sal,
                        'Tax (6% before EPF, Exceed RM 3000)': tax,
                        'EPF (11%)': EPF,
                        "Net Salary": Net_salary
                    })
                else:
                    Total_sal = Total_sal
                    EPF = Total_sal * 0.11
                    Net_salary = Total_sal - EPF
                    emp_data.update({
                        'Total Salary': Total_sal,
                        'EPF (11%)': EPF,
                        "Net Salary": Net_salary
                    })

        if not employee_found:
            print(f"Employee ID {check_employee} not found in {month_check}")

    with open('APU_Assignment.json', 'w') as FILE:
        json.dump(Employees_data, FILE)


def update_employee():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}
    month_check = input("Which month of payslip you want to access? ").capitalize()
    if month_check in Employees_data:
        check_employee = input("What is the employee ID you want to change?")

        for emp_data in Employees_data[month_check]:
            if emp_data['Employee_ID'] == check_employee:
                print(f"What information you want to change?\n1.Name \n2.Department \n3.Salary \n4.Allowance "
                      f"\n5.Bonus \n6.OT")
                selection = int(input("Please enter your selection: \n"))
                if selection == 1:
                    name = input("Enter updated Name: ")
                    emp_data['Name'] = name

                elif selection == 2:
                    Department = input("Enter updated Department: ")
                    emp_data['Department'] = Department

                elif selection == 3:
                    Basic_Salary = int(input("Please enter updated basic salary: "))
                    emp_data.update({'Basic Salary': Basic_Salary})

                elif selection == 4:
                    Allowance = int(input("Please enter update allowance: "))
                    emp_data.update({'Allowance': Allowance})

                elif selection == 5:
                    Bonus = int(input("Please enter updated bonus: "))
                    emp_data.update({'Bonus': Bonus})

                elif selection == 6:
                    OT = int(input("Please enter updated  OT: "))
                    emp_data.update({'OT': OT})

                else:
                    print("You select incorrect option")

                print(f"Employee ID {check_employee} updated successfully")
                break
        else:
            print(f"Employee ID {check_employee} not found in {month_check}")
    else:
        print(f"No data available for {month_check}")

    with open("APU_Assignment.json", "w") as FILE:
        json.dump(Employees_data, FILE)

    generateSalary()


def deleteEmployee():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}

    month_check = input("Which month of payslip you want to access?\n").capitalize()
    delete_employee = input("What is the employee ID you want to delete?\n")
    if month_check in Employees_data:
        cleaned_employee_data = []

        for emp_data in Employees_data[month_check]:
            if emp_data['Employee_ID'] != delete_employee:
                cleaned_employee_data.append(emp_data)

            print(f"Employee ID {delete_employee} deleted successfully")

        Employees_data[month_check] = cleaned_employee_data

    else:
        print(f"The Employee ID  {delete_employee}is not found in {month_check}")

    with open("APU_Assignment.json", "w") as file:
        json.dump(Employees_data, file)


def search_Payslip():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}

    month_check = input("Which month of payslip do you want to access?\n ").capitalize()

    if month_check in Employees_data:
        employee_id = input("What is your employee ID\n")

        for emp_data in Employees_data[month_check]:
            # print("Current emp_data:", emp_data)
            if employee_id == emp_data['Employee_ID']:
                print("************** APU Sdn Bhd's Payroll***************")
                print(f"Payslip for the Month of {month_check}")
                print(f"Employee_ID: {employee_id}\t\t Employee Name: {emp_data['Name']}")
                print(f"Department: {emp_data['Department']}")
                print(f"Basic Salary: {emp_data['Basic Salary']}")
                print(f"Allowance: {emp_data['Allowance']}")
                print(f"Bonus: {emp_data['Bonus']}")
                print(f"OT: {emp_data['OT']}")
                print(f"Gross Salary: {emp_data['Total Salary']}")
                if "Commission (5% of total salary before EPF, below RM2000)" in emp_data:
                    print(f"Add: Commission (5% of total salary before EPF, below RM2000): {emp_data['Commission (5% of total salary before EPF, below RM2000)']}")
                elif "Tax (6% before EPF, Exceed RM 3000)" in emp_data:
                    print(f"Deduct: Tax (6% before EPF, Exceed RM 3000): {emp_data['Tax (6% before EPF, Exceed RM 3000)']}")
                print(f"Deduct: EPF (11%): {emp_data['EPF (11%)']}")
                print(f"Net Salary: {emp_data['Net Salary']}")
                break
        else:
            print(f"The employee ID: {employee_id} is not found in {month_check}")
    else:
        print(f"It's unable to find {month_check} in APU Sdn Bhd's system")


def viewPaySlip():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}

    month_check = input("Which month of payslip do you want to access?\n").capitalize()
    employee_id = input("What is your employee ID\n")
    printed_payslip = []

    if month_check in Employees_data:

        for emp_data in Employees_data[month_check]:
            # print("Current emp_data:", emp_data)
            if employee_id == emp_data["Employee_ID"]:
                if "Commission (5% of total salary before EPF, below RM2000)" in emp_data:
                    text = str(f"************** APU Sdn Bhd's Payroll***************\n" +
                            f"Payslip for the Month of {month_check}\n" +
                            f"Employee_ID: {employee_id}\t\t Employee Name: {emp_data['Name']}\n"+
                            f"Department: {emp_data['Department']}\n" +
                            f"Basic Salary: {emp_data['Basic Salary']}\n" +
                            f"Allowance: {emp_data['Allowance']}\n" +
                            f"Bonus: {emp_data['Bonus']}\n" +
                            f"OT: {emp_data['OT']}\n" +
                            f"Gross Salary: {emp_data['Total Salary']}\n" +
                            f"Add: Commission (5% of total salary before EPF, below RM2000): {emp_data['Commission (5% of total salary before EPF, below RM2000)']}\n"+
                            f"Deduct: EPF (11%): {emp_data['EPF (11%)']}\n" +
                            f"Net Salary: {emp_data['Net Salary']}"
                               )

                elif "Tax (6% before EPF, Exceed RM 3000)" in emp_data:
                    text = str(f"************** APU Sdn Bhd's Payroll***************\n" +
                            f"Payslip for the Month of {month_check}\n" +
                            f"Employee_ID: {employee_id}\t\t Employee Name: {emp_data['Name']}\n"+
                            f"Department: {emp_data['Department']}\n" +
                            f"Basic Salary: {emp_data['Basic Salary']}\n" +
                            f"Allowance: {emp_data['Allowance']}\n" +
                            f"Bonus: {emp_data['Bonus']}\n" +
                            f"OT: {emp_data['OT']}\n" +
                            f"Gross Salary: {emp_data['Total Salary']}\n" +
                            f"Deduct: Tax (6% before EPF, Exceed RM 3000): {emp_data['Tax (6% before EPF, Exceed RM 3000)']}\n" +
                            f"Deduct: EPF (11%): {emp_data['EPF (11%)']}\n" +
                            f"Net Salary: {emp_data['Net Salary']}"
                               )
                else:
                    text = str(f"************** APU Sdn Bhd's Payroll***************\n" +
                            f"Payslip for the Month of {month_check}\n" +
                            f"Employee_ID: {employee_id}\t\t Employee Name: {emp_data['Name']}\n"+
                            f"Department: {emp_data['Department']}\n" +
                            f"Basic Salary: {emp_data['Basic Salary']}\n" +
                            f"Allowance: {emp_data['Allowance']}\n" +
                            f"Bonus: {emp_data['Bonus']}\n" +
                            f"OT: {emp_data['OT']}\n" +
                            f"Gross Salary: {emp_data['Total Salary']}\n" +
                            f"Deduct: EPF (11%): {emp_data['EPF (11%)']}\n" +
                            f"Net Salary: {emp_data['Net Salary']}"
                               )

                printed_payslip.append(text)

        # Employees_data[month_check] = printed_payslip
        file = open(f"Payslip of {month_check} for {employee_id}.txt", "w")
        file.writelines(printed_payslip)

    else:
        print(f"The employee ID: {employee_id} is not found in {month_check}")

def exit():
    try:
        with open("APU_Assignment.json", 'r') as FILE:
            file_content = FILE.read()
            if not file_content.strip():
                Employees_data = {}
            else:
                Employees_data = json.loads(file_content)
    except FileNotFoundError:
        Employees_data = {}

    file = open("APU_Assignment.json", "r")
    print(file.read())
    for i in file:
        print(i)

    file.close()



print("************** APU Payroll***************")
print("1. Employee Profile")
print("2. Salary Generator")
print("3. Pay Slip")

selection = int(input("Please enter your selection from the Menu:\n"))

if selection == 1:
    print("You have select employee profile")
    decision = int(input("Do you want to (1) add employee or (2) delete employee or (3) update employee's information\n"))
    if decision == 1:
        addEmployee()
    elif decision == 2:
        deleteEmployee()
    elif decision == 3:
        update_employee()
elif selection == 2:
    print("You have select salary generator")
    generateSalary()
elif selection == 3:
    print("You have select payslip")
    decision = int(input("Do you want to (1) search Payslip or (2) view Payslip\n"))
    if decision == 1:
        search_Payslip()
    elif decision == 2:
        viewPaySlip()
elif selection == 4:
    print("You select the exit function and display the information")
    exit()
# elif selection == 4:
#     try:
#         with open("APU_Assignment.json", 'r') as FILE:
#             file_content = FILE.read()
#             if not file_content.strip():
#                 Employees_data = {}
#             else:
#                 Employees_data = json.loads(file_content)
#     except FileNotFoundError:
#         Employees_data = {}
#
#     Employees_data.clear()
#
#     with open("APU_Assignment.json", "w") as file:
#         json.dump(Employees_data, file)
else:
    print("You select a wrong one")



# else:
#     print("You select a wrong one")
file = open("APU_Assignment.json", "r")
print(file.read())
for i in file:
    print(i)
