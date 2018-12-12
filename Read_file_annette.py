import csv
import numpy as np

file_name = "clinical.tsv"


race = 5
vital_status = 13
primary_diagnosis = 10
age_at_diagnosis = 12



with open(file_name) as f:
    reader = csv.reader(f, delimiter = "\t")
    master_list = list(reader)
    master_array = np.asarray(master_list)
number_of_cases = len(master_list) - 1


print "Total Number of patients in this clinical data set = ",number_of_cases

number_of_alive_patients = np.where(master_array[1:308,vital_status] == 'alive')
print "Number of Alive patients = ", len(number_of_alive_patients[0])

number_of_white_race = np.where(master_array[:,race] == 'white')
print "Number of white race", len(number_of_white_race[0])

number_of_white_race_with_age_info = np.where((master_array[:,race] == 'white') & (master_array[:,age_at_diagnosis] != '--'))

max_age_of_white = max((master_array[number_of_white_race_with_age_info[0],age_at_diagnosis]).astype(int))/365
min_age_of_white = min((master_array[number_of_white_race_with_age_info[0],age_at_diagnosis]).astype(int))/365

print "Age range (at time of diagnosis) of patients of White race are between ", min_age_of_white, " and ", max_age_of_white , "years"


primary_diagnosis_of_white = np.unique(master_array[number_of_white_race[0],primary_diagnosis])
number_of_primary_diagnosis_of_white = len(primary_diagnosis_of_white)

for i in primary_diagnosis_of_white:
    number_of_primary_diagnosis = float(len((np.where(master_array[:,primary_diagnosis] == i))[0]))
    percentage_of_primary_diagnosis = (number_of_primary_diagnosis/float(len(number_of_white_race[0])))*100.0
    print "Percentage of white patients with ", i," Primary diagnosis = ", percentage_of_primary_diagnosis, "%"







