from model.employee import Employee
import argparse
import json


def printEmployees(employeeList):
    try:
        employeeDict = dict()
        topEmployeeList = list()
        totalSalary = 0

        # Sort by employee first_name
        employeeList.sort(key=lambda employee: employee["first_name"])

        # Create each employee object and make a dict with key: id, Value: employee object
        for employee in employeeList:
            # New employee object
            newEmployee = Employee(
                employee["id"], employee["first_name"], employee["salary"], employee["manager"]
            )
            # Add salary
            totalSalary += newEmployee.salary

            # Add employee to dict
            employeeDict[employee["id"]] = newEmployee

            # if employee manager is empty means it is the top level employee
            if newEmployee.manager is None:
                topEmployeeList.append(newEmployee)

        # add each employee object to its manager's object
        for id in employeeDict:
            employee = employeeDict[id]
            # if this employee doesn't have manager than pass.
            if employee.manager is None:
                continue
            # check if manager exist
            if employee.manager not in employeeDict:
                raise ValueError(
                    "Manager id \"{}\" not found".format(employee.manager)
                )
            # Add self into manager's object
            manager = employeeDict[employee.manager]
            manager.addEmployee(employee)

        # print employee detail from toplevel employees
        for topEmployee in topEmployeeList:
            print(topEmployee.toStr())

        # Print the total salary
        print("Total salary: {}".format(totalSalary))
    except Exception as e:
        print(e)


def main():
    # get parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Employees data file. Default will open 'employees.json' in local directory.",
        default="employees.json"
    )
    args = parser.parse_args()
    config = vars(args)

    try:
        # open json file
        file = open(config["file"])
    except FileNotFoundError:
        print("Can't not found '{}'".format(config["file"]))
        return

    try:
        # read input
        employeeList = json.load(file)
    except:
        print("Invalid JSON file")
        file.close()
        return

    file.close()

    # print employees
    printEmployees(employeeList)


if __name__ == '__main__':
    main()
