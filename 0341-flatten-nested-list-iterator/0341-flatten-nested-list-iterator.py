class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        if self.hasNext():
            if self.stack[-1].isInteger():
                return self.stack.pop().getInteger()
            else:
                nested_list = self.stack.pop().getList()
                self.stack.extend(nested_list[::-1])
            return self.next()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            nested_list = self.stack.pop().getList()
            self.stack.extend(nested_list[::-1])
        return bool(self.stack)
