import json

def is_registration(input_str):
    # Simple heuristic: registration often contains a dash and is not all digits
    return '-' in input_str and not input_str.isdigit()

def main():
    json_file = 'dynamic.json'

    # Load existing JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    new_rows = []
    for i in range(3):
        user_input = input(f"Enter flight number or aircraft registration ({i+1}/3): ").strip().upper()
        if is_registration(user_input):
            url = f"https://www.flightradar24.com/data/aircraft/{user_input}"
            label = user_input
        else:
            # Assume it's a flight number
            url = f"https://www.flightradar24.com/data/flights/{user_input}"
            label = user_input
        new_rows.append({"label": label, "url": url})

    # Update the rows in the JSON data
    data['rows'] = new_rows

    # Write back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

    print("JSON file updated successfully.")

if __name__ == "__main__":
    main()
