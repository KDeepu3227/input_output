'''
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
Input and Output Format
Input Format:
The first line contains the principal amount (principal).
The second line contains the rate of interest (rate) per annum.
The third line contains the time (time) in years.
Output Format:
A single line containing the simple interest calculated.
'''
# Input
principal = float(input())
rate = float(input())
time = float(input())

# Calculation
simple_interest = (principal * rate * time) / 100

# Output
print(simple_interest)
'''
1000
5
2
100.0
