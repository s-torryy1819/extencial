def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result
print(raise_to_power(3, 2))

#TRANSLATOR
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"

        else:
            translation += letter
    return translation
#print(translator(input("Enter the phrase :  ")))

'''

try:

    num = int(input("Enter a number:  "))
    print(num)
except ZeroDivisionError as err:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")
'''

employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()