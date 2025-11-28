#Best Time to Buy & Sell Stocks
# Leetcode Lesson: Best Time to Buy and Sell Stock
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
print (maxProfit([7,1,6,5,3,4,2,]))



def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        char_index[char] = end
    
    return max_length
print(lengthOfLongestSubstring(["a","b","c","a","b","c","a","e","f","g",]))