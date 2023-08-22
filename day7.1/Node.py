class Node(object):
    def __init__(self, name, parent, size):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
    
    def get_children(self):
        return self.children

    def add_child(self, obj):
        self.children.append(obj)

    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size = new_size

    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent

    