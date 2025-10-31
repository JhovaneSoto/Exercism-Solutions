class CustomSet:
    def __init__(self, elements=[]):
        self.items=[]
        for element in elements:
            if element not in self.items:
                self.items.append(element)

    def isempty(self):
        return self.items==[]

    def __contains__(self, element):
        return element in self.items

    def issubset(self, other):
        tam=len(self.items)
        return any([other.items[pos:pos+tam]==self.items for pos in range(len(other.items)+1-tam)])

    def isdisjoint(self, other):
        return not(any([item in self.items for item in other.items]))

    def __eq__(self, other):
        return sorted(self.items)==sorted(other.items)

    def add(self, element):
        if element not in self.items:
            self.items.append(element)

    def intersection(self, other):
        items=[item for item in self.items if item in other.items]
        return CustomSet(items)

    def __sub__(self, other):
        items=[item for item in self.items if item not in other.items]
        return CustomSet(items)

    def __add__(self, other):
        items=self.items+other.items
        return CustomSet(items)
