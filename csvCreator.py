import sys
import csv
import os
from datetime import datetime
import random
import string

def getCurrentDateAndTime():
	now = datetime.now()
	dateString = now.strftime("%Y-%m-%d-%H_%M_%S")
	return dateString

def generateRandomNumbers(rows):
	randomNumbers = [random.randint(1, 10000) for _i in range(rows)]
	return randomNumbers

def generateSingleRandomString():
	letters = string.ascii_lowercase + string.ascii_uppercase
	return ''.join(random.choice(letters) for i in range(10))

def generateMultipleRandomStrings(rows):
	randomStrings = [generateSingleRandomString() for _i in range(rows)]
	return randomStrings

def writeRandomDataToCsvFile(column, output_path, fileName, rows):
	with open(fileName, 'w', newline = '') as outcsv:
		writer = csv.writer(outcsv)
		writer.writerow([entry[0] for entry in column])
		dataTypes = [entry[1] for entry in column]
		
		# Append random strings and integer based on the datatypes of the columns
		randomData = []
		for dataType in dataTypes:
			if (dataType == 'string'):
				randomStrings = generateMultipleRandomStrings(rows)
				randomData.append(randomStrings)
			else:
				randomNumbers = generateRandomNumbers(rows)
				randomData.append(randomNumbers)
		
		# Use zip function to write rows of the data under appropriate columns
		writer.writerows(zip(*randomData))

def csvCreator(column, rows = 50, output_path = "present working directory"):
	# filename is generated with current date and time in the given format
	fileName = getCurrentDateAndTime() + ".csv"
	
	# If output_path is left empty by user, save CSV file in the current working directory
	if (output_path == "present working directory"):
		writeRandomDataToCsvFile(column, output_path, fileName, rows)
	else:
	# create new directory and save csv file within it
		output_path = validateAndReturnOutputPathIfCorrect(output_path)
		writeRandomDataToCsvFile(column, output_path, fileName, rows)

def getNumberofRowsFromUser():
	numberOfRows = None
	rows = input("Please enter the number of rows in the CSV file: ")
	
	# If user input is not empty, check if it is a number, otherwise print error message and exit
	if (rows.strip() != ''):
		try:
			numberOfRows = int(rows)
		except ValueError:
			print ("Please enter a valid integer for this choice!")
			sys.exit()
			
	return numberOfRows

def getDirectoryToSaveCsvFile():
	directory = input("Please enter the directory you want to save the CSV file to: ")
	return directory.strip()

def getColumnNamesOfCsvFile():
	print ("Column names of the CSV file should be in the format columnName, Type where Type is either a string or integer")
	columnInfo = input("Please enter the column names in the specified format columnName, Type: ")
	columns = columnInfo.split(",")
	
	# remove whitespace from user inputs 
	result = list(map(str.strip, columns))

	columns = validateAndReturnColumnInputIfCorrect(result)
	return columns

def validateAndReturnOutputPathIfCorrect(output_path):
	# if directory does not exist, make a directory with name output_path in the current working directory
	if not os.path.exists(output_path):
		try:
			os.makedirs(output_path)
		except FileNotFoundError:
			print ("Please enter a valid directory path in this server!")
			sys.exit()
	os.chdir(output_path)
	return output_path	

def validateAndReturnColumnInputIfCorrect(columnInfo):
	try:
		# Get tuples of columns from the user input if entered correctly
		columns = [(columnInfo[i], columnInfo[i+1]) for i in range(0, len(columnInfo), 2)]
	except (ValueError, IndexError):
		print("Please enter column names in specified format!")
		sys.exit()		

	for tuples in columns:
		# checks if second element of the column tuples is either a string or integer
		if tuples[1].lower() not in ("integer", "string"):
			print ("Please enter column type as either 'string' or 'integer'!")
			sys.exit()
	return columns

def main():
	# Return user input after validation
	numberOfRows = getNumberofRowsFromUser()
	directory = getDirectoryToSaveCsvFile()
	columns = getColumnNamesOfCsvFile()

	if (numberOfRows and directory and columns):
		csvCreator(columns, numberOfRows, directory)
	elif (numberOfRows and columns):
		csvCreator(columns, numberOfRows)
	elif (directory and columns):
		csvCreator(columns, directory)
	else:
		csvCreator(columns)

if __name__ == "__main__":
	main()	