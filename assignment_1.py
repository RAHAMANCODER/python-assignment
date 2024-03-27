Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list built in function
list=[ 'banana' ,'graps' ,'apple']
#append
list.append("lemon")
print(list)
"""
['banana', 'graps', 'apple', 'lemon']
"""
#copy
fruits=list.copy()
print(fruits)
"""
['banana', 'graps', 'apple', 'lemon']
"""
"""
#count
fruits.count()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fruits.count()
TypeError: list.count() takes exactly one argument (0 given)
list.count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list.count()
TypeError: list.count() takes exactly one argument (0 given)
fruits.count(apple)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fruits.count(apple)
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
fruits.count('apple')
1
"""
#extend
vegetables=['onion','carrot','ginger']
fruits.extend(vegetables)
print(fruits)
"""
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
"""
"""
#index
fruits.index()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fruits.index()
TypeError: index expected at least 1 argument, got 0
"""
fruits.index('ginger')
#6
#insert
fruits.insert(1,'guava')
print(fruits)
"""
['banana', 'guava', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'guava', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'guava', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
"""
"""
#pop
fruits.pop('guava')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fruits.pop('guava')
TypeError: 'str' object cannot be interpreted as an integer
"""
fruits.pop(1)
#'guava'
print(fruits)
"""
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
"""
#reverse
fruits.reverse()
print(fruits)
"""
['ginger', 'carrot', 'onion', 'lemon', 'apple', 'graps', 'banana']
"""
print(fruits[::-1])
"""
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
['banana', 'graps', 'apple', 'lemon', 'onion', 'carrot', 'ginger']
"""
#sort
fruits.sort()
print(fruits)
"""
['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']
['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']
['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']

['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']
['apple', 'banana', 'carrot', 'ginger', 'graps', 'lemon', 'onion']
"""
#clear
fruits.clear()
print(fruits)
# []
print(list)
"""
['banana', 'graps', 'apple', 'lemon']
"""

tuple=('dhoni','virot','sachin','rohit sharma')
print(tuple)
"""
('dhoni', 'virot', 'sachin', 'rohit sharma')
"""
"""
players=tuple.copy()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    players=tuple.copy()
AttributeError: 'tuple' object has no attribute 'copy'
players=tuple.copy
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    players=tuple.copy
AttributeError: 'tuple' object has no attribute 'copy'
"""
#count
tuple.count('dhoni')
# 1
#index
"""
tupke.index('sachin')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    tupke.index('sachin')
NameError: name 'tupke' is not defined. Did you mean: 'tuple'?
NameError: name 'tupke' is not defined. Did you mean: 'tuple'?
SyntaxError: invalid syntax. Perhaps you forgot a comma?
tuple.index('sachin')
2
"""
"""
#dict
dict={
    'car':' BMW"
    
SyntaxError: unterminated string literal (detected at line 2)
tuple.index('sachin')
2
"""

tuple.index('sachin')
#2
#dict
dict={
    'car':' BMW'
}
# 2
#dict
bike={
    "brand" : ["splender", "royel enfeild", "pulser"],
    "speed" : ["100 cc" , "220 cc" ,"150 cc"],
    "year" :[ 2020,2021,2022],
    "color" :[ "red","yellow","black"]
    }
    

#dict
bike={
    "brand" : ["splender", "royel enfeild", "pulser"],
    "speed" : ["100 cc" , "220 cc" ,"150 cc"],
    "year" :[ 2020,2021,2022],
    "color" :[ "red","yellow","black"]
    }
    
print(bike)
    
"""
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
"""
#copy
    
bike 1=bike.copy
    

print(bike)
 """   
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
"""
x=bike.copy()
    
print(x)
 """   
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
    
{'brand': ['splender', 'royel enfeild', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
"""


#dict_items([('brand', ['splender', 'royel enfeild', 'pulser']), ('speed', ['100 cc', '220 cc', '150 cc']), ('year', [2020, 2021, 2022]), ('color', ['red', 'yellow', 'black'])])



bike.get("brand")
    
['splender', 'royel enfeild', 'pulser']


SyntaxError: invalid syntax. Perhaps you forgot a comma?
bike.update({ "brand" : ["honda", "royel enfield" , "pulser" ]})
print(bike)
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
bike.update({ "brand" : ["honda", "royel enfield" , "pulser" ]})
print(bike)
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022], 'color': ['red', 'yellow', 'black']}
bike.fromkeys()

bike.values()
dict_values([['honda', 'royel enfield', 'pulser'], ['100 cc', '220 cc', '150 cc'], [2020, 2021, 2022], ['red', 'yellow', 'black']])

bike.pop("color")

#['red', 'yellow', 'black']
print(bike)
"""
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022]}
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022]}
{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc'], 'year': [2020, 2021, 2022]}
"""


bike.popitem()\
  
#('year', [2020, 2021, 2022])

print(bike)
#{'brand': ['honda', 'royel enfield', 'pulser'], 'speed': ['100 cc', '220 cc', '150 cc']}
bike.popitem()
#('speed', ['100 cc', '220 cc', '150 cc'])
print(bike)
"""
{'brand': ['honda', 'royel enfield', 'pulser']}
{'brand': ['honda', 'royel enfield', 'pulser']}
{'brand': ['honda', 'royel enfield', 'pulser']}
"""
bike.clear()
print(bike)
#{}
