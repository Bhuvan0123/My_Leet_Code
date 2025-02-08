# Design a number container system that can do the following:

# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:

# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
class NumberContainers:

    def __init__(self):
        self.indexes={}
        self.res={}

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            if self.indexes[index]==number:
                return
        self.indexes[index]=number
        if number not in self.res:
            self.res[number]=[]
        heapq.heappush(self.res[number],index)

    def find(self, number: int) -> int:
        if number not in self.res:
            return -1
        while self.res[number] and self.indexes[self.res[number][0]]!=number:
            heapq.heappop(self.res[number])
        if self.res[number]:
            return self.res[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)