def format(L, H, W):
        return((L*H*W)/1728)

L=float(input("Please, enter your subwoofer box's lenght "))
H=float(input("Please, enter your subwoofer box's height "))
W=float(input("Please, enter your subwoofer box's width "))

print("Your volume in cubic inches is ", L*H*W, ".")
print("Your volume in cubic feet is ", (L*H*W)/1728, "." )
