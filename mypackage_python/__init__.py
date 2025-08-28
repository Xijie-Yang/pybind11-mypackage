import mypackage_cpp

# This file is a Python wrapper of the C++ package, for IntelliSense.

def add(a: int, b: int = 1) -> int:
    """
    add two integers and return their sum
    """
    return mypackage_cpp.add(a, b)
