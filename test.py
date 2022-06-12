import unittest
import os
from main import readEmployeesFromFile, employeesToStr


class TestEmployeeToStr(unittest.TestCase):
    def test_employee_to_str(self):
        for filename in os.listdir("testcase/input"):
            employeeList = readEmployeesFromFile(
                "testcase/input/{}".format(filename))
            with open("testcase/output/{}".format(filename)) as f:
                contents = f.read()
            self.assertEqual(employeesToStr(employeeList),
                             contents, "should be empty")


if __name__ == '__main__':
    unittest.main()
