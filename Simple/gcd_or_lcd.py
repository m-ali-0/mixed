def gcd(a,b):
    if a==0: return b
    elif b==0: return a
    elif a<b: return gcd(a,b-a)
    else: return gcd(a-b,b)
    
def lcm(a,b):
    return a*b//gcd(a,b)


def main():
    a, b = 0, 0
    while 0 in (a,b):
        try:
            a,b = map(int,input('please enter a and b seperated by space: ').split())
            while a<=0 or b<=0: 
                a,b = map(int,input('please enter positive integers: ').split())
            op = input('please enter G (for gcd) or L (for lcm): ')
            while op not in ('g','G','l','L'):
                op = input('given input is not expected, please enter valid letter: ')    
        except ValueError as e:
            print('please enter valid integers.')
        except KeyboardInterrupt as e:
            print('program stopped by user.')
            exit()
    if op in ('g','G'):
        print(f'gcd of {a} and {b} is: {gcd(a,b)}')
    elif op in ('l','L'):
        print(f'lcm of {a} and {b} is: {lcm(a,b)}')

    try:
        ans = input('another one? (enter Y (for yes) or N (for no)): ')
        while ans not in ('Y','y','n','N'):
            ans = input('please enter valid answer: ')
        if ans in ('y','Y'):
            print('sure!')
            main()
        elif ans in ('n','N'):
            print('thank you!')
            exit()
    except KeyboardInterrupt as e:
        print('program stopped by user.')

while True:
    main()
        
    
        
    