"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

# build list of all calls made from a bangalore number
calls_from_bangalore = []
for call in calls:
    if call[0][:5] == '(080)':
        calls_from_bangalore.append(call[:2])


# extract unique numbers called from bangalore
unique_numbers_called_from_bangalore = set()
for call in calls_from_bangalore:
    unique_numbers_called_from_bangalore.add(call[1])


# initialise set to store final results
unique_area_codes_and_mobile_prefixes = set()
for number in unique_numbers_called_from_bangalore:
    if '(' in number and ')' in number: # checks for fixed lines
        end_index = number.index(')')
        unique_area_codes_and_mobile_prefixes.add(number[:end_index + 1])
    elif ' ' in number: # checks for space => mobile phone number
        unique_area_codes_and_mobile_prefixes.add(number[:4])
    elif number[:3] == '140': # checks for telemarketers
        unique_area_codes_and_mobile_prefixes.add(number[:3])


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
total_num_calls_made_from_bangalore = len(calls_from_bangalore)

calls_to_bangalore_from_bangalore = []
for call in calls_from_bangalore:
    if call[1][:5] == '(080)':
        calls_to_bangalore_from_bangalore.append(call[1])


num_calls_made_from_bangalore_to_bangalore = len(calls_to_bangalore_from_bangalore)
percentage_result = num_calls_made_from_bangalore_to_bangalore / total_num_calls_made_from_bangalore * 100


if __name__ == '__main__':
    print("The numbers called by people in Bangalore have codes:")
    for code in unique_area_codes_and_mobile_prefixes:
        print(code)
    print(f"{round(percentage_result,1)} percent of calls from fixed lines in Bangalore")
    print("are calls to other fixed lines in Bangalore.")
