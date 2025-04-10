"""
Example Dummy Python Script

This script contains a simple function that returns a greeting message
and a function that returns a farewell message.
"""


def hello(name: str) -> str:
    """
    Example function that returns a greeting message with the provided name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message.

    """
    return f"Hello, {name}!"


def bye(name: str) -> str:
    """
    Example function that returns a farewell message with the provided name.

    Args:
        name (str): The name to include in the farewell.

    Returns:
        str: A farewell message.

    """
    return f"Goodbye, {name}!"
