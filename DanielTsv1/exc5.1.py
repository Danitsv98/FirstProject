current_payment=int(input("Enter your current month sallary : "))
percentage=int(input("Enter your percantage increase : "))
percentage2=float((percentage+100)/100)
new_payment=float(current_payment*percentage2)
print("your new monthly sallary is:",new_payment)

