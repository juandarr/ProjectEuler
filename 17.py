"""
Finds the number of letters that would be used writting the numbers from 1 to 1000
Author: Juan Rios
"""
import math

"""
Adds the number of letters used in the sequence of numbers from 1 to n
"""
def letter_quantity(n):
    units = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    teens = {1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
    tens = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    total = 0
    for num in range(1,n+1):
        if num==1000:
            total += len('one')+len('thousand')
            continue
        cen = num // 100
        cen_res = num % 100
        if cen > 0:
            total += len(units[cen])+len('hundred')
            if cen_res>0:
                total += len('and')
        if cen_res > 0:
            dec = cen_res // 10
            dec_res = cen_res % 10
            if dec == 0:
                total += len(units[dec_res])
            elif dec==1 and dec_res>0:
                total += len(teens[dec_res])
            elif dec>0:
                total += len(tens[dec])
                if dec_res>0:
                    total += len(units[dec_res])
    return total
    
if __name__ == "__main__":
    n = 1000
    print('The amount of letters written for numbers from 1 to {0} is {1}'.format(n,letter_quantity(n)))
