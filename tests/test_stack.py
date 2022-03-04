import pytest



def test_stack():
    """Testing the main function."""
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptiness():
    """Testing additional functionality."""
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    """Edge cases."""
    stack =[]
    with pytest.raises(IndexError):
        stack.pop()
