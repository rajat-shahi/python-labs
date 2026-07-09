# collection of key-value pairs
# imp. things are : listing keys, listing values, listing items
# keys() , values() , items()

# iterable is an object capable of returning elements one at a time
# we can use loops on any iterable object

driverDetails = {
    "Lewis Hamilton": "Scuredia Ferrari",
    "Charles Leclerc": "Scuredia Ferrari",
    "Max Verstappen": "Red Bull Racing",
    "Oscar Piastri": "McLaren",
}

print(driverDetails)
print(driverDetails["Max Verstappen"])

driverDetails.popitem()
print(driverDetails)

driverDetails.update({"Lando Norris": "McLaren"})
print(driverDetails)

print(driverDetails.keys())
print(driverDetails.values())
print(driverDetails.items())


for key in driverDetails.keys():
    print(f"Drive Name - {key} , Team - {driverDetails[key]}")

for driver in driverDetails.values():
    print(driver)

for item in driverDetails.items():
    print(f"{item[0]}, {item[1]}")

del driverDetails["Lewis Hamilton"]
print(driverDetails)

driverDetails.clear()  # clear the dictionary
