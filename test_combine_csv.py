import pandas as pd
import pytest
import combine_csv

def test_read_first_line():
    first_line = combine_csv.read_first_line('sample_csv_1.csv')
    assert list(first_line) == ['Animal', 'Class', 'Legs', 'Predator']

def test_read_file():
    df = combine_csv.read_file('sample_csv_1.csv')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (6, 4)
    assert list(df.columns) == ['Animal', 'Class', 'Legs', 'Predator']
    assert df.values.tolist() == [['Orca','Mammal',0,'Yes'], ['Butterfly','Invertebrate',6,'No'], 
                                  ['Snake','Reptile',0,'Yes'], ['Penguin','Bird',2,'Yes'], 
                                  ['Moose','Mammal',4,'Yes'], ['Hamster','Mammal',4,'No']]

def test_file_not_found():
    result = combine_csv.read_first_line('non_existent_file.csv')
    assert result == "Error: The file 'non_existent_file.csv' was not found."

    result = combine_csv.read_file('non_existent_file.csv')
    assert result == "Error: The file 'non_existent_file.csv' was not found."

def test_empty_file(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("")
    result = combine_csv.read_first_line(str(file))
    assert result == f"Error: The file '{file}' is empty."

    result = combine_csv.read_file(str(file))
    assert result == f"Error: The file '{file}' is empty."

def test_compare_headers():
    header1 = combine_csv.read_first_line('sample_csv_1.csv')
    header2 = combine_csv.read_first_line('sample_csv_2.csv')
    assert combine_csv.compare_headers(header1, header2) is None

def test_combine_csvs():
    df = combine_csv.combine_csvs('sample_csv_1.csv', 'sample_csv_2.csv')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (11, 4)
    assert list(df.columns) == ['Animal', 'Class', 'Legs', 'Predator']
    assert df.values.tolist() == [['Orca','Mammal',0,'Yes'], ['Butterfly','Invertebrate',6,'No'], 
                                  ['Snake','Reptile',0,'Yes'], ['Penguin','Bird',2,'Yes'], 
                                  ['Moose','Mammal',4,'Yes'], ['Hamster','Mammal',4,'No'],
                                  ['Frog','Amphibian',4,'Yes'], ['Starfish','Invertebrate',5,'No'], 
                                  ['Duck','Bird',2,'No'], ['Bass','Fish',0,'Yes'], ['Lion','Mammal',4,'Yes']]

def test_check_output_file():
    df = combine_csv.combine_csvs('sample_csv_1.csv', 'sample_csv_2.csv')
    output = pd.read_csv("combined_file.csv")
    assert output.equals(df)

if __name__ == '__main__':
    pytest.main()
