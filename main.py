from cgi import print_exception
from pprint import pprint
from model.employee import Employee


def main():
    req = [
        {
            "id": 1,
            "first_name": "Dave",
            "manager": 2,
            "salary": 100000
        },
        {
            "id": 2,
            "first_name": "Jeff",
            "manager": None,
            "salary": 110000
        },
        {
            "id": 3,
            "first_name": "Andy",
            "manager": 1,
            "salary": 90000
        },
        {
            "id": 4,
            "first_name": "Jason",
            "manager": 1,
            "salary": 80000
        },
        {
            "id": 5,
            "first_name": "Dan",
            "manager": 1,
            "salary": 70000
        },
        {
            "id": 6,
            "first_name": "Rick",
            "manager": 9,
            "salary": 60000
        },
        {
            "id": 9,
            "first_name": "Suzanne",
            "manager": 1,
            "salary": 80000
        }
    ]
    try:
        employeeDict = dict()

        topEmployees = list()

        totalSalary = 0

        for employee in req:
            newEmployee = Employee(
                employee["id"], employee["first_name"], employee["salary"], employee["manager"]
            )
            totalSalary += newEmployee.salary
            employeeDict[employee["id"]] = newEmployee
            if newEmployee.manager is None:
                topEmployees.append(newEmployee)

        for id in employeeDict:
            employee = employeeDict[id]
            if employee.manager is None:
                continue
            manager = employeeDict[employee.manager]
            if manager is None:
                raise ValueError("Manager id \"%s\" not found" % manager)
            manager.addEmployee(employee)

        # for id in employeeDict:
        #     employee = employeeDict[id]
        #     print(employee)
        #     print(vars(employee))

        for topEmployee in topEmployees:
            print(topEmployee.toStr())
        print("Total salary: {}".format(totalSalary))

    except Exception as e:
        print_exception(e)


if __name__ == '__main__':
    main()
