def hello_world(name: str) -> str:
    """
    Prints a greeting message with the given name.

    Parameters:
    name (str): The name to include in the greeting message.

    Returns:
    str: The greeting message.

    Raises:
    TypeError: If the `name` parameter is not a string.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting