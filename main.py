import json
import os

# Input and output file paths
input_file_path = os.path.join(os.path.dirname(__file__), "files/input.json")
output_file_path = os.path.join(os.path.dirname(__file__), "files/output.sql")

try:
    # Load the JSON file
    with open(input_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract location data
    location_data = data.get("location_data", {})

    if not location_data:
        raise ValueError("No 'location_data' found in the input JSON file.")

    # SQL INSERT script
    insert_statements = []

    for location, location_details in location_data.items():
        # Ensure the JSON data is formatted as a valid JSON string for SQL
        json_data = location_details
        
        # json_data = json.dumps(json.dumps(json.dumps(location_details)))
        json_data = json.dumps(location_details)
   
        # Generate the SQL INSERT statement
        insert_statement = (
            f"INSERT INTO `location_data` (location, data) "
            f"VALUES ('{location}', '{json_data}');"
        )
        insert_statements.append(insert_statement)

    # Generate the SQL script
    sql_script = "\n".join(insert_statements)

    # Save the SQL script to the output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(sql_script)

    print(f"SQL script generated successfully and saved to {output_file_path}")

except json.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON file. Details: {e}")
except FileNotFoundError as e:
    print(f"Error: Input file not found. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
