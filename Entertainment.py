#ENTERTAINMENT

print("seats   :  [   Stalls-Rs:625/-,Circle-Rs:750/- , Upper Class-Rs:850/- , Box-Rs:1000/-  ]")

seat=(input("select the seat : "))

print("payment  :  [  Cash   ,  Credit card ]")

Payment_mode=input("select the Payment mode  : ")

seats={"Stalls":625,"Circle":750,"Upper Class":850,"BOx":1000}

payment={"Cash":10,"Credit card":5}

print("Cost of Ticket  : ",(seats[seat]*(1-(payment[Payment_mode]/100))))
