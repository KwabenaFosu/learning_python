print("------- MTN MoMo Charge Calculator -------")
amount = input("Enter amount you wish to transfer: " )
print(f"Calculating momo charges for : {amount} cedis")
amount = int(amount)
#print(type(amount))
def mtn_fee(amount):
    if amount <= 50:
       return 0.38
    if amount <= 1000:
       return round(amount * 0.0075,2)
    else:
       return 7.5

    
print(f'mtn fee is: {mtn_fee(amount)} cedis')

def elevy(amount):         #Charged only after 100 cedis
    if amount <= 100:
       return 0.0
    elif amount > 100:
       return amount * 0.01
    
print (f'E-levy charge is: {elevy(amount)} cedis')

total_charge = mtn_fee(amount) + elevy(amount)
print(f'Total charges for the transaction is: {total_charge} cedis')

total_transaction = round(amount + mtn_fee(amount) + elevy(amount),2)
print(f'Total transaction fee is : {total_transaction} cedis')
        
