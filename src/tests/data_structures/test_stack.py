from hypothesis import given, strategies as st
import pytest

from data_structures.stack import Stack

@given(st.integers())
def test_stack_initialization(x):
    stack_no_args = Stack()
    assert stack_no_args.is_empty()
    
    stack_value_arg = Stack(x)
    assert stack_value_arg.pop() == x
    
    stack_list_arg = Stack([x])
    assert stack_list_arg.pop() == x
    
    with pytest.raises(ValueError):
        Stack(x, x)

@given(st.integers())
def test_stack_pops_pushed_values(x):
    stack = Stack()
    stack.push(x)
    assert stack.pop() == x

def test_pop_empty_stack_throws_exception():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_safe_pop_empty_stack_returns_none():
    stack = Stack()
    assert stack.safe_pop() is None

@given(st.integers())
def test_peek_doesnt_delete_element(x):
    stack = Stack()
    stack.push(x)
    
    assert stack.peek() == x
    assert stack.pop() == x

@given(st.integers())
def test_clone(x):
    stack = Stack()
    stack.push(x)
    
    cloned_stack = stack.clone()

    assert stack.pop() == x
    assert cloned_stack.pop() == x
    
@given(st.integers(), st.integers())
def test_swap(x, y):
    stack = Stack([x, y])
    stack.swap()
    
    assert stack.pop() == x
    assert stack.pop() == y
