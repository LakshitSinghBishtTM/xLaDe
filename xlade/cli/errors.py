def error(title, message, hint=None):
    print(f"[xLaDe ERROR] {title}")
    print(f"  {message}")
    if hint:
        print(f"  Hint: {hint}")
