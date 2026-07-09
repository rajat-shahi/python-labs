def check_even(x):
    if x % 2 == 0:
        return True


print(check_even(10))
print(check_even(5))


# the below function stop executing the function once the error hits
def error_hit(list):
    for log in logs:
        if log == "error":
            return
        else:
            print(log)


logs = ["exec1", "exec2", "error", "exec3", "error"]
error_hit(logs)
