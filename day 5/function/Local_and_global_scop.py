# this is global variable
balance = 3000

def buy_things(item, price):
    
    #this is local variable 
    # you can access only global variable but you can not modify it in a function
    # if you want to modify global variable or use global variable in a function you have to use global keyword 
    
    # print(balance)  -- this going to run with error
    # balance = 1000  -- this going to run with error
    global balance 
    balance =  balance - price
    print(f'after buying {item} ' , balance)
    
buy_things('sun_glasses',1000)
print('global balance : ' , balance)

