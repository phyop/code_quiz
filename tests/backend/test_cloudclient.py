import pytest

from quiz.backend.cloudclient import MemoryCloudClient


@pytest.fixture
def client():
    return MemoryCloudClient()


def test_memory_client_upload_file(client):
    expected = []
    num = 10
    for i in range(num):
        parent_id = client.root_id
        name = 'new_file%s' % i
        node = client.upload_file(parent_id, name, 'foobar_data')
        expected.append(node)
        assert node.is_dir == False

    childrens = client.list_children(client.root_id)
    assert len(childrens) == num
    assert expected == childrens


def test_memory_client_create_folder(client):
    expected = []
    num = 10
    for i in range(num):
        parent_id = client.root_id
        name = 'new_dir%s' % i
        node = client.create_folder(parent_id, name)
        expected.append(node)
        assert node.is_dir == True

    childrens = client.list_children(client.root_id)
    assert len(childrens) == num
    assert expected == childrens
