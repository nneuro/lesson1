

def check(triplets):
    if 'ATG' in triplets and 'TAA' in triplets:
        if triplets.index('ATG') < triplets.index('TAA'):
            return True
    else:
        return False
  
x = 0
triplets = ['ATG', 'TAA', 'TAG', 'ATG', 'GGC', 'TAA']
while check(triplets) == True :
    print(f'цикл номер {x}, check = {check(triplets)}')
    x += 1
    triplets = triplets[1::]
    print(f'{triplets}, check = {check(triplets)}')