from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
    mock_data = [
        {"nome_do_arquivo": "file1.txt", "qtd_linhas": 3},
        {"nome_do_arquivo": "file2.txt", "qtd_linhas": 6},
        {"nome_do_arquivo": "file3.txt", "qtd_linhas": 2},
    ]
    [pq.enqueue(item) for item in mock_data]
    assert len(pq) == 3
    removed_file = pq.dequeue()
    assert removed_file is not None
    assert removed_file["nome_do_arquivo"] == "file1.txt"
    assert pq.search(0)["nome_do_arquivo"] == "file3.txt"
    assert len(pq) == 2
    with pytest.raises(IndexError):
        pq.search(len(pq))
