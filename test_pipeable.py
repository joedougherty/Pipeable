from functools import partial
import pytest


from Pipeable import Pipeable, BarePipelineDeclarationError
from FunctionChain import FunctionChain

#
# A handful of helpful functions
#
def multiply_by_4(n):
    return n * 4


def add_12(n):
    return n + 12


def divide_by_2(n):
    return n / 2


def minus_4(n):
    return n - 4


def test_it_does_what_it_says_it_does_on_the_box():
    times4 = Pipeable(multiply_by_4)
    plus12 = Pipeable(add_12)
    halve = Pipeable(divide_by_2)
    minus4 = Pipeable(lambda x: x - 4)  # Yes, lambdas work as well!

    # BEHOLD
    pipe_result = times4(5) | plus12 | halve | minus4

    # The above call yields the same answer as...
    nested_call_result = minus_4(divide_by_2(add_12(multiply_by_4(5))))

    assert pipe_result.value == nested_call_result


def test_call_behavior():
    times4 = Pipeable(multiply_by_4)

    assert times4(4).value == 16.0


def test_that_a_bare_pipeline_raises_an_exception():
    times4 = Pipeable(multiply_by_4)
    plus12 = Pipeable(add_12)
    halve = Pipeable(divide_by_2)
    minus4 = Pipeable(lambda x: x - 4)  # Yes, lambdas work as well!

    # This is not supported and will raise an exception
    with pytest.raises(BarePipelineDeclarationError):
        pipe = times4 | plus12 | halve | minus4


def test_partials_seem_to_work_as_well():
    times4 = Pipeable(multiply_by_4)
    plus12 = Pipeable(add_12)
    halve = Pipeable(divide_by_2)
    minus4 = Pipeable(lambda x: x - 4)  # Yes, lambdas work as well!

    def add_a_b_c(a, b, c):
        return a + b + c

    single_arg_version = Pipeable(partial(add_a_b_c, b=9, c=14))

    pipe_result = times4(5) | plus12 | halve | minus4 | single_arg_version

    assert pipe_result.value == 35.0


def test_function_chain_does_what_it_says_on_the_box():
    special_op = FunctionChain(multiply_by_4, add_12, divide_by_2,)

    # This call ...
    fn_chain_result = special_op(5)

    # ... is functionally equivalent to:
    nested_fn_call_result = divide_by_2(add_12(multiply_by_4(5)))

    assert fn_chain_result == nested_fn_call_result
