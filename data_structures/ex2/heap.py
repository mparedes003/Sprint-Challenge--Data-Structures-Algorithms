'''# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root 
    l = 2 * i + 1  # left = 2*i + 1 
    r = 2 * i + 2  # right = 2*i + 2  

    # if left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]:
        largest = l

    # if right child of root exists and is greater than root     
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed     
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap 

        # heapify the root
        heapify(arr, n, largest)'''

def heapsort(arr):
# create a new empty heap
  new_heap = []
# loop over all elements in the array and insert each element in to the heap
  for i in arr:
    new_heap.append(i)
# create an empty array to put the sorted stuff in
  sorted = []
# oop over the storage of the heap appending the items to the new array
  for i in Heap.storage:
    sorted.append(i)
# reverse the array
  reverse_sorted = sorted[::-1]


class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2