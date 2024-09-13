def add(n1, n2):
    """
    Returns the sum of two numbers.
    
    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.
    
    Returns:
    float: The result of adding n1 and n2.
    """
    return n1 + n2

def sub(n1, n2):
    """
    Returns the difference between two numbers.
    
    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.
    
    Returns:
    float: The result of subtracting n2 from n1.
    """
    return n1 - n2

def div(n1, n2):
    """
    Returns the quotient of two numbers.
    
    Parameters:
    n1 (float): The numerator.
    n2 (float): The denominator.
    
    Returns:
    float: The result of dividing n1 by n2.
    """
    return n1 / n2

def mult(n1, n2):
    """
    Returns the product of two numbers.
    
    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.
    
    Returns:
    float: The result of multiplying n1 and n2.
    """
    return n1 * n2

#Dictionary mapping symbols to functions
operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult,
}

def cal():
    """
    Main function to handle user input and perform calculations.
    """
    num1 = float(input("Enter 1st number: "))
    continue_calculating = "y"
    
    #Display available operations
    for key in operations:
        print(key)
    
    while continue_calculating == "y":
        operation_symbol = input("Pick an operation symbol: ")
        num2 = float(input("Enter another number: "))
        
        #Fetch the corresponding function and perform the operation
        operation = operations.get(operation_symbol)
        if operation:
            result = operation(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
            
            
            continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type anything else to exit: ").lower()
            if continue_calculating == "y":
                num1 = result
            else:
                print("Exiting the calculator.")
                break
        else:
            print("Invalid operation symbol. Please try again.")

cal()
