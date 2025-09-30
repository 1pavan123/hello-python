def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"
