#quiz07b.py

presidentsData = '''
order,firstName,middeName,lastName,birthState,birthYear,birthMonth,birthDay
1,"George","","Washington","Virginia",1722,2,22
2,"John","","Adams,"Massachusetts",1735,10,30
3,"Thomas","","Jefferson","Virginia",1743,4,13
4,"James","","Madison","Virginia",1751,3,16
5,"James","","Monroe","Virginia",1758,4,28
6,"John","Quincy","Adams","Massachusetts",1767,11,7
'''

print(presidentsData)
print('-' * 30)

presidentsList = presidentsData.split("\n")
print(presidentsList)
print('-' * 30)

presidents = []
for line in presidentsList:
    row = line.split(',')
    if row[0].isalpha() or len(row) != 8:
        continue
    rec = {}
    rec['order'] = int(line[0])
    rec['name'] = {'firstName':row[1].replace('"',''), 'middleName':row[2].replace('"',''),'lastName':row[3].replace('"','')}
    rec['birthState'] = row[4].replace('"','')
    rec['birthDay'] = [int(row[5]), int(row[6]), int(row[7])]
    presidents.append(rec)
print('-' * 30)

for p in presidents:
    for key, value in p.items():
        print("%s => %s" % (key, value))
    print()
print('-' * 30)

print(presidents)
#month = {
#        1:'January',
#        2:'February',
#        3:'March',
#        4:'April',
#        5:'May',
#        6:'June',
#        7:'July',
#        8:'August',
#        9:'September',
#        10:'October',
#        11:'November',
#        12:'December'
#        }
#presidents = []
#presidents.append(
#        {'order': 1,
#        'name':   {'firstName': 'George', 'middleName': '', 'lastName': 'Washington'},
#        'birthState': 'Virginia',
#        'birthDay': [1722,2,22] })
#
#presidents.append(
#        {'order': 2,
#        'name':   {'firstName': 'John', 'middleName': '', 'lastName': 'Adams'},
#        'birthState': 'Massachusetts',
#        'birthDay': [1735,10,30] })
#presidents.append(
#        {'order': 3,
#        'name':   {'firstName': 'Thomas', 'middleName': '', 'lastName': 'Jefferson'},
#        'birthState': 'Virginia',
#        'birthDay': [1743,4,13] })
#presidents.append(
#        {'order': 4,
#        'name':   {'firstName': 'James', 'middleName': '', 'lastName': 'Madison'},
#        'birthState': 'Virginia',
#        'birthDay': [1751,3,16] })
#presidents.append(
#        {'order': 5,
#        'name':   {'firstName': 'James', 'middleName': '', 'lastName': 'Monroe'},
#        'birthState': 'Virginia',
#        'birthDay': [1758,4,28] })
#presidents.append(
#        {'order': 6,
#        'name':   {'firstName': 'John', 'middleName': 'Quincy', 'lastName': 'Adams'},
#        'birthState': 'Massachusetts',
#        'birthDay': [1767,11,7] })
#
#print('--------------------')
#print(presidents[0]['name']['firstName'], presidents[0]['birthDay'][0], month[presidents[0]['birthDay'][1]])
#print('--------------------')
#for p in presidents:
#    dob = "%s %s, %s" % (presidents[0]['birthDay'][0], month[presidents[0]['birthDay'][1]], presidents[0]['birthDay'][2])
#    print(p)
##print("%s %s %s was born on %g" % (presidents[0]['name']['firstName'],presidents[0]['name']['middleName'],presidents[0]['name']['lastName'],presidents[0]['birthDay'][0]))
#print('---------------here-----')
#for i in range(len(presidents)):
#    #print(presidents[i]['name']['firstName'], presidents[i]['name']['middleName'], presidents[i]['name']['lastName'], month[presidents[i]['birthDay'][1]], presidents[i]['birthDay'][0],  presidents[i]['birthDay'][0])
#    dob = "%s %s, %s" % (month[presidents[i]['birthDay'][1]], presidents[i]['birthDay'][2], presidents[i]['birthDay'][0])
#    name = "%s %s %s" % (presidents[i]['name']['firstName'], presidents[i]['name']['middleName'], presidents[i]['name']['lastName'])
#    print("President %d, %s, from %s, was born on %s" % ( presidents[i]['order'], name, presidents[i]['birthState'], dob))
##print("%s %s %s was born on %g" % (presidents[0]['name']['firstName'],presidents[0]['name']['middleName'],presidents[0]['name']['lastName'],presidents[0]['birthDay'][0]))
