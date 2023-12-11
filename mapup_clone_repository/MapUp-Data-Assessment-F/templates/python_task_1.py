# question 1
import pandas as pd

def generate_car_matrix(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Create a pivot table using id_1, id_2, and car columns
    pivot_table = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0
    pivot_table = pivot_table.fillna(0)

    # Set diagonal values to 0
    for i in range(min(pivot_table.shape)):
        pivot_table.iloc[i, i] = 0

    return pivot_table

# Example usage:
dataset_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)

print("Question 1 =", result_matrix)


# question 2
import pandas as pd

def get_type_count(data):
    # Add a new categorical column 'car_type' based on the specified conditions
    data['car_type'] = pd.cut(data['car'], bins=[float('-inf'), 15, 25, float('inf')],
                              labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each 'car_type' category
    type_count = data['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_count = dict(sorted(type_count.items()))

    return sorted_type_count

df = pd.read_csv('dataset-1.csv')

# Example usage
result = get_type_count(df)
print("Question 2 =",result)


# Question 3
import pandas as pd

def get_bus_indexes(data_frame):
    # Calculate the mean value of the 'bus' column
    mean_bus_value = data_frame['bus'].mean()

    # Identify indices where the bus values are greater than twice the mean
    bus_indexes = data_frame[data_frame['bus'] > 2 * mean_bus_value].index

    # Convert the indices to a sorted list
    sorted_bus_indexes = sorted(bus_indexes)

    return sorted_bus_indexes

# Load the CSV file into a DataFrame
dataset_1 = pd.read_csv('dataset-1.csv')

# Call the function and get the result
result = get_bus_indexes(dataset_1)

# Print the result
print("Question 3 =",result)


# Question 4
import pandas as pd

def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter routes based on the condition (average of truck column > 7)
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index

    # Sort the routes and return as a list
    sorted_routes = sorted(filtered_routes.tolist())

    return sorted_routes

# Example usage
file_path = 'dataset-1.csv'
result = filter_routes(file_path)
print("Question 4 =",result)


# Question 5
def multiply_matrix(input_matrix):
    # Create a copy of the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to modify the values
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage:
modified_result_matrix = multiply_matrix(result_matrix)

print("Question 5 =", modified_result_matrix)


# Question 6
import pandas as pd

def check_time_completeness(df):
    # Combine startDay and startTime to create a datetime column
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%A %H:%M:%S')
    
    # Combine endDay and endTime to create a datetime column
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%A %H:%M:%S')
    
    # Calculate the time difference between start and end timestamps
    df['time_difference'] = df['end_timestamp'] - df['start_timestamp']
    
    # Check if each time range covers a full 24-hour period and spans all 7 days of the week
    completeness_series = (
        (df['time_difference'] == pd.Timedelta(days=1)) &
        (df['start_timestamp'].dt.day_name() == df['end_timestamp'].dt.day_name())
    )
    
    # Check if 'id' and 'id_2' columns exist in the DataFrame
    if 'id' in df.columns and 'id_2' in df.columns:
        # Create a multi-index series with (id, id_2) as index
        result_series = completeness_series.groupby(['id', 'id_2']).all()
        return result_series
    else:
        raise KeyError("'id' or 'id_2' column not found in the DataFrame.")

# Example usage:
df = pd.read_csv('dataset-2.csv')
result_series = check_time_completeness(df)
print("Question 6 =",result_series)
