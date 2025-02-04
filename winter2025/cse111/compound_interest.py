def final_value(principal, rate, time, periods_per_year):
    """Calculate the final value of an investment."""
    return principal * (1 + rate / periods_per_year) ** (time * periods_per_year)

def main():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the annual interest rate: "))
    t = float(input("Enter the number of years: "))
    n = float(input("Enter the number of compounding periods per year: "))
    print(f'Final value: {final_value(p, r, t, n):.02f}')

if __name__ == "__main__":
    main()