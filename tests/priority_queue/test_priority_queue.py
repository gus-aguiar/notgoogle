import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    def test_enqueue_high_priority():
        queue = PriorityQueue()

        data = {"qtd_linhas": 4, "nome_arquivo": "file1.txt"}
        queue.enqueue(data)

        assert len(queue.high_priority) == 1
        assert len(queue.regular_priority) == 0

    def test_enqueue_regular_priority():
        queue = PriorityQueue()
        data = {"qtd_linhas": 6, "nome_arquivo": "file2.txt"}
        queue.enqueue(data)

        assert len(queue.high_priority) == 0
        assert len(queue.regular_priority) == 1

    def test_dequeue_high_priority():
        queue = PriorityQueue()
        high_priority_data = {"qtd_linhas": 3, "nome_arquivo": "file3.txt"}
        regular_priority_data = {"qtd_linhas": 7, "nome_arquivo": "file4.txt"}

        queue.enqueue(high_priority_data)
        queue.enqueue(regular_priority_data)

        dequeued_item = queue.dequeue()

        assert dequeued_item == high_priority_data
        assert len(queue.high_priority) == 0
        assert len(queue.regular_priority) == 1

    def test_dequeue_regular_priority():
        queue = PriorityQueue()
        high_priority_data = {"qtd_linhas": 3, "nome_arquivo": "file5.txt"}
        regular_priority_data = {"qtd_linhas": 7, "nome_arquivo": "file6.txt"}

        queue.enqueue(high_priority_data)
        queue.enqueue(regular_priority_data)

        dequeued_item = queue.dequeue()

        assert dequeued_item == high_priority_data
        assert len(queue.high_priority) == 0
        assert len(queue.regular_priority) == 1

        queue.dequeue(high_priority_data)
        queue.dequeue(regular_priority_data)

        assert len(queue.high_priority) == 0
        assert len(queue.regular_priority) == 0
        with pytest.raises(IndexError):
            queue.search(99)
