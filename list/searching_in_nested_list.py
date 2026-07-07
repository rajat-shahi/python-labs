countries = [
    ["Egypt", "USA", "India"],
    ["Dubai", "America", "Spain"],
    ["London", "England", "France"],
]

filtered_countries = [
    country for sublist in countries for country in sublist if len(country) < 6
]

print(filtered_countries)
