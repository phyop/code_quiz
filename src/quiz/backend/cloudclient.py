import uuid


class CloudClientAbstract(object):
    ''' This class defines the interface of a client connect to a cloud storage
    '''

    @property
    def root_id(self):
        ''' Get root's id

        return the root unique identifier on the cloud storage

        @return: root id
        @rtype: str
        '''

    def upload_file(self, parent_id, name, data):
        ''' Upload a file with name and data under parent_id

        e.g. 

        @param  parent_id: the parent id 
        @type   parent_id: str
        @param  name: the name of new file
        @type   name: str
        @param  data: a file-like object of source
        @type   data: bytes
        @return the metadata of new node
        @rtype  Node
        '''

    def create_folder(self, parent_id, name):
        '''Create a new folder with name under parent_id

        @param  parent_id: the parent id
        @type   parent_id: str
        @param  name: the name of new file
        @type   name: str
        @return the metadata of new node
        @rtype  Node
        '''

    def list_children(self, folder_id):
        ''' List children under specific folder_id

        @param  folder_id: the folder id
        @param  _id: unicode
        @return:    list of Node object
        @rtype:     list
        '''


class MemoryCloudClient(object):
    ''' This class simulate a cloud in memory
    '''
    def __init__(self):
        self._map = {
            "root": []
        }

    @property
    def root_id(self):
        return "dummy_root"

    def upload_file(self, parent_id, name, data):
        is_dir = False
        return self._create_node(parent_id, name, is_dir)

    def create_folder(self, parent_id, name):
        is_dir = True
        return self._create_node(parent_id, name, is_dir)

    def list_children(self, folder_id):
        try:
            return self._map[folder_id]
        except KeyError:
            raise FolderNotFoundError('folder not found')

    def _create_node(self, parent_id, name, is_dir):
        childrens = self._map.get(parent_id, [])

        for c in childrens:
            if c.name == name:
                return c

        node = Node(str(uuid.uuid4()), parent_id, name, is_dir)
        childrens.append(node)
        self._map[parent_id] = childrens
        return node


class Node(object):
    ''' Node has following attritubes
            - id, str
            - parent_id, str
            - name, str
            - is_dir, bool
    '''
    def __init__(self, _id, parent_id, name, is_dir):
        self.id = _id
        self.parent_id = parent_id
        self.name = name
        self.is_dir = is_dir

    def __str__(self):
        d = dict(vars(self))
        return '%s(%s)' % (self.__class__.__name__, d)


class FolderNotFoundError(Exception):
    pass
