import csv

# Open the CSV file
with open('file.csv', newline='') as csvfile:
# Create a CSV reader object
reader = csv.reader(csvfile, delimiter=',')

# Loop through each row in the CSV file and print it to the console
for row in reader:
print(row)