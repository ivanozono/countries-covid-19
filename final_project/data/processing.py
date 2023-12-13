# Importing required modules and functions for data processing
import final_project.utils.paths as path  # Custom module for managing file paths
import pandas as pd  # Pandas library for data manipulation and analysis
import janitor  # Janitor library to extend Pandas with more convenient data cleaning functions

def load_proccesed_data(file_name):
    """
    Loads processed data from a CSV file and transforms the 'date' column to datetime objects.
    
    Parameters:
    file_name (str): The file path to the CSV file to be loaded.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the processed data with the 'date' column
                      formatted as datetime objects.
    """
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_name)
    
    # Use the `transform_column` method from the Janitor library to convert the 'date'
    # column from a string to a Pandas datetime object, which is essential for
    # time-series analysis as it allows for date and time based operations.
    df = df.transform_column("date", pd.to_datetime)
    
    return df  # Return the processed DataFrame
