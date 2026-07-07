superheros = ["Thor", "Iron Man", "Loki", "Captain America"]
superhero = "Loki"


if superhero in superheros:
    print(f"We found {superhero}")
else:
    print(f"We didn't find {superhero}")


if "Batman" not in superheros:
    print("Batman is not available in superheros list")
else:
    print("Batman is available in superheros list")
