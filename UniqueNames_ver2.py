#Take inputted file and delete lines with duplicate 
#first and last customer names. 
#The names must be in separate
#columns, either Col#n.FirstName and Col#n+1.LastName,
#or Col#n.LastName and Col#n+1.FirstName (see line 31).
#Input file must be a tab-separated spreadsheet formatted
#in UTF-8.

#Instructions
print('===================================')
print('Your spreadsheet must be a text file, tab-separated, UTF-8 format, and in the same directory as this program.')
print('Hit CTRL and C to exit at anytime.')
print('===================================')

#Ask user for input spreadsheet
while True:
	try:
		txt = input('Name of file to delete duplicates (include .txt ext): ')
		f = open(txt, 'r')
		break
	except IOError:
		print('File not found.')
#Read spreadsheet into 2D array
arr1 = []
for line in f.readlines():
	arr1.append([])
	for i in line.split():
		arr1[-1].append(str(i))
f.close()

#Make copy of array to be edited
arr2 = arr1
###Insert the line below to set a permanent first column
#col1 = (integer)
###End supplementary code
while True:
	try:	
		col1 = int(input('What number column is the first to contain names? Start counting from 0: '))
		break
	except ValueError:
		print('Please enter an integer. ')
#Insert line below to set a permanent second column
#col2 = (integer)
##End supplementary code
col2 = col1+1
###Insert lines below if the names are not in consecutive columns
#while True:
#	try:
#		col2 = int(input('What number column is the second to contain names?: '))
#		break
#	except ValueError:
#		print('Please enter an integer. ')
###Then, you may comment out line 30 for efficiency
###End supplementary code

#Find and delete duplicate customer names and rows
i = 0
while i < len(arr1):
	j = i + 1
	while j < len(arr2):
		if arr1[i][col1] == arr2[j][col1]:
			if arr1[i][col2] == arr2[j][col2]:
				del arr2[j]
			else:
				j += 1
		else:
			j += 1
	j = 0
	i += 1

#Create new file with unique customers only	 
nameoffile = 'UniqueNames_'+txt
f = open(nameoffile, 'w')
for i in range(0,len(arr1)):
	for j in range(0,len(arr1[2])):
		f.write(arr1[i][j])
		f.write('\t')
	if i == len(arr1)-1:
		break
	else:
		f.write('\n')
f.close()
print('A new file with unique first and last names, '+nameoffile+',  has been created.')
print('Operation complete.')
