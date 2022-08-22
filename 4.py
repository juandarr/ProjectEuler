"""
Finds the largest palindrome product of two numbers of 3 digits
Author: Juan Rios
"""
# Finds the largest palindrome producto of two 3 digit factors
def largest_palindrome():
    max_val = 0
    for i in range(999,101,-1):
        for j in range(i-1,101,-1):
            temp = str(i*j)
            if temp==temp[::-1] and int(temp)>max_val:
                max_val = int(temp)
    return max_val

if __name__ == "__main__":
    print('The largest palindrome of two 3 digit factors is {0}'.format(largest_palindrome()))
