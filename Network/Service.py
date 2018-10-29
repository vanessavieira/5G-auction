class Service:
    used_units = 0

    def __init__(self, id, node, type):
        self.id = id
        self.node = node
        self.type = type

    def __str__(self):
        return "id: " + str(self.id) + "node: " + str(self.node) + "type: " + str(self.type) +\
               "used_units: " + str(self.used_units)
