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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def check_if_number_sends_texts(number_string):
    for text in texts:
        if text[0] == number_string:
            return True
    return False


def check_if_number_receives_texts(number_string):
    for text in texts:
        if text[1] == number_string:
            return True
    return False


def check_if_number_receives_calls(number_string):
    for call in calls:
        if call[1] == number_string:
            return True
    return False


# numbers that make calls
callers = set()
for call in calls:
    callers.add(call[0])


# the following could have been done more efficiently, but this approach enables us
# to inspect behavior of suspected telemarketers more closely

# dictionary of callers with various scores initialised to False
caller_metrics = {}
for caller in callers:
    caller_metrics[caller] = {'sends_texts': False,
                              'receives_texts': False,
                              'receives_calls': False
                              }

potential_telemarketers = set()

for caller in caller_metrics.items():
    caller[1]['sends_texts'] = check_if_number_sends_texts(caller[0])
    caller[1]['receives_texts'] = check_if_number_receives_texts(caller[0])
    caller[1]['receives_calls'] = check_if_number_receives_calls(caller[0])

    if (caller[1]['sends_texts'] == False
            and caller[1]['receives_texts'] == False
            and caller[1]['receives_calls'] == False):
        potential_telemarketers.add(caller[0])


if __name__ == '__main__':
    print("These numbers could be telemarketers:")
    for number in potential_telemarketers:
        print(number)

