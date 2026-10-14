def simple_interest(principal, interest, time):
    return (principal*interest*time)/100

if __name__== "__main__":
    p = int(input("Enter principal amt"))
    i = float(input("Enter interest"))
    t = int(input("Enter time in moths"))

    print("Simple interst is:",simple_interest(p,i,t))