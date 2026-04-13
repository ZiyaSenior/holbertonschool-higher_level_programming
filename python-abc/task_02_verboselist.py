class VerboseList(list):
    """VerboseList class"""

    def append(self, value):
        super().append(value)
        print("Added [{}] to the list.".format(value))

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        value = self[index]
        print("Popped [{}] from the list.".format(value))
        return super().pop(index)
