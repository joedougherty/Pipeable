class FunctionChain:
    """
    Chains together two or more functions together 
    and returns final result when called.
    
        functions: 
            * must be named
            * must take *exactly one* required argument
            * ought to have explict return statements
            
        # Example code:
        def multiply_by_4(n):
            return n * 4

        def add_12(n):
            return n + 12

        def divide_by_2(n):
            return n/2

        special_op = FunctionChain(
            multiply_by_4, 
            add_12, 
            divide_by_2,
        )
        
        # This call ...
        special_op(5) 
    
        # ... is functionally equivalent to:
        divide_by_2(add_12(multiply_by_4(5)))
        
        # Also: has a cute string representation
        >> print(special_op)
        multiply_by_4() -> add_12() -> divide_by_2()
    """

    def __init__(self, *functions):
        self.functions = [f for f in functions]

        if len(self.functions) < 2:
            raise ValueError(
                """Please provide at least 2 functions to chain together."""
            )

    def __call__(self, arg):
        for idx, fn in enumerate(self.functions):
            if idx == 0:
                result = fn(arg)
            else:
                result = fn(result)

        return result

    def __repr__(self):
        return " -> ".join(["{}()".format(f.__name__) for f in self.functions])
