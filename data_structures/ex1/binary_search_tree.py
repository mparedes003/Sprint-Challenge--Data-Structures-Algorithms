class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # invoke callback on the node
    cb(self.value)

    # if the node is None
    if self.value is None:
      # return None
      return None

    # if there is a node on the left child of the parent on the tree, recursively call the depth_first_for_each on the left
    if self.left:
      self.left.depth_first_for_each(cb)
    
    # if there is a node on the right child of the parent on the tree, recursively call the depth_first_for_each on the right
    if self.right:
      self.right.depth_first_for_each(cb)
    

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
