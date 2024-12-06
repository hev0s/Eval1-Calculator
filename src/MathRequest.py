# MathRequest.py
class MathRequest:
    def __init__(self):
        self.operand1 = None
        self.operator = None
        self.operand2 = None

    def ask_user_input(self):
        """Demander les entrées de l'utilisateur."""
        self.operand1 = self.ask_user_float_input("Enter the first operand: ")
        self.operator = input("Enter an operator (+, -, *, /, ^): ")
        self.operand2 = self.ask_user_float_input("Enter the second operand: ")

    def calculate(self):
        """Calculer le résultat en fonction de l'opérateur."""
        match self.operator:
            case '+':
                return self.operand1 + self.operand2
            case '-':
                return self.operand1 - self.operand2
            case '*':
                return self.operand1 * self.operand2
            case '/':
                if self.operand2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return self.operand1 / self.operand2
            case '^':
                return self.operand1 ** self.operand2
            case _:
                raise ValueError(f"Invalid operator: {self.operator}")

    @staticmethod
    def ask_user_float_input(prompt):
        """Demander un nombre flottant à l'utilisateur avec validation."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
