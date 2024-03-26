#creating the class
class Calc:
    def __init__(self,num_a,num_b) :  #__init__ is instance method(newly create the objects)
      self.num_a=num_a
      self.num_b=num_b
      
    def addition(self):
      return self.num_a+self.num_b
    
    def subtraction(self):
      return self.num_a-self.num_b 
    
    def multiply(self):
      return self.num_a*self.num_b
    
    def divition(self):
      return self.num_a/self.num_b
    
value=Calc(2,4)  
print(value.addition(),"add")  
print(value.subtraction(),"sub")  
print(value.multiply(),"mul")  
print(value.divition(),"div")  



"""
6 add
-2 sub
8 mul
0.5 div
"""

#another example of class
class MyName:
  def __init__(self,name,age):
     self.name=name
     self.age=age
     
details=MyName("rahaman",19)
print(details.name)
print(details.age)


"""     
rahaman
19
"""



#creating class in employee details
class Employee:
    def __init__(self,name,age,company,number,salary,working):
       self.name=name
       self.age=age
       self.company=company
       self.number=number
       self.salary=salary
       self.working=working
employee_details=Employee("rahaman",19,"zoho",6369966919,50000,"fullstack developer") 
print(employee_details.name,"=emp_name")    
print(employee_details.age,"=emp_age")    
print(employee_details.company,"=emp_company")    
print(employee_details.salary,"=emp_salary")    
print(employee_details.working,"=emp_work")     

"""
19 =emp_age
zoho =emp_company
50000 =emp_salary
fullstack developer =emp_work
variable x is not defined 
"""

#create the try and expect
try: #try block for code the error
    print(x)
except: #except block is handled the error
   print("variable x is not defined")
   


try:
  numerator=int(input("enter the No:"))
  denumerator=int(input("enter the No:"))
  result=numerator/denumerator
  print(result)
except:
  print("zero divition error") 
  
  print("program ends")

"""
enter the No:10
enter the No:0
zero divition error
program ends 
"""

try:
  my_list=[1,2,3]  
  value=int(input("enter the index val:"))
  print(my_list[value])
except IndexError:
  print("cannot find the value for list")
  """
cannot find the value for list
"""


def main():
       date=100
       while date !=0 :
         date=int(input("enter the date 1-7:"))
       match date:
         case 1:
           print("monday")
         case 2:
           print("tuesday")
         case 3:
           print("wednesday")
         case 4:
           print("thursday")
         case 5:
           print("friday")
         case 6:
           print("saterday")
         case 7:
           print("invalid date")
           
          
#anothe example of match case
grade =1
match grade:
  case 1:
    print("very good marks")   
  case 2:
    print("good marks")      
  case 3:
    print("okey this mark")  
  case 4:
    print("improve the marks")
  case 5:
    print("bad marks")        
                      
