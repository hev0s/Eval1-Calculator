from MathRequest import MathRequest

def main():
    math_request = MathRequest()

    try:
        # Demander les entrées utilisateur
        math_request.ask_user_input()

        # Calculer le résultat
        result = math_request.calculate()

        # Afficher le résultat en passant l'objet MathRequest
        display_result(math_request, result)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

def display_result(math_request, result):
    """Affiche le résultat en utilisant un objet MathRequest."""
    print(f"{math_request.operand1} {math_request.operator} {math_request.operand2} = {result}")

# Appeler la fonction principale
if __name__ == "__main__":
    main()
