class Vector:
    """A class to represent a vector in n-dimensional space."""

    def __init__(self, *args):
        """Initialize a Vector object with a variable number of arguments."""
        self.elements = list(args)

    def __str__(self):
        """Return a string representation of the Vector."""
        return str(self.elements)

    def length(self):
        """Return the length (number of elements) of the Vector."""
        return len(self.elements)

    def dim(self):
        """Return the dimensions (rows, columns) of the Vector."""
        return (self.length(), 1)

    def extend(self, element):
        """Add an element to the end of the Vector."""
        self.elements.append(element)

    def __add__(self, other):
        """Add two Vectors element-wise or add a scalar to a Vector."""
        if hasattr(other, "__float__") or hasattr(other, "__int__"):
            return Vector(*[other + element for element in self.elements])
        elif hasattr(other, "length"):
            if self.length() == other.length():
                return Vector(*[left + right for left, right in zip(self.elements, other.elements)])
            else:
                raise ValueError("The vectors are of different length!")
        else:
            raise ValueError(f"{other} is not a valid scalar or Vector object!")
        
    def __radd__(self, other):
        """Returns a new vector that is the result of adding this vector by a scalar."""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Substract two Vectors element-wise or substract a scalar from a Vector."""
        return self.__add__(-1*other)
    
    def __rsub__(self, other):
        """Returns a new vector that is the result of substracting a vector from a scalar."""
        return -1*self.__add__(other)
        
    def __mul__(self, other):
        """Multiply a Vector by a scalar or compute the dot product of two Vectors."""
        if hasattr(other, "__float__") or hasattr(other, "__int__"):
            return Vector(*[other * element for element in self.elements])
        elif hasattr(other, "length"):
            if self.length() == other.length():
                return sum([left * right for left, right in zip(self.elements, other.elements)])
            else:
                raise ValueError("The vectors are of different length!")
        else:
            raise ValueError(f"{other} is not a valid scalar or Vector object!")
        
    def __rmul__(self, other):
        """Returns a new vector that is the result of multiplying this vector by a scalar."""
        return self.__mul__(other)
    
    def __truediv__(self, other):
            if hasattr(other, "__float__") or hasattr(other, "__int__"):
                return self.__mul__(1/other)
            else:
                raise ValueError("Only scalar division is allowed!")