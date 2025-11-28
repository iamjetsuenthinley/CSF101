1. [Duplicates]
This Python program defines a function containsDuplicate to check if a list has any duplicate elements. It iterates through the list and uses a set to keep track of elements that have already been seen. If an element appears more than once, the function returns True; otherwise, it returns False.
For the example list x = [1, 2, 3, 4, 5, 6, 7, 7], the function detects the duplicate 7 and prints:True

2. [Longest_Substring]
This Python program defines a function lengthOfLongestSubstring to find the length of the longest substring without repeating characters. It uses a dictionary char_index to track the last seen index of each character and two pointers (start and end) to maintain a sliding window of unique characters. Whenever a repeated character is found within the current window, start is moved right after the previous occurrence to maintain uniqueness.

3. [Palindrome]
This Python program defines a function isPalindrome to check if a string is a palindrome, ignoring spaces, punctuation, and letter case. It uses two pointers, left and right, to compare characters from both ends, skipping non-alphanumeric characters. If any mismatch is found, it returns False; otherwise, it returns True.

4. [Best_time_to_Buy_&_Sell_Stocks]
Best Time to Buy & Sell Stocks (maxProfit)
This function calculates the maximum profit from a list of stock prices where you can buy and sell once. It keeps track of the minimum price seen so far and the maximum profit achievable at each step.

5. [Stack_Using_Queue]
This Python program implements a Stack using two Queues (q1 and q2). It simulates the Last In, First Out (LIFO) behavior of a stack with the following operations:

push(x): Adds an element to the stack by enqueueing it in q2 and then transferring all elements from q1 to q2, effectively keeping the newest element at the front.

pop(): Removes and returns the top element from the stack (front of q1).

top(): Returns the top element without removing it.

empty(): Checks if the stack is empty.

6. [Two_Sum]
his Python program implements the Two Sum problem, which finds two numbers in a list that add up to a given target. It uses a hash map (dictionary) to store numbers and their indices as it iterates through the list. For each number, it checks if the complement (target minus the current number) exists in the map. If found, it returns the indices of the two numbers.

7. [Three_Sum]
This Python program implements the Three Sum problem, which finds all unique triplets in a list that sum to zero. It first sorts the list and then uses a two-pointer approach for each element: one pointer starting just after the current element (left) and one at the end (right). By moving the pointers inward based on the sum, it efficiently finds triplets while skipping duplicates to ensure uniqueness.