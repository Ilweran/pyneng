K = float(input("Starting capital? "))
D = float(input("How much you will add after each period? "))
p = float(input("Interest rate? "))
n = int(input("Number of years? "))

i = 0
while i < n:
    K +=  K * p / 100.0 + D
    i += 1
    print(i, K)
print("Capital after " + str(n) + " ys: " + str(K))
