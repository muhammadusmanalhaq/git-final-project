# simple_interest.py
# Simple Interest Calculator

def simple_interest(p, t, r):
    """
    Calculate simple interest.
    
    Parameters:
        p: principal amount
        t: time period in years
        r: annual rate of interest
    
    Returns:
        Simple interest = p * t * r / 100
    """
    return (p * t * r) / 100

if __name__ == "__main__":
    principal = 1000
    time = 2
    rate = 5
    si = simple_interest(principal, time, rate)
    print(f"Simple Interest = {si}")
