# src/main.py
from src import get_user_data

if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    user_data = get_user_data(user_id)

    #print("User Data:", user_data)

    if user_data["location"] is None:
        print("Current Location: (unavailable)")
    elif isinstance(user_data, dict):
        if "location" in user_data:
            print("Current Location:", user_data["location"])
        else:
            print("Error finding location")
    else:
        print("Error fetching data")
