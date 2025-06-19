import pandas as pd
import re

# Function to validate option_part_no based on the given formats
def is_valid_option_part_no(part_number: str) -> bool:
    part_number = part_number.strip()  # Strip leading/trailing spaces
    
    # Regular expressions for different formats
    ucs_mr_pattern = r"^(UCS|UCSX)-?MR(-?[A-Za-z0-9]+)+(-[A-Za-z0-9]+)?(-?[A-Za-z0-9]{1,2})?$" # UCS-MR or UCSX-MR followed by 1 or 2 alphanumeric characters
    hdd_pattern = r"^(UCS|UCSX)-?HD-?[A-Za-z0-9]+(-?[A-Za-z0-9]{1,2})?(-?[A-Za-z0-9]{1,2})?$"  # UCS/ UCSX - HD followed by alphanumeric and optional -XX
    ssd_pattern = r"^(UCS|UCSX)-?SD-?[A-Za-z0-9]+(-[A-Za-z0-9]{1,2})?(-?[A-Za-z0-9]{1,2})?$"  # UCS/ UCSX - SD followed by alphanumeric and optional -XX
    cpu_pattern = r"^(UCS|UCSX)-?CPU--?[A-Za-z0-9]+(-?[A-Za-z0-9]{1,2})?$"  # UCS-CPU followed by alphanumeric characters
    ucsxs_pattern = r"^(UCSXS)[A-Za-z0-9]+[A-Za-z0-9]+[A-Za-z0-9]+-D$" # Regular expression to match the given format for UCSXS
    
    # Check against all the patterns
    if re.match(ucs_mr_pattern, part_number):
        return True
    if re.match(hdd_pattern, part_number):
        return True
    if re.match(ssd_pattern, part_number):
        return True
    if re.match(cpu_pattern, part_number):
        return True
    if re.match(ucsxs_pattern, part_number):
        return True
    
    return False

# Function to validate a CSV file containing the 'option_part_no' column
def validate_option_part_no_in_csv(csv_file_path: str, output_file_path: str):
    # Load CSV data using pandas
    df = pd.read_csv(csv_file_path)
    
    # Check if 'option_part_no' column exists in the CSV
    if 'option_part_no' not in df.columns:
        raise ValueError("The CSV file must contain an 'option_part_no' column.")
    
    # Apply the validation function to the 'option_part_no' column
    df['valid'] = df['option_part_no'].apply(is_valid_option_part_no)
    
    # Optionally, save the results back to a new CSV file
    df.to_csv(output_file_path, index=False)
    
    # Return the modified DataFrame
    return df

# Example usage:
csv_file_path = 'E:\\Pytest\\04062025_cisco_db_import.csv'  # Replace with the path to your CSV file
output_file_path = 'output.csv'  # Replace with the desired output file path

# Validate and get the DataFrame with validation results
result_df = validate_option_part_no_in_csv(csv_file_path, output_file_path)

# Print the resulting DataFrame (optional)
print(result_df.head())
