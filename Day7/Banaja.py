class Item:
    def __init__(self, name,type,**others):
        self.name = name
        self.type = type
        self.others = others
        self.size=self.calculate_size()

    def calculate_size(self):
        return len(self.name) + len(self.type)

class Storage:
    def __init__(self, host, port, protocol,max_size):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []
        self.max_size=max_size
       

    def add_element(self, item):
        
        if not isinstance(item,Item):
            raise TypeError
        
        self.container.append(item)
        if self.calculate_size()>self.max_size:
            raise MemoryError
        return item      
        
    def calculate_size(self):
        self.size = sum([item.size for item in self.container])
        return self.size

item1 = Item('item1','type1', color='red', weight= '20kg')
item2=Item('item2','type1',color='pink',weight='10kg')

storage1 = Storage('storage1', 1, 'protocol1',10)

storage1.add_element(item1)
      
print(storage1.add_element(item2))

print(storage1.calculate_size())


