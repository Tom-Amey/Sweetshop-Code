import random
import time
#import date
# loop 1 is loop for type of action(s)
def loop_check(a):
    loop = True # not included in code as scope is local
    while loop:
        carry_on = input('Would you like to leave our website (yes/no)').lower()
        if carry_on == "yes":
            a = False 
            loop = False 
        elif carry_on == "no":
            print('goodbye :)')
            a = a 
            loop = False
        else:
            print('Try again')
    return a

# Checks if loop is to be continued

print('Welcome to the Sweetshop!')
sweet_list = { 'Cola bottles' :10,
              'gold bears' :5,
              'brainlickers' :50,
              'Refreshers' :20,
              'Fruit salads' :15,
              'black jacks' :5,
              'dip dabs' :20,
              'jelly babies' :5,
              'jelly beans' :2,
              'strawberry laces' :5,
              'bubblegum bottles' :5,
              'Marshmallows' :5,
              'Teeth and lips' :10,
              'lovehearts' :5,
              'drumsticks' :20,
               'haribos' :10}
# states prices
user_cost = 0
stock_refill = False
time.sleep(1)
loop_1 = True 
while loop_1:
    option_one = input('What would you like to do? (place an order / contact us / employee access)').lower()
    if option_one == 'place an order':
        loop_2 = True
        while loop_2:
            print('choose an option. . .')
            time.sleep(1)	
            print('Sweet bundles:')
            print('-----------')
            print('1. suprise me')
            print('2. Blue package')
            print('3. Strawberry delight')
            print('4. pick n mix')
            print('5. jars of sweets')
            time.sleep(1)
            choice_menu = input('Pick a number (1,2,3,4,5)').lower()
            sweet_list = []
            price = 0 
            if choice_menu == '1':
                print('Suprise me has been added to your basket')
                print(random.choice(list(sweet_list.keys())))
                sweet_list.append(sweet)
                price += (sweet_list.get(sweet))    
                    
                    
            elif choice_menu == '2':
                print('Blue package has been added to your basket')
            elif choice_menu == '3':
                print('Strawberry delight has been added to your basket')
            elif choice_menu == '4':
                print('Pick n mix has been added to your basket')
            elif choice_menu == '5':
                pass
            else:
                print('Invalid, please try again')
	
    elif option_one == 'contact us':
        print('Our conact details:')
        print('-------------------')
        print('25 Jubilee Drive')
        print('Loughborough')
        print('Leicestershire')
        print('LE11 5TX')
        print('United Kingdom')
        print('Phone: 0330 2020902 Mon-Fri 8:30am - 5:00pm')
        print('Email: support@uksweets.com')
        time.sleep(3)
        end_prgram = input('Would you like to continue or leave the website? (yes/no)').lower()
        if end_program == 'yes' or 'y':
            loop_1 = False
        elif end_program == 'no' or 'n':
            loop_1 = True 
        else:
            print('Invalid response')
    
    elif option_one == 'employee access':
        employee = input('Would you like to view stock or sign in?').lower()
        if employee == 'stock':
            pass
        elif employee == 'sign in':
            pass
        else:
            print('Sorry! Invalid response')
            time.sleep(1)
            print('Try again')
        
    else:
        print('Sorry! Invalid response')
        time.sleep(1)
        print('Try again')
        
                  
                  
              
            
