# arithmetic arranger.  This takes math strings horizontal and returns them in vertical
import re


def arranger(input):
    if type(input) != list:
        return print("Please use a list data type.")
    if len(input) > 5:
        return print(
            "We can only take a maximum of 5 problems at a time, please use fewer."
        )
    for i in input:
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
                total += int(x)
            print("The sum of " + i + " is " + str(total))
        elif operation == "-":
            item = i.split(operation)
            item = list(map(int, item))
            difference = item[0] - item[1]
            print("The difference of " + i + " is " + str(difference))
        elif operation == "*":
            item = i.split(operation)
            item = list(map(int, item))
            product = item[0] * item[1]
            print("The product of " + i + " is " + str(product))
        elif operation == "/":
            item = i.split(operation)
            item = list(map(int, item))
            division = item[0] / item[1]
            print("The division of " + i + " is " + str(division))


# test case
arranger(["5 % 6", "1 - 3", "1 + 2", "6 / 3", "13 * 8"])
