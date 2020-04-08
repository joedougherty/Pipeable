class BarePipelineDeclarationError(Exception):
    pass


class Pipeable:
    """
    Magically endow a function with the capability to be piped to/from.

    Functions: 
        * can be either named, or anonymous
        * must take *exactly one* required argument
    """
    def __init__(self, fn):
        self.fn = fn
        self.arg = None
        self.value = None
        self.called = False
        self.head = False

    def __or__(self, other):
        if not self.called:
            raise BarePipelineDeclarationError("Pipeable must be called at time of piping.")

        self.fn = other.fn
        self.value = self.fn(self.value)
        return self 

    def __call__(self, arg):
        self.called = True
        self.value = self.fn(arg)
        self.arg = arg
        return self

    def __repr__(self):
        return f"{self.value}"
