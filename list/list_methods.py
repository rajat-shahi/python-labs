countries = ["India", "UK", "US", "Japan", "China", "Russia"]

countries.append("Nepal")  # push at the end
countries.insert(4, "South Korea")  # insert at any place

print(countries)

countries.pop()  # pop the last element
print(countries)

countries.remove("UK")  # remove any value
print(countries)

countries.pop(3)  # pop the element at an index
print(countries)

a = 10
b = 20
b, a = a, b  # swap the values
print(a, b)

arr = [2, 6, 1, -1, 0, 11]
print(arr)
arr.sort()  # sort the array in increasing order
print(arr)
arr.reverse()  # reverse the array
print(arr)
arr.sort(reverse=True)  # sort array in decreasing order
print(arr)

print(max(arr))  # find the max of the list
print(min(arr))  # find the min of the list
