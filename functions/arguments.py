# func(a,b)
# func(a=10,b=10)
# while calling can do something like this : fn_call(10,b=10) , fn_call(a=10,b=10), fn_call(b=10,a=20)


def square_sum(x=2, y=3):
    print(f"x : {x} , y : {y}")
    return (x * x) + (y * y)


print(square_sum(10, 5))
print(square_sum(3))
print(square_sum())
print(square_sum(y=10))
print(square_sum(y=1, x=2))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


def double_list(values):
    doubled_values = []

    values[0] = 10

    for value in values:
        doubled_values.append(value * 2)

    return doubled_values


arr = [1, 2, 3, 4, 5]
print(f"Original Array : {arr}")
print(double_list(arr))
print(f"Modified Array : {arr}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


def print_arguments(*argv):
    for arg in argv:
        print(arg, end=" ")


print_arguments(10, [20, 30], ("Rajat", "Shahi"), "Rajat Shahi")
