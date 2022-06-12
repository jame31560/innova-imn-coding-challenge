# innova-imn-coding-challenge


## Run the Code
Note: python3.x is required

```
$ python main.py -f [your input file]
```

## Run the Test
```
$ python test.py
```

### How to add test file
Add the custom test case under `testcase/input` & `testcase/output` folder.  
This is the test for `employeesToStr()` function.
Each test case input & output file must have the same filename.

## About solving solution
The Solution process I think:
1. Sort the input employee list by employee's first name.
2. Then Create a dict to store each employee object, and the key has be set ad employee's id. So that I can get the employee I want easier.
3. In second step, I also store the first level(who don't have manager) employee. This is a record that I can use this in finally when I print the employee tree. 
4. The fourth step, I add the each employee to its manager's object.
5. Finally, print all first level employee, and the `toStr()` function in employee class, it will automatically print all its employee children.