#LIST BULID IN FUNCTION
list=[ 'banana' ,'graps' ,'apple']

#append
list.append("lemon")
print(list)

#copy
fruits=list.copy()
print(fruits)

#count
fruits.count('apple')

#extend
vegetables=['onion','carrot','ginger']
fruits.extend(vegetables)
print(fruits)

fruits.index('ginger')
print(fruits)

#insert
fruits.insert(1,'guava')
print(fruits)

#pop
fruits.pop(1)
print(fruits)

#reverse
fruits.reverse()
print(fruits)
print(fruits[::-1])
#sort
fruits.sort()
print(fruits)

#clear
fruits.clear()
print(fruits)
print(list)

"""
['banana', 'graps', 'apple', 'lemon']
['banana', 'graps', 'apple', 'lemon']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'guava', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['ginger', 'carrot', 'onion', 'lemon', 'apple', 'graps', 'banana']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']
[]
['banana', 'graps', 'apple', 'lemon']
"""

#TUBLE BUILD IN FUNCTION
tuple=('dhoni','virot','sachin','rohit sharma')
print(tuple)


#count
tuple.count('dhoni')

#indeX
tuple.index('sachin')

"""
['banana', 'graps', 'apple', 'lemon']
('dhoni', 'virot', 'sachin', 'rohit sharma')
"""
    
#DICT BUILD IN FUNCTION
#dict
bike={
    "brand" : ["splender", "royel enfeild", "pulser"],
    "speed" : ["100 cc" , "220 cc" ,"150 cc"],
    "year" :[ 2020,2021,2022],
    "color" :[ "red","yellow","black"]
    }
    
print(bike)

#copy
    
bike_1=bike.copy
print(bike)

x=bike.copy()  
print(x)


bike.get("brand")

bike.update({ "brand" : ["honda", "royel enfield" , "pulser" ]})
print(bike)

bike.values()

bike.pop("color")
print(bike)

bike.popitem()
print(bike)

bike.clear()
print(bike)

"""
'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022]}
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc']}
{'brand': ['honda', 'royel enfield', 'pulser']}
{}
"""