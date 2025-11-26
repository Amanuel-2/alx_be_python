import inspect
import os
import sys

# Ensure project root is on sys.path so tests can import modules in the workspace
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from fns_and_dsa.arithmetic_operations import perform_operation


def test_signature():
    sig = inspect.signature(perform_operation)
    params = list(sig.parameters.keys())
    assert params == ["num1", "num2", "operation"], (
        "perform_operation must have parameters named num1, num2, operation"
    )


def test_add():
    res = perform_operation(5.0, 6.0, "add")
    assert isinstance(res, float) or isinstance(res, int)
    assert res == 11.0


def test_subtract():
    assert perform_operation(10.0, 3.0, "subtract") == 7.0


def test_multiply():
    assert perform_operation(3.0, 4.0, "multiply") == 12.0


def test_divide():
    assert perform_operation(8.0, 2.0, "divide") == 4.0


def test_divide_by_zero():
    res = perform_operation(5.0, 0.0, "divide")
    assert isinstance(res, str)
    assert "division" in res.lower() or "zero" in res.lower()


def test_invalid_operation():
    res = perform_operation(1.0, 2.0, "power")
    assert isinstance(res, str)
    assert "invalid" in res.lower()
