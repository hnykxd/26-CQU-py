import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    
    partner = {}
    for _ in range(n):
        id1 = input_data[idx]
        id2 = input_data[idx+1]
        partner[id1] = id2
        partner[id2] = id1
        idx += 2
        
    m = int(input_data[idx])
    idx += 1
    
    guests = set(input_data[idx:idx+m])
    
    singles = []
    for guest in guests:
        if guest not in partner or partner[guest] not in guests:
            singles.append(guest)
            
    singles.sort()
        
    print(len(singles))
    if singles:
        print(" ".join(singles))

if __name__ == '__main__':
    main()

for i in range(len(l3)):
    if i%2 == 0:
        l3[i] =0