# quiz07a.py

# initialize month dictionary
month = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
        }

#initialize presidents list
presidents = []
#append data to presidents list
presidents.append(
        {'order': 1,
        'name':   {'firstName': 'George', 'middleName': '', 'lastName': 'Washington'},
        'birthState': 'Virginia',
        'birthDay': [1722,2,22] })

presidents.append(
        {'order': 2,
        'name':   {'firstName': 'John', 'middleName': '', 'lastName': 'Adams'},
        'birthState': 'Massachusetts',
        'birthDay': [1735,10,30] })
presidents.append(
        {'order': 3,
        'name':   {'firstName': 'Thomas', 'middleName': '', 'lastName': 'Jefferson'},
        'birthState': 'Virginia',
        'birthDay': [1743,4,13] })
presidents.append(
        {'order': 4,
        'name':   {'firstName': 'James', 'middleName': '', 'lastName': 'Madison'},
        'birthState': 'Virginia',
        'birthDay': [1751,3,16] })
presidents.append(
        {'order': 5,
        'name':   {'firstName': 'James', 'middleName': '', 'lastName': 'Monroe'},
        'birthState': 'Virginia',
        'birthDay': [1758,4,28] })
presidents.append(
        {'order': 6,
        'name':   {'firstName': 'John', 'middleName': 'Quincy', 'lastName': 'Adams'},
        'birthState': 'Massachusetts',
        'birthDay': [1767,11,7] })

#print presidents in friendly user format
print('---------------here are the presidents-----------')
for i in range(len(presidents)):
    dob = "%s %s, %s" % (month[presidents[i]['birthDay'][1]], presidents[i]['birthDay'][2], presidents[i]['birthDay'][0])
    name = "%s %s %s" % (presidents[i]['name']['firstName'], presidents[i]['name']['middleName'], presidents[i]['name']['lastName'])
    print("President %d, %s, from %s, was born on %s" % ( presidents[i]['order'], name, presidents[i]['birthState'], dob))
