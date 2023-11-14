"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """making two self variables so we can use self.start to reset the serial value."""
        self.start = self.next = start

    def __repr__(self):
        return f"SerialGenerator starts at {self.start}"

    def generate(self):
        """returns the starting value first and then every time it is called returns the next serial"""
        self.next += 1
        return self.next-1

    def reset(self):
        """resets the serial back to the starting value"""
        self.next = self.start
