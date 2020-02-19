# CSV Creator

## Requirements
- [Python 3.7](https://www.python.org/downloads/)

## Running the Application

- To run the application, clone this repository and navigate to the directory that contains the csvCreator.py file on the command line
- Type python csvCreator.py and hit enter

## User Inputs

- The program will prompt you to enter 3 inputs.
- The first will prompt you to enter the number of rows you want to create in the CSV file. Please enter an integer value for this option. If other values are provided, the program will exit with a message informing you about the usage. If left empty, default value of 50 will be used.
- The second option will prompt you to enter the directory name where you want to save the CSV file. If invalid characters are used, an error message will be shown and the application will exit. If left empty, the CSV file will be saved in the current directory itself.
- The third option will prompt you to enter the column names you want in the CSV. This option is **mandatory** and will require at least one input in the form of columnName, type. 'Type' can only take the values of either 'integer' or 'string'. Other values will cause the program to exit. To enter multiple values, just enter the next values of columnName, type after the first and so on.
- For example, entering name, string, age, integer will create 2 columns 'name' and 'age'.
- name, int, age, str will be an invalid input because the type has to be 'integer' or 'string'
- Only entering columnName without its type will be an invalid output as well.
