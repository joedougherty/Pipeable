class Pipeable:
    """
    Magically endow a function with the capability to be piped to/from.

    Functions: 
        * can be either named, or anonymous
        * must take *exactly one* required argument
    """
    def __init__(self, fn, arg=None, name=''):
        self.fn = fn
        self.arg = arg
        self.value = None
        self.name = name

    def __or__(self, other):
        if self.value is None:
            self.value = self.fn(self.arg)
            self.value = other.fn(self.value)
        else:
            self.fn = other.fn
            self.value = self.fn(self.value)
        return self 

    def __call__(self, arg):
        self.arg = arg
        return self

    def __repr__(self):
        return "{}".format(self.value)
