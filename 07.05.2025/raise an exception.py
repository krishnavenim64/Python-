

Def set(age):

    If age < 0:

        Raise ValueError(“Age cannot be negative.”)

    Print(f”Age set to {age}”)



Try:

    Set(-5)

Except ValueError as e:

    Print(e)

