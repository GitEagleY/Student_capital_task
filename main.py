
def maximize_income(N, C, gains, price):

    laptop_tuples = zip(gains, price)

    #sort laptops based on the ratio of gains to price
    sorted_laptops = sorted(laptop_tuples, key=lambda x: x[0]/x[1], reverse=True)

    #extract only the sorted laptops
    laptops = [laptop for laptop in sorted_laptops]

    #initialize capital
    capital = C

    #buy laptops until reaching the maximum number allowed or running out of capital
    for gain, cost in laptops:
        if N <= 0 or capital < cost:# if theres no laptops we can buy or we dont have capital anymore
            break
        capital -= cost  #subtract the cost of the laptop
        capital += gain  #add the gain from selling the laptop
        N -= 1  #decrease the count of laptops we can buy

    return capital  #return the final capital


def main():
    try:
        N = int(input("Enter the number of laptops you can deal with(N): "))
        if N <= 0:
            raise ValueError("Number of laptops must be a positive integer")

        C = float(input("Enter your initial capital in USD (C): "))
        price = list(map(float, input("Enter the actual price of laptops in USD separated by spaces: ").split()))
        gains = list(map(float, input("Enter the gains in USD you expect from selling laptops separated by spaces: ").split()))
        

        if len(gains) != len(price):
            print("Error: Lengths of gains array and price array must be equal.")
            return

        capital_at_end = maximize_income(N, C, gains, price)
        print("Capital at the end of the summer:", capital_at_end)
        
    except ValueError as e:
        print("Error:", e)

main()
