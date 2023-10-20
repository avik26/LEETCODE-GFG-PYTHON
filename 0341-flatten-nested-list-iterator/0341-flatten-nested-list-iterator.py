class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = []
        self.flatten(nestedList)

    def flatten(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.flatten_list.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        return self.flatten_list.pop(0)

    def hasNext(self) -> bool:
        return bool(self.flatten_list)
