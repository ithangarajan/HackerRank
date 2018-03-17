n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
m = int(input().strip())
sum = 0
for x in range(0, len(ar)):
    if x != k:
        sum = sum + ar[x]
if (m==(sum / 2)):
    print ("Bon Appetit")
else:
    print (int((m - (sum / 2))))