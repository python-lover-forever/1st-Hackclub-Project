while True :
  print("Welcome to the ATM system")
  d = {"ahmed": 1234, "shams": 12345}
  b= 1000
  y = input("please enter your username : ")
  if y in d :
    print("Welcome",y)
    z = int(input("please enter your password : "))
    if z == d[y] :
      print("\nyou are logged in")
      x = input("\nwhat do you want to do ? 1.check balance 2.withdraw 3.deposit 4.exit :")
      if x == "1" :
        print("\nyour balance is " , b)
      elif x == "2" :
        a = int(input("\nplease enter the amount you want to withdraw : "))
        if a > b :
          print("\nyou don't have enough balance (go find a donation for your poor self (joking) )")
        if a <= b :
          b = b - a
          print("\nyour new balance is " , b)
      elif x == "3" :
        c = int(input("\nplease enter the amount you want to deposit : "))
        b = b + c
        print("\nyour new balance is " , b)
      elif x == "4" :
        print("\nthank you for using Atm System Goodbye")
        break
    else :
      print("\nWrong Password Please try again")
  else:
    print("\nwrong username Please try again")
  