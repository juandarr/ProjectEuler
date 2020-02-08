"""
Finds the sum of the only ordered set of six cyclic 4-digit numbers of polygonal type
"""

import math

def get_polygonal(lower_limit, upper_limit):
    octagonal = []
    heptagonal = []
    hexagonal = []
    pentagonal = []
    square = []
    triangle = []
    for i in range(lower_limit,upper_limit+1):
        oct = (2+math.sqrt(4+12*i))/6
        if oct==int(oct):
            octagonal.append(i)
        
        hep = (1.5+math.sqrt(1.5**2+10*i))/5
        if hep == int(hep):
            heptagonal.append(i)
       
        hex = (1+math.sqrt(1+8*i))/4
        if hex == int(hex):
            hexagonal.append(i)
        
        pen = (0.5+math.sqrt(0.5**2+6*i))/3
        if pen == int(pen):
            pentagonal.append(i)
        
        sqr = math.sqrt(i)
        if sqr == int(sqr):
            square.append(i)
        
        tri = (-0.5 + math.sqrt(0.5**2+2*i))
        if tri == int(tri):
            triangle.append(i)

    return [octagonal, heptagonal, hexagonal, pentagonal, square, triangle]
        
def get_candidates(ar, val):
    val_string = str(val)
    tmp_total = []
    for group in ar:
        tmp = []
        for candidate in group:
            if val_string[-2:]==str(candidate)[0:2]:
                tmp.append(candidate)
        tmp_total.append(tmp)
    return tmp_total

"""
Returns the sum of the only ordered set of six cyclic 4-digit numbers of polygonal type
"""
def sum_of_polygonal():
    polygonal = get_polygonal(1000, 9999)
    for i in polygonal[0]:
        candidates_0 = get_candidates(polygonal[1:],i)
        for i1 in range(len(candidates_0)):
            for j in candidates_0[i1]:
                ar1 = polygonal[1:][:i1]+polygonal[1:][i1+1:]
                candidates_1 = get_candidates(ar1,j)
                for i2 in range(len(candidates_1)):
                    for k in candidates_1[i2]:
                        ar2 = ar1[:i2]+ar1[i2+1:]
                        candidates_2 = get_candidates(ar2,k)
                        for i3 in range(len(candidates_2)):
                            for l in candidates_2[i3]:
                                ar3 = ar2[:i3]+ar2[i3+1:]
                                candidates_3 = get_candidates(ar3,l)
                                for i4 in range(len(candidates_3)):
                                    for m in candidates_3[i4]:
                                        ar4 = ar3[:i4]+ar3[i4+1:]
                                        candidates_4 = get_candidates(ar4,m)
                                        for i5 in range(len(candidates_4)):
                                            for n in candidates_4[i5]:
                                                if str(n)[-2:]==str(i)[:2]:
                                                    print(i,j,k,l,m,n,i+j+k+l+m+n)
                                                    return (i+j+k+l+m+n)

if __name__ == "__main__":
    print('The sum of ordered set of polygonal numbers is {0}'.format(sum_of_polygonal()))