def calculate_electricity_bill(meter_reading):
    rate_per_unit = 0.7  # Price for consuming a single unit in rupees

    if meter_reading < 200:
        print("Congrats! You have got the electricity bill under 200 units.")
    else:
        bill_amount = meter_reading * rate_per_unit
        print(f"Your electricity bill for {meter_reading} units is: {bill_amount:.2f} rupees")

# Example usage
if __name__ == "__main__":
    try:
        meter_reading = float(input("Enter the meter reading (in units): "))
        calculate_electricity_bill(meter_reading)
    except ValueError:
        print("Please enter a valid number for the meter reading.")
