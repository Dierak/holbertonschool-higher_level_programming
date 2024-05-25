class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
        else:
            print(f"{item} not found in the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if 0 <= index < len(self):
            print(f"Popped {self[index]} from the list.")
        else:
            print("Index out of range.")
        return super().pop(index)
