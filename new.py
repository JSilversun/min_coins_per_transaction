from functools import reduce
from decimal import Decimal

def calculateExhange(amount, payment, coins):
    global m_exchange
    exchange=payment-amount
    if exchange in m_exchange:
        return m_exchange[exchange]
    exchange_coins=[0 for i in range(0,len(coins))]
    subtotal=0
    for d in range(0,len(coins)):
        if coins[d]<=(exchange-subtotal):
            exchange_coins[d]=(exchange-subtotal)/coins[d]
            subtotal+=exchange_coins[d]*coins[d]
    if subtotal<exchange:
        return None
    else:
        m_exchange[exchange]=exchange_coins
        return exchange_coins

def recursive(current, subtotal):
    global coins, amount, payment_coins
    for i in range(current,len(coins)):
        current_max=((amount-subtotal)/coins[i])+1
        for j in reversed(range(0, current_max+1)):
            payment_coins[i]=j
            subtotal+=payment_coins[i]*coins[i]
            if subtotal>=amount:
                checkPayment(payment_coins)
            if i+1< len(coins) and subtotal<amount:
                recursive(i+1, subtotal)
            subtotal-=payment_coins[i]*coins[i]

def minCoins(coins, m, amount):
    if (amount == 0):
        return 0
 
    res = sys.maxsize
    table={}
    table[0]=0 
    table=[sys.maxsize for _ in range(0,amount)]
    for i in range(0, amount):
        table[i]=sys.maxsize
        for j in range(0,m):
            if coins[j]<=i:
                sub_result=table[i-coins[j]]
            if sub_result!=sys.maxsize and sub_result+1<table[i]:
                table[i]=sub_result+1
 
    return table[amount]

fname="input.txt"
lines=[line.rstrip('\r\n') for line in open(fname)]
#for i in range(1,len(lines)):
for i in range(2,len(lines)-1):
    line=[int(x) for x in lines[i].split()]
    n=line[0]
    k=line[1]
    del line[0:2]
    coins=line[:]
    coins.sort(reverse=True)
    posiblePayment=False
    total_coins=0
    used_coins=0
    max_coins=-1
    print(coins)
    for amount in range(0, n+1):
        smaller_denom=list(filter(lambda x: x <= amount, coins))
        payment_coins=[0 for i in range(0,len(coins))]
        exchange_coins=[0 for i in range(0,len(coins))]
        total_payment_coins=0
        total_exchange_coins=0
        total_payment=0
        total_exchange=0
        min_coins=99999999
        m_exchange={}
        subtotal=0
        #print("Amount " + str(amount))
        recursive(0,0)
                
        #print("Cant min coins "+str(min_coins))
        total_coins+=min_coins
        if min_coins>max_coins:
            max_coins=min_coins
    average=round(Decimal(total_coins)/Decimal(n),2)
    print(str(average)+" "+str(max_coins))
