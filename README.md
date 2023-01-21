## Pipeable: a Class Wrapper to make your functions magically pipeable ##

    
    from Pipeable import Pipeable
        

    def multiply_by_4(n):
        return n * 4


    def add_12(n):
        return n + 12


    def divide_by_2(n):
        return n / 2


    def minus_4(n):
        return n - 4


    times4 = Pipeable(multiply_by_4)
    plus12 = Pipeable(add_12)
    halve  = Pipeable(divide_by_2)
    minus4 = Pipeable(lambda x: x - 4) # Yes, lambdas work as well!

    # BEHOLD
    result = times4(5) | plus12 | halve | minus4

    # The above call yields the same answer as...
    minus_4(divide_by_2(add_12(multiply_by_4(5))))


### ASPECTS TO NOTE ###


`Pipeable` does not support declaring a bare pipeline for later execution.


That is:


    pipe = times4 | plus12 | halve | minus4


raises: `BarePipelineDeclarationError`.


Instead, be sure to the call the first function in the pipeline like so:


    result = times4(5) | plus12 | halve | minus4

---

#### WHAT IF ONE OF THE FUNCTIONS I WANT TO MAKE `Pipeable` TAKES MULTIPLE ARGUMENTS? ####

Reach for `functools.partial`.


Let's say you have a function that takes multiple required arguments:


    def add_a_b_c(a, b, c):
        return a + b + c


Use `partial` to create a version with "frozen" args.


    from functools import partial
    

    add_a_9_14_fn = partial(add_a_b_c, b=9, c=14)

    add_a_9_14 = Pipeable(add_a_9_14_fn)

    result = times4(5) | plus12 | halve | add_a_9_14
    

### BUT I REALLY WANT TO DECLARE A FUNCTION PIPELINE AND CALL IT LATER, MAYBE ###


Okay, so we can't get it done with `Pipeable` but `FunctionChain` can do this:

    
    from FunctionChain import FunctionChain


    Chains two or more functions together 
    and returns final result when called.
    
        - functions must take *exactly one* required argument
        - lambdas are supported    

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


### RUNNING THE TESTS ###

    pytest


