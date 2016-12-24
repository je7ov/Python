def tower(n, fromT, toT, extraT):
    if n==1:
        print('Move piece ', n, ' from ', fromT, ' to ', toT, sep='')
        return
    tower(n-1, fromT, extraT, toT)
    print('Move piece ', n, ' from ', fromT, ' to ', toT, sep='')
    tower(n-1, extraT, toT, fromT)

n = int(input('Enter how many rings: '))
tower(n, 'A', 'B', 'C')
