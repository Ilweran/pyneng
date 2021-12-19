K = float(input("Starting capital? "))
p = float(input("Interest rate? "))
n = int(input("Number of years? "))

i = 0
while i < n:
    K +=  K * p / 100.0
    # or K *=  1 +  p / 100.0
    i += 1
    print(i, K)
print("Capital after " + str(n) + " ys: " + str(K))
