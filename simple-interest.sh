#!/bin/bash
# simple-interest.sh
# A simple script to compute simple interest based on user input

echo "Enter the principal amount:"
read principal

echo "Enter the rate of interest (per year):"
read rate

echo "Enter the time period (in years):"
read time

# Calculate simple interest: SI = (P * R * T) / 100
simple_interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo "Simple Interest = $simple_interest"
