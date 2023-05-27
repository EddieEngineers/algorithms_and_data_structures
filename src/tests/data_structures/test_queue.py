from hypothesis import given, strategies as st

from data_structures.queue import Queue, Deque

@given(st.integers(), st.integers(), st.integers())
def test_queue_is_FIFO(x, y, z):
    queue = Queue()
    queue.enqueue(x)
    queue.enqueue(y)
    queue.enqueue(z)
    
    assert queue.dequeue() == x
    assert queue.dequeue() == y
    assert queue.dequeue() == z

@given(st.integers(), st.integers())
def test_queue_increases_on_queue_and_decreases_on_dequeue(x, y):
    queue = Queue()
    assert len(queue) == 0
    
    queue.enqueue(x)
    queue.enqueue(y)
    assert len(queue) == 2
    
    assert queue.dequeue() == x
    assert len(queue) == 1
    
    assert queue.dequeue() == y
    assert len(queue) == 0

@given(st.integers(), st.integers(), st.integers())
def test_deque_pushes_front_and_back(x, y, z):
    pass

@given(st.integers(), st.integers(), st.integers())
def test_deque_pops_front_and_back(x, y, z):
    pass

@given(st.integers(), st.integers(), st.integers())
def test_deque_peeks_front_and_back(x, y, z):
    pass
