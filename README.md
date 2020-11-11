# Setup
1. Clone this repository
2. Setup tox on your environment (https://tox.readthedocs.io/en/latest/)
3. Run 'tox' and you will see
```sh
tests/test_encrypt.py::test_name_cipher_encode PASSED                         [ 25%]
tests/test_encrypt.py::test_name_cipher_decode PASSED                         [ 50%]
tests/backend/test_cloudclient.py::test_memory_client_upload_file PASSED      [ 75%]
tests/backend/test_cloudclient.py::test_memory_client_create_folder PASSED    [100%]

========================================= 4 passed in 0.03s =========================================

```
Now, you pass all unittests in the project.

# Install
1. Prepare virtual environment if necessary
2. Run "python setup.py install"
3. You will get a command line utility "quiz_cli", "quiz_cli" is a utility to simulate upload a file, make a folder, and browse the data on cloud.
4. Run "quiz_cli"
```sh
$ quiz_cli 
quiz_cli:ls /
# list children of "/", and "/" is empty folder now.

quiz_cli:mkdir / test_folder
Node({'id': '36b8759f-b785-4740-9608-1aeea523230b', 'parent_id': '/', 'name': 'test_folder', 'is_dir': True})

# make a dir "test_folder" in "/", and you get a new node with id '36b8759f-b785-4740-9608-1aeea523230b'

quiz_cli:ls /
Node({'id': '36b8759f-b785-4740-9608-1aeea523230b', 'parent_id': '/', 'name': 'test_folder', 'is_dir': True})

# list children of "/", you will see the node "36b8759f-b785-4740-9608-1aeea523230b"

quiz_cli:upload / test_file1 mydata
Node({'id': 'b1a56335-5129-41f2-a4cf-0d6fdea812bd', 'parent_id': '/', 'name': 'test_file1', 'is_dir': False})

# upload a file "test_file1" in "/", the file content is "mydata"

quiz_cli:ls /
Node({'id': '36b8759f-b785-4740-9608-1aeea523230b', 'parent_id': '/', 'name': 'test_folder', 'is_dir': True})
Node({'id': 'b1a56335-5129-41f2-a4cf-0d6fdea812bd', 'parent_id': '/', 'name': 'test_file1', 'is_dir': False})

# list children of "/", you have 1 file and 1 folder in "/" now.

quiz_cli:upload 36b8759f-b785-4740-9608-1aeea523230b test_file1 mydata
Node({'id': 'a338a8e8-b95a-4c97-8854-d0e561daeaac', 'parent_id': '36b8759f-b785-4740-9608-1aeea523230b', 'name': 'test_file1', 'is_dir': False})

# upload a file into folder "36b8759f-b785-4740-9608-1aeea523230b"

quiz_cli:ls 36b8759f-b785-4740-9608-1aeea523230b
Node({'id': 'a338a8e8-b95a-4c97-8854-d0e561daeaac', 'parent_id': '36b8759f-b785-4740-9608-1aeea523230b', 'name': 'test_file1', 'is_dir': False})

# list children of "a338a8e8-b95a-4c97-8854-d0e561daeaac", you will see the file you uploaded.

```

# Development
Great! We have a utility "quiz_cli" to connect to cloud storage. We can use it to access data on cloud.

Consider the following scenario, we have to add a new feature "client-side encryption" on it.
It means all folder name and file name should be encrypted before transfer to cloud. However,
customers want to see the real name with "quiz_cli".

## Requirements of Client-side encryption
- When uploading a file via "quiz_cli", the file name should be encrypted via encrypt.FileNameCipher before upload to cloud.
- When creating a folder via "quiz_cli", the folder name should be encrypted via encrypt.FileNameCipher before upload to cloud.
- When ls a folder via "quiz_cli", customers want to see the folder and file name in plaintext.
- "quiz_cli" should have the ability to disable client-side encryption if customers want to. Customers might run multiple "quiz_cli"
  process to connect to different cloud storage, e.g. googledrive and dropbox, and Customers only want to encrypt for googledrive but
  not encrypt for dropbox.

Please add the feature to "quiz_cli". Keep readability and flexibility in your design. Change is the only constant in life.
