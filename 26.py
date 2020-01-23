"""
Finds the value d for which the representation of unit fractions has the longest recurring cycle
Author: Juan Rios
"""

def unit_fraction(den):
    residues = [0]*(den)
    sequence = []
    residues[1] = 1
    num = 1
    while True:
        if num<den:
            num *= 10
            while (num<den):
                num *= 10
                sequence.append(0)
                if residues[num//10]==0:
                    residues[num//10]=len(sequence)+1
            if residues[num%den]==0:
                sequence.append(num//den)
                residues[num%den] = len(sequence)+1
                if num%den==0:
                    #Uncomment this if you want to see the numerical expression of the result 
                    #return '0.'+''.join(str(i) for i in sequence)
                    return 0
            else:
                sequence.append(num//den)
                separator = residues[num%den]
                #Uncomment this if you want to see the numerical expression of the result 
                #return '0.'+''.join(str(i) for i in sequence[:separator-1])+'('+''.join(str(i) for i in sequence[separator-1:])+')'
                return len(sequence[separator-1:])
            num %= den

def longest_unit_fraction(limit_value):
    max_value = 0
    number = 2
    for i in range(2,limit_value):
        value = unit_fraction(i)
        if value > max_value:
            max_value = value
            number = i
    return number
    
if __name__ == "__main__":
    limit_value = 1000
    print('The value with the longest recurring fraction under {0} is {1}'.format(limit_value, longest_unit_fraction(limit_value)))