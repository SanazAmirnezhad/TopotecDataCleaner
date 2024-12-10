import pandas as pd

def data_cleaner(input_file, output_file):
     """
     Clean and analyze survey data from a CSV file.
     """
     # Load data

     data = pd.read_csv(input_file)
 
     # 1. Remove duplicates
     data = data.drop_duplicates()
 
     # Replace missing GPS coordinates with default value (-9999)
     data['Latitude'] = data['Latitude'].fillna(-9999)
     data['Longitude'] = data['Longitude'].fillna(-9999)
 
     # Format Date
     if 'Timestamp' in data.columns:
         data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
 
     # Analysis:
     print("analysis")
     total_points = len(data)
     missing_gps = data[(data['Latitude'] == -9999) & (data['Longitude'] == -9999)].shape[0]
 
     print(f"Total data points: {total_points}")
     print(f"Data points with missing GPS info: {missing_gps}")
 
     # Save the cleaned data
     print("Saving")
     data.to_csv(output_file, index=False)
     print(f"Cleaned data saved to {output_file}")
# Get input file path from the user
input_file = input("Enter the path to your input CSV file: ").strip()
    # Get output file path from the user
output_file = input("Enter the path to save the cleaned data (e.g., cleaned_data.csv): ").strip()

    # Run the data cleaning function
data_cleaner(input_file, output_file)

 