import pandas as pd
import sys

def read_file(file_path):
    '''
    Function to open and read a file, or raise an error if there is one
    '''
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception:
        return f"Error reading file '{file_path}'"

if __name__ == "__main__":
    #If there is too many or to few command line inputs, show usage message in the terminal, then quit running code
    if len(sys.argv) != 3: 
        print("Usage: python combine_csv.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1] #first file name from command line
    file2_path = sys.argv[2] #second file name from command line

    file1= read_file(file1_path)
    file2= read_file(file2_path)