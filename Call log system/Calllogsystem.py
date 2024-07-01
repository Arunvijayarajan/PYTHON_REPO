def find_call_log(call_log,phone_number):
    found_entries=set()
    for entry in call_log:
        if call_log[entry]==phone_number:
            found_entries.add(entry)
    return found_entries
call_log={
    'john doe':'123-456-7890',
    'jane smith':'987-645-3210',
    'alice johnson':'555-123-4567',
    'bob brown':'123-456-7890',
    'charli davies':'555-123-4567'
    }
phone_number='123-456-7890'
found_entries=find_call_log(call_log,phone_number)
if found_entries:
    print(f"call log entries for phone number{phone_number}:")
    for entry in found_entries:
        print(entry)
else:
    print(f"no call log entries found for phone number{phone_number}")
