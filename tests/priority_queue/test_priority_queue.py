import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Arrange
    priority_queue = PriorityQueue()

    high_priority_file = {
        "nome_do_arquivo": "high_priority.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }

    regular_priority_file = {
        "nome_do_arquivo": "regular_priority.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [],
    }

    low_priority_file = {
        "nome_do_arquivo": "low_priority.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    # Act
    priority_queue.enqueue(high_priority_file)
    priority_queue.enqueue(regular_priority_file)
    priority_queue.enqueue(low_priority_file)

    # Assert
    assert len(priority_queue) == 3
    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 1

    assert priority_queue.search(0) == regular_priority_file
    assert priority_queue.search(1) == low_priority_file
    assert priority_queue.search(2) == high_priority_file

    assert priority_queue.dequeue() == regular_priority_file
    assert priority_queue.dequeue() == low_priority_file
    assert priority_queue.dequeue() == high_priority_file

    assert len(priority_queue) == 0

    with pytest.raises(IndexError):
        priority_queue.search(99)
