phones_db = {'25': {'None': 'Life:)'},
             '29': {'1': 'A1', '2': 'MTC', '3': 'A1', '5': 'MTC',
                    '6': 'A1', '7': 'MTC', '8': 'MTC', '9': 'A1'},
             '33': {'None': 'MTC'},
             '44': {'None': 'A1'}}
next_number = True

while next_number:
    result = {}
    success = None
    user_phone = input('Enter phone number: ')

    if len(user_phone) == 13:
        success = True
        if user_phone[0] == '+':
            success = True
            try:
                int(user_phone[1:])
                success = True
                if user_phone[1:4] == '375':
                    success = True
                    for key in phones_db:
                        if key == user_phone[4:6]:
                            result['success'] = True
                            result['phone'] = user_phone
                            for n in phones_db[key]:
                                if user_phone[6] == n:
                                    result['success'] = True
                                    result['operator'] = phones_db[key][n]
                                elif n == 'None':
                                    result['success'] = True
                                    result['operator'] = phones_db[key]['None']
                        try:
                            result['success']
                        except KeyError:
                            result['success'] = False
                            result['description'] = 'Operator code check not passed'
                else:
                    result['success'] = False
                    result['description'] = 'Country code check not passed'
            except TypeError:
                result['success'] = False
                result['description'] = 'it is not digits'
        else:
            result['success'] = False
            result['description'] = 'First symbol + not passed'
    else:
        result['success'] = False
        result['description'] = 'Len check not passed'

    print(result)
    if input('Would you like to check out another one? (Y / N): ').lower() == 'y':
        continue
    else:
        next_number = False
