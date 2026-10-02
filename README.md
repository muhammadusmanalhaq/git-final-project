# Simple Interest Calculator

A simple script that calculates simple interest given principal, annual rate of interest, and time period in years.

## Formula

`Simple Interest = (P x T x R) / 100`

## Input

- **p** - principal amount
- **t** - time period in years
- **r** - annual rate of interest

## Output

- **simple interest** = p x t x r / 100

## Usage

`python
def simple_interest(p, t, r):
    """Calculate simple interest."""
    return (p * t * r) / 100

# Example
principal = 1000
time = 2
rate = 5
si = simple_interest(principal, time, rate)
print(f"Simple Interest = {si}")
`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.