def input_number():
    return int(input("Enter the Integer"))


def input_float():
    return float(input("Enter the Float"))


choice = input("Whether you want to input 'Integer' or 'Float'")

if choice == "Integer":
    input_number()
elif choice == "Float":
    input_float()
else:
    print("Invalid Choice")
