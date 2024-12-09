# JSON to SQL Insert Script

This Python script is designed to automate the conversion of a JSON file containing location data into SQL `INSERT` statements for easy import into a database. It extracts data from the JSON structure, formats it properly, and generates a SQL script with the necessary statements.

## Features
- Reads location data from a JSON file.
- Converts each entry into a valid SQL `INSERT` statement.
- Ensures proper handling of special characters and JSON formatting for database compatibility.
- Saves the generated SQL script to a specified output file.

## Usage
1. Place your JSON file in the `files/` directory and name it `input.json`.
2. Run the script.
3. The generated SQL script will be saved as `output.sql` in the same directory.

## Example
For a JSON file structured as:
```json
{
  "location_data": {
    "Westlake": {"formatted_address": "Westlake, Cape Town, 7945, South Africa", ...},
    "Paulshof": {"formatted_address": "Paulshof, Sandton, South Africa", ...}
  }
}
```
The script will generate:
```sql
INSERT INTO `location_data` (location, data) VALUES ('Westlake', '{"formatted_address": "Westlake, Cape Town, 7945, South Africa", ...}');
INSERT INTO `location_data` (location, data) VALUES ('Paulshof', '{"formatted_address": "Paulshof, Sandton, South Africa", ...}');
```

## Requirements
- Python 3.x
- A JSON file with the expected structure.

## Notes
This script is especially useful for scenarios where you need to quickly import large datasets into a SQL database without manual effort.