from datetime import datetime
from math import ceil

def get_square_feet():
    square_feet = 0.0
    while True:
        try:
            square_feet = float(input("\nPlease enter the total square feet of wall space: "))
            if (square_feet <= 0): 
                print("Invalid value. Must be a positive value greater than 0.")
                continue
        except ValueError:
            print("Invaid value. Only numbers are allowed.")
        else:
            break
    return square_feet

def get_price_of_paint():
    price_of_paint = 0.0
    while True:
        try:
            price_of_paint = float(input("Please enter the price of your paint per gallon: "))
            if (price_of_paint <= 0): 
                print("Invalid value. Must be a positive value greater than 0.\n")
                continue
        except ValueError:
            print("Invalid value. Only numbers are allowed.\n")
        else:
            break
    return price_of_paint

def calculate_paint_required(square_feet: float):
    gallons = int(ceil(square_feet / 350))
    return gallons

def calculate_labor_hours(square_feet: float):
    labor = float((square_feet / 350) * 6)
    return labor

def calculate_paint_cost(gallons: int, price_of_paint: float):
    cost = gallons * price_of_paint
    return cost

def calculate_labor_cost(labor_hours: float):
    cost = labor_hours * 62.25
    return cost

def adjust_string_padding(string_to_adjust: str, max_string_length: int):
    # pad the left side of the string by subtracting the left-side
    # character count from the max string length variable to
    # right-align them
    result = ""
    format_list = string_to_adjust.split(":")
    padding_size = max_string_length - (len(format_list[0]) + 1)
    formatted_string = format_list[1].rjust(padding_size, " ")
    result = format_list[0] + ":" + formatted_string
    return result


def print_receipt(max_string_length, strings_list, job_total):
    print("")
    print("-" * max_string_length)

    # Add local date, time, and sales associate
    date = datetime.now()
    print(f"{date.strftime('%c')}")
    print("Sales Associate: Travis") # TODO: Substitute with employee name

    print("-" * max_string_length)

    # Loop through list and 
    for elm in strings_list:
        formatted_string = adjust_string_padding(elm, max_string_length)
        print(formatted_string)

    print("-" * max_string_length)
    job_total = adjust_string_padding(job_total, max_string_length)
    print(job_total)

    print("-" * max_string_length)
    print("")

def display_results(gallons: int, labor_hours: float, paint_cost: float, labor_cost: float, total: float):
    # Format strings
    if  (gallons > 1):
        paint = f"Paint required: {gallons} gallons"
    else:
        paint = f"Paint required: {gallons} gallon"
    
    labor = f"Labor required: {labor_hours:.1f} hours"
    cost_of_paint = f"Cost of paint: ${paint_cost:.2f}"
    labor_cost_total = f"Labor cost: ${labor_cost:.2f}"
    job_total = f"Total: ${total:.2f}"

    # Add formatted strings to list
    strings_list = [paint, labor, cost_of_paint, labor_cost_total]

    # Get length of string with the most characters and add some extra space
    max_string_length = max(len(elm) for elm in strings_list)
    max_string_length += 10

    # Print totals formatted like a receipt
    print_receipt(max_string_length, strings_list, job_total)

def ask_user_to_continue():
    user_continue = input("Would you like to do another estimate? (y/n)").lower()
    if (user_continue != "y"):
        return False
    else:
        return True

def main():
    continue_running = True

    print("\nWelcome to the Paint Job Estimator!")

    while (continue_running):
        # Get square feet and price of paint from user
        square_feet = get_square_feet()
        price_of_paint = get_price_of_paint()

        # Perform calculations
        gallons = calculate_paint_required(square_feet)
        labor_hours = calculate_labor_hours(square_feet)
        paint_cost = calculate_paint_cost(gallons, price_of_paint)
        labor_cost = calculate_labor_cost(labor_hours)
        total = paint_cost + labor_cost

        # Display results
        display_results(gallons, labor_hours, paint_cost, labor_cost, total)

        # Continue?
        continue_running = ask_user_to_continue()

main()