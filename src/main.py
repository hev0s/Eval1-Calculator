operand1 = None
operator = None
operand2 = None

def main():
    ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(operand1, operator, operand2, result)


def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = ask_user_float_input("Enter the first operand: ")

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /, ^): ")

    global operand2
    # Get second operand from the user
    operand2 = ask_user_float_input("Enter the second operand: ")

def calculate(ope1, oper, ope2):
    # Perform the operation based on the operator
    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope1 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case '^':
            res = fonctionpuissance(ope1,oper, ope2)
        case _:
            print("Invalid operator.")
            return
    return res

def display_result(op1, ope, ope2, res):
    print(str(op1) + " " + ope + " " + str(ope2) + " = " + str(res))

#fonction float input
def ask_user_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Fonction puissance
def fonctionpuissance(ope1,oper, ope2):
    puiss = 1
    for _ in range(int(abs(ope2))):  # Utilisation de la valeur absolue pour gérer les puissances négatives
        puiss *= ope1

    if ope2 < 0:  # Gestion des puissances négatives
        return 1 / puiss
    return puiss

# Call the main function to run the program
main()
