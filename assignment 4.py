from random import randint

class BankingSystem:
    def __init__(self):
        self.creaditcard_number=[]
        self.pin_number=[]
        
    def welcome_screen(self):
        print(
            "1.crearting an account\n"
            "2.login an account\n"
            "0.Exit\n"
        )    
        
        dept_selection=str(input("Enter your choice:"))
        if dept_selection =="1":
            self.create_account()
        if dept_selection =="2":
            self.login_account()     
        if dept_selection =="0":
            return "Bye!" 
    
    def create_account(self):
        creadit_card_number_gen=format(randint(0000000000,999999999))
        pin_number_gen=format(randint(0000,9999))
        
        self.creaditcard_number.append(creadit_card_number_gen)   
        self.pin_number.append(pin_number_gen)
        
        print("hello")
        print("your creadit_card number is successfully created")
        print("your creadit_card number:",creadit_card_number_gen)
        print("your pin number",pin_number_gen)
        self.welcome_screen()
        
    def login_account(self):
         print("Enter your creadit card number:")
         enter_card_number=int(input())
         print("Enter your pin number: ")
         enter_pin_number=int(input())
         
         if enter_card_number in self.creaditcard_number and enter_pin_number in self.pin_number:
             
             print("your account successfully created")
         else:
             print(self.creaditcard_number,self.pin_number)
             print("wrong account number")   

         self.welcome_screen()
print(BankingSystem().welcome_screen())

"""
1.crearting an account
2.login an account
0.Exit

Enter your choice:1
hello
your creadit_card number is successfully created
your creadit_card number: 909545914
your pin number 3312
1.crearting an account
2.login an account
0.Exit

Enter your choice:2
Enter your creadit card number:
 909545914
Enter your pin number:
 3312
wrong account number
"""



  
        