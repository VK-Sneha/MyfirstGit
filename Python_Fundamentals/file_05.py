def amount_deposit(account_balance, amount):
    if account_balance <= 500:
        account_balance = account_balance + amount
        return account_balance 
        
   # else:
    #    print("you have minimum balance of rupees =", account_balance)

deposit = amount_deposit(400, 400)

if deposit >= 800:
    print("nothing to see")

else:
    print("we need to make a deposit")
