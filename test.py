import math

def roots(x,y,i):
    roots = []
    roots.append(((2*x*y+math.sqrt(4*(x**2)*(y**2)-4*(y**2)*((x**2)-i)))/(2*(y**2))))
    roots.append(((2*x*y-math.sqrt(4*(x**2)*(y**2)-4*(y**2)*((x**2)-i)))/(2*(y**2))))
    return roots
    
if __name__ == "__main__":
    print('The roots are: {0}'.format(roots(2,3,19)))