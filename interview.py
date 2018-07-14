import sys
def get_min_coins(coins, amount):
    """ Given an array of coins and a given value "amount" this function returns an array where each index point to the minimum number of coins needed to make that amount exactly
    """
    results=[sys.maxsize for _ in range(0,amount+1)]
    results[0]=0 
    for current_amount in range(1, amount+1):
        results[current_amount]=sys.maxsize
        for coin in coins:
            if coin<=current_amount:
                sub_result=results[current_amount-coin]
                if sub_result!=sys.maxsize and sub_result+1<results[current_amount]:
                    results[current_amount]=sub_result+1
    return results

fname="input.txt"
lines=[line.rstrip('\r\n') for line in open(fname)]
for i in range(1,len(lines)):
    line=[int(x) for x in lines[i].split()]
    n=line[0]
    k=line[1]
    del line[0:2]
    coins=line[:]
    result=get_min_coins(coins, n+max(coins)+1)
    max_used_coins=-1
    total=0
    for amount in range(1,n+1):
        min_coins=result[amount]
        # The minimum number of coins per transaction could be where payment=amount then the exchange is 0 
        # Otherwise payment>amount, so we check every possible payment and see if the number of coins for that payment + number of coins per exchange is minimum
        # If so, we save it
        for x in range(amount,n+max(coins)):
            if min_coins>result[x]+result[x-amount]:
                min_coins=result[x]+result[x-amount]
        if min_coins>max_used_coins:
            max_used_coins=min_coins
        total+=min_coins
    average=float(total)/float(n)
    print(str(average)+" "+str(max_used_coins))