import pandas as pd
import sys

def read_first_line(file_name):
    '''
    Function to read the header of a CSV file using pandas
    Returns the column names if successful, or an error message if not
    '''
    try:
        return pd.read_csv(file_name, nrows=0).columns
    except FileNotFoundError:
        return f"Error: The file '{file_name}' was not found."
    except pd.errors.EmptyDataError:
        return f"Error: The file '{file_name}' is empty."
    except Exception:
        return f"Error reading file '{file_name}'"
    
def read_file(file_name):
    '''
    Function to read a CSV file into a DataFrame using pandas
    Returns the DataFrame if successful, or an error message if not
    '''
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return f"Error: The file '{file_name}' was not found."
    except pd.errors.EmptyDataError:
        return f"Error: The file '{file_name}' is empty."
    except Exception:
        return f"Error reading file '{file_name}'"
    
def compare_headers(file1, file2):
    '''
    Function to compare headers of two CSV files. Raises ValueError if headers do not match.
    '''
    #read the first line from each file
    df1_header = read_first_line(file1) 
    df2_header = read_first_line(file2)

    #convert each header to a set for comparison
    df1_header= set(df1_header)
    df2_header = set(df2_header)

    #if the headers of each file are not identical, return an error
    if df1_header != df2_header:
        raise ValueError("CSV file columns do not match")

def combine_csvs(file1, file2):
    '''
    Function to combine two CSV files
    '''
    #read each file into a dataframe
    df1 = read_file(file1)
    df2 = read_file(file2)

    return pd.concat([df1, df2], ignore_index=True) #combine dataframes

if __name__ == "__main__":
    # Check for correct number of command-line arguments. Stop execution if incorrect number of arguments
    if len(sys.argv) != 3: 
        print("Usage: python combine_csv.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1] #first csv file from command line
    file2= sys.argv[2] #second csv file from command line

    compare_headers(file1, file2) #confirm headers of each file match
    combined_df = combine_csvs(file1, file2) #combine dataframes

    combined_df.to_csv('combined_file.csv', index=False) #save combined dataframe to a new csv file