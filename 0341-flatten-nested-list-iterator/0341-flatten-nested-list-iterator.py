class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.flatten(nestedList)

    def flatten(self, nested_list):
        for i in range(len(nested_list) - 1, -1, -1):
            self.stack.append(nested_list[i])

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.flatten(top.getList())
        return False
