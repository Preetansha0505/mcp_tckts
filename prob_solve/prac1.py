"""

prices[i] = []    
k = transactions t

buy i sell j    prices[j] - prices[i]
sell i buy j    prices[i] - prices[j]

Complete 1 t before starting another
do not buy or sell on the same day as prev t

max prof by atmost k t   
   
Input: prices = [1,7,9,8,2], k = 2
                [1, 7, 8, 9, 2]   

Output: 14

Explanation:

We can make $14 of profit through 2 transactions:
A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.

Notes - buy on the min day poss and sell on the max day poss

"""

def buy_sell_v(prices, k):
    mini = min(prices)
    maxi = max(prices)
    arr = [mini, maxi]
    total += maxi - mini
    pass


"""

Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
Output: [0,1,3]
Explanation:
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.    
    
"""


def share_secrets(n, m, fP)