import random
from datetime import datetime

# List of famous people with characteristics 
famous_people = [
    {"name": "Daniel Radcliffe", "gender": "male", "hair_color": "brown", "eye_color": "brown"},
    {"name": "Rupert Grint", "gender": "male", "hair_color": "red", "eye_color": "blue"},
    {"name": "Emma Watson", "gender": "female", "hair_color": "brown", "eye_color": "brown"},
    {"name": "Selena Gomez", "gender": "female", "hair_color": "brown", "eye_color": "brown"},
    
    {"name": "Zlatan Ibrahimovic", "gender": "male", "hair_color": "black", "eye_color": "brown"},
    {"name": "David Hellenius", "gender": "male", "hair_color": "black", "eye_color": "blue"},
    {"name": "Ed Sheeran", "gender": "male", "hair_color": "orange", "eye_color": "blue"},
    {"name": "Zara Larsson", "gender": "female", "hair_color": "blond", "eye_color": "blue"},
    {"name": "Brad Pitt", "gender": "male", "hair_color": "blond", "eye_color": "blue"},
]

# Function for generate "Search of the Day"
def get_search_of_the_day():
    genders = ["male", "female"]
    hair_colors = ["brown", "blond", "black", "red", "grey"]
    eye_colors = ["brown", "blue", "green", "grey"]

    # Random characteristics for the day
    daily_gender = random.choice(genders)
    daily_hair_color = random.choice(hair_colors)
    daily_eye_color = random.choice(eye_colors)

    return daily_gender, daily_hair_color, daily_eye_color

# Save todays date and "Search of the Day" i a variable
current_date = datetime.now().date()
search_of_the_day = get_search_of_the_day()

print("     .:Fame Matcher :.")

print("----------------------------")

print(f"Search of the Day ({current_date})\n Gender: {search_of_the_day[0]}, Hair color: {search_of_the_day[1]}, Eye color: {search_of_the_day[2]}")

print("----------------------------")

# Ask user for characteristics
gender = input("Enter gender (male/female): ").lower()
hair_color = input("Enter hair color: ").lower()
eye_color = input("Enter eye color: ").lower()

# Search for matches
matches = [person["name"] for person in famous_people if person["gender"] == gender and person["hair_color"] == hair_color and person["eye_color"] == eye_color]

# Print the results
if matches:
    print("Matching famous people:")
    for match in matches:
        print("- " + match)
else:
    print("No matches found.")
