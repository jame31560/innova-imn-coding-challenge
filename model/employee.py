class Employee():
    def __init__(self, id, firstName, salary, manager=None, employee=None):
        self.id = id
        self.firstName = firstName
        self.salary = salary
        self.manager = manager
        if employee is None:
            employee = []
        self.employee = employee

    def addEmployee(self, employee):
        self.employee.append(employee)

    def toStr(self, level=0):
        result = ""
        result += "{}{}\n".format("    "*level, self.firstName)
        if len(self.employee) <= 0:
            return result
        result += "{}Employees of: {}\n".format("    "*level, self.firstName)
        for employee in self.employee:
            result += employee.toStr(level + 1)
        return result
