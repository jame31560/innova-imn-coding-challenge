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
        # Append a employee who are self management to employee list.
        self.employee.append(employee)

    def toStr(self, level=0):
        result = ""
        # level will generate different indent in front of result
        result += "{}{}\n".format("    "*level, self.firstName)
        # if don't have employee under self then return 
        if len(self.employee) <= 0:
            return result
        # print next level employees
        result += "{}Employees of: {}\n".format("    "*level, self.firstName)
        for employee in self.employee:
            # level add 1
            result += employee.toStr(level + 1)
        return result
