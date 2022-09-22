# arithmetic arranger.  This takes math strings horizontal and returns them in vertical
import re

# this function converts strings to integers and does the arithmetic in the event show_answers=True
def do_the_math(input_list):
    if type(input_list) != list:
        return print("Please use a list data type.")
    if len(input_list) > 5:
        return print(
            "We can only take a maximum of 5 problems at a time, please use fewer."
        )
    for i in input_list:
        result = re.search(r"[+,\-,\*,\/]", i)

        try:
            operation = result.group()
        except:
            print("There is no proper operator in " + i)
            continue
        if operation == "+":
            item = i.split(operation)
            total = 0
            for x in item:
                return total += int(x)
            # print("The sum of " + i + " is " + str(total))
        elif operation == "-":
            item = i.split(operation)
            item = list(map(int, item))
            return difference = item[0] - item[1]
            # print("The difference of " + i + " is " + str(difference))
        elif operation == "*":
            item = i.split(operation)
            item = list(map(int, item))
            return product = item[0] * item[1]
            # print("The product of " + i + " is " + str(product))
        elif operation == "/":
            item = i.split(operation)
            item = list(map(int, item))
            return division = item[0] / item[1]
            # print("The division of " + i + " is " + str(division))

# this function will actually print the arranged strings
def string_manipulation(input_list):
    for i in input_list:
        result = re.search(r"[+,\-,\*,\/]", i)

        try:
            operation = result.group()
        except:
            print("There is no proper operator in " + i)
            continue
        if operation == "+":
            item = i.split(operation)

        elif operation == "-":
            item = i.split(operation)

        elif operation == "*":
            item = i.split(operation)

        elif operation == "/":
            item = i.split(operation)
# test case

