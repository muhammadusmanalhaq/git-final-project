# Simple Interest Calculator

A simple script that calculates simple interest given principal, annual rate of interest, and time period in years.

## Formula

```
Simple Interest = (P x T x R) / 100
```

## Input

- **p** - principal amount
- **t** - time period in years
- **r** - annual rate of interest

## Output

- **simple interest** = p x t x r / 100

## Usage

```bash
chmod +x simple-interest.sh
./simple-interest.sh
```

### Example Run

```
Enter the principal amount:
1000
Enter the rate of interest (per year):
5
Enter the time period (in years):
2
Simple Interest = 100.00
```

## Python Version

```python
def simple_interest(p, t, r):
    return (p * t * r) / 100

print(simple_interest(1000, 2, 5))
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
