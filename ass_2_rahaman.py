#creating a nested dictionary
details={'college':'Amcet','std_1':{'name':'Rahaman','roll_no':40,'marks':{'python':90, 'c':80,'sql':85}},
         'std_2':{'name':'Sam','roll_no':41,'marks':{'python':80, 'c':90,'sql':78}},
         'std_3':{'name':'Jon','roll_no':42,'marks':{'python':70, 'c':95,'sql':80}} }
print(details)

#print the specific details
print(details.get('college'))
print(details.get('std_1'))
print(details.get('std_2'))
print(details.get('std_3'))


#print the key value in nest dictionary
print(details.keys())

#print the values in nest dictionary
print(details.values())

"""
{'college': 'Amcet', 'std_1': {'name': 'Rahaman', 'roll_no': 40, 'marks': {'python': 90, 'c': 80, 'sql': 85}}, 'std_2': {'name': 'Sam', 'roll_no': 41, 'marks': {'python': 80, 'c': 90, 'sql': 78}}, 'std_3': {'name': 'Jon', 'roll_no': 42, 'marks': {'python': 70, 'c': 95, 'sql': 80}}}
Amcet
{'name': 'Rahaman', 'roll_no': 40, 'marks': {'python': 90, 'c': 80, 'sql': 85}}
{'name': 'Sam', 'roll_no': 41, 'marks': {'python': 80, 'c': 90, 'sql': 78}}
{'name': 'Jon', 'roll_no': 42, 'marks': {'python': 70, 'c': 95, 'sql': 80}}
dict_keys(['college', 'std_1', 'std_2', 'std_3'])
dict_values(['Amcet', {'name': 'Rahaman', 'roll_no': 40, 'marks': {'python': 90, 'c': 80, 'sql': 85}}, {'name': 'Sam', 'roll_no': 41, 'marks': {'python': 80, 'c': 90, 'sql': 78}}, {'name': 'Jon', 'roll_no': 42, 'marks': {'python': 70, 'c': 95, 'sql': 80}}])
"""

#creating the set using build in function
friends={'rahaman','dinesh','dhanush','deepak'}
print(friends)

#copying the set
set_1=friends.copy()
print(set_1)

#adding the set
friends.add('samsung')
print(friends)

#using the difference in set function
frd={'rahaman','dinesh','dhanush','jeeva'}
friends.difference(frd)
frd.difference(friends)


#using the difference_update
friends.difference_update(frd)
print(friends)


#using discard to remove the specific element in the set
courses={'python','sql','c++','fullstack developer'}
print(courses)

courses.discard('c++')
print(courses)

#getting the common element using the intersection in set
courses_1={'c++','python','sql','mangodb'}
courses.intersection(courses_1)

#intersection_update getting the common element and remove the other element
courses.intersection_update(courses_1)
print(courses)

#isdisjoint is true or false for no common element
courses.isdisjoint(courses_1)

#issuperset method()
courses.issuperset(courses_1)

#union using the adding the list
courses.union(courses_1)

#pop() using the delete to random element
courses.pop()

#remove() method is delete thee specific element
courses_1.remove('sql')
print(courses_1)

"""
{'deepak', 'dhanush', 'dinesh', 'rahaman'}
{'deepak', 'dhanush', 'dinesh', 'rahaman'}
{'dhanush', 'dinesh', 'samsung', 'rahaman', 'deepak'}
{'samsung', 'deepak'}
{'c++', 'fullstack developer', 'sql', 'python'}
{'fullstack developer', 'sql', 'python'}
{'sql', 'python'}
{'c++', 'mangodb', 'python'}
"""
#if elif else
num=int(input("enter the number:"))
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')
    
num=int(input("enter the number:"))
if num%2==0:
    print('even')
else:
    print('odd')
    
 #for loops   
for i in range(11):
    print(i)
        
for i in range(11):
    if i==5:
        break
    print(i)

for i in range(11):
    if i==5:
        continue
    else:
         print(i)
