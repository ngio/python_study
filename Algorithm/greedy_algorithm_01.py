# https://www.acmicpc.net/problem/2839
#
#  Greedy algorithm 그리디 알고리즘
#

# 예제 1 
def coin_change(coins, amount):
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    num_coins = 0
    i = 0
    
    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            # Use as many coins of the highest denomination as possible
            num_coins += amount // coins[i]
            amount %= coins[i]
        i += 1
    
    if amount == 0:
        return num_coins
    else:
        return -1  # Not possible to make the amount with given coins


# Example usage
coins = [1, 2, 5]
amount = 11
print(f"Minimum number of coins needed: {coin_change(coins, amount)}")  # Output: 3


print("===================================================================")
# 예제 2
#python code
N = int(input("원금을 정수 형태로 입력하세요 : "))
coin = [500,100,50,10]
cnt = 0 # 거스름돈의 갯수

for i in coin:
    cnt += (N // i)
    N %= i

print( "거스름돈의 개수는 "+ str(cnt) )



