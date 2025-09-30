def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"
hotfix/fix-crash-on-start
def greet(name: str) -> str:
    if not name:
        return "Hello!"
=======

def greet(name: str) -> str:
 main
    return f"Hello, {name.strip()}!"
