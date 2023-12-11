# question 1
import pandas as pd

def calculate_distance_matrix(data_file):
    # Read the data from the CSV file
    df = pd.read_csv(data_file, sep='\t')

    # Check for the actual column names in the DataFrame
    if 'id_start' not in df.columns or 'id_end' not in df.columns or 'distance' not in df.columns:
        raise ValueError("Column names are not present in the DataFrame. Please check the column names in your CSV file.")

    # Create an empty DataFrame for the distance matrix
    unique_ids = sorted(set(df['id_start'].tolist() + df['id_end'].tolist()))
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)

    # Fill the diagonal with zeros
    distance_matrix.values[[range(len(unique_ids))]*2] = 0

    # Iterate through the rows of the original DataFrame to calculate cumulative distances
    for index, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']

        # Add distance to the matrix
        distance_matrix.at[start_id, end_id] = distance_matrix.at[end_id, start_id] = distance

    # Perform cumulative summation along the rows
    distance_matrix = distance_matrix.cumsum(axis=1)

    return distance_matrix

# Example usage:
data_file = 'dataset-3.csv'
result_matrix = calculate_distance_matrix(data_file)

# Display the resulting distance matrix
print("Question 1 =",result_matrix)


