
if __name__ == '__main__':
#t = int(raw_input())
t = int(input())
phase = 3
while t > phase:
    t -= phase
    phase *= 2

s = phase - t + 1
print("s")