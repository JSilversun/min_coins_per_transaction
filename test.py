from functools import reduce
from decimal import Decimal
def calculateExhange(amount, payment, denominations):
    exchange=payment-amount
    exchange_coins=[0 for i in range(0,len(denominations))]
    subtotal=0
    for d in range(0,len(denominations)):
        if denominations[d]<=(exchange-subtotal):
            exchange_coins[d]=(exchange-subtotal)/denominations[d]
            subtotal+=exchange_coins[d]*denominations[d]
    if subtotal<exchange:
        return None
    else:
        return exchange_coins
def recursive(current, subtotal):
    global denominations, amount, payment_coins
    for i in range(current,len(denominations)):
        current_max=((amount-subtotal)/denominations[i])+1
        for j in reversed(range(0, current_max+1)):
            payment_coins[i]=j
            subtotal+=payment_coins[i]*denominations[i]
            if subtotal>=amount:
                checkPayment(payment_coins)
            if i+1< len(denominations) and subtotal<amount:
                recursive(i+1, subtotal)
            subtotal-=payment_coins[i]*denominations[i]
def checkPayment(payment_coins):
    global min_coins, used_coins, amount
    total_per_coin=list(map(lambda x, y: x*y, payment_coins,denominations))
    total_payment=reduce((lambda x,y:x+y),total_per_coin)
    total_payment_coins=reduce((lambda x,y:x+y),payment_coins)
    exchange_coins=calculateExhange(amount, total_payment, denominations)
    min_reached=False
    if exchange_coins is not None:
        total_exchange_coins=reduce((lambda x,y:x+y),exchange_coins)
        used_coins=total_payment_coins+total_exchange_coins
        if used_coins<min_coins:
            print(list(map(lambda x, y: str(x)+" "+str(y), payment_coins,denominations)))
            print(list(map(lambda x, y: str(x)+" "+str(y), exchange_coins,denominations)))
            min_reached=True
            min_coins=used_coins
    
    return min_reached

fname="input.txt"
lines=[line.rstrip('\r\n') for line in open(fname)]
#for i in range(1,len(lines)):
for i in range(2,len(lines)-1):
    line=[int(x) for x in lines[i].split()]
    n=line[0]
    k=line[1]
    del line[0:2]
    denominations=line[:]
    denominations.sort(reverse=True)
    posiblePayment=False
    total_coins=0
    used_coins=0
    max_coins=-1
    print(denominations)
    for amount in range(0, n+1):
        smaller_denom=list(filter(lambda x: x <= amount, denominations))
        payment_coins=[0 for i in range(0,len(denominations))]
        exchange_coins=[0 for i in range(0,len(denominations))]
        total_payment_coins=0
        total_exchange_coins=0
        total_payment=0
        total_exchange=0
        min_coins=99999999
        subtotal=0
        print "Amount " + str(amount)
        recursive(0,0)
        """ for d in range(0,len(denominations)):
            if denominations[d]<=amount:
                payment_coins[d]=(amount-subtotal)/denominations[d]
                max_per_denomination=payment_coins[d]

                subtotal+=payment_coins[d]*denominations[d]
                if subtotal==amount:
                    checkPossiblePayment(amount,payment_coins)
                for f in range(0,len(denominations)):
                    if denominations[f]+subtotal>=amount:
                        payment_coins[f]+=1
                        checkPossiblePayment(amount,payment_coins)
                        payment_coins[f]-=1
                    
            else:
                payment_coins[d]+=1
                total_payment_coins+=1
                total_payment=denominations[d]
                checkPossiblePayment(amount,payment_coins)
                payment_coins=[0 for i in range(0,len(denominations))] """
                


        print("Cant min coins "+str(min_coins))
        #print(list(map(lambda x, y: str(x)+" "+str(y), payment_coins,denominations)))
        #print("Amount: "+str(amount)+" Used coins: "+str(used_coins))
        #print("Total payed: ")
        #print(used_coins)
        total_coins+=min_coins
        if min_coins>max_coins:
            max_coins=min_coins
    #print(total_coins)
    average=round(Decimal(total_coins)/Decimal(n),2)
    print(str(average)+" "+str(max_coins))

    
