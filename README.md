### Pipeable: a Class Wrapper to make your functions magically pipeable ###

    
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
