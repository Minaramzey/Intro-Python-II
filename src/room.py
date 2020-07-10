# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []    

    def list_items(self):
        if not self.items:
            print('No items in this room.')
        else:
            print('This room contains:')
            for item in self.items:
                print(item.name, item.description) 