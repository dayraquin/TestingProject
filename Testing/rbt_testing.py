import pytest
from rbtree import RBTree 

def test_is_valid():
    root = Node(13, 'k')
    root.left = Node(3, 'r')
    root.right = Node(14, 'r')
    root.left.parent = root
    root.right.parent = root
    root.left.left = Node(2, 'k')
    root.left.right = Node(8, 'k')
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left = Node(16, 'k')
    root.right.right = Node(9, 'k')
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    tree = RBTree(root)  

    assert tree.is_valid() == True

    root.right.color = 'k'
    with pytest.raises(Exception):
        tree.is_valid()
        
        
def test_tree_traversals():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    tree = RBTree(root)  

    assert tree.inorder() == [4, 2, 5, 1, 3]
    assert tree.preorder() == [1, 2, 4, 5, 3]
    assert tree.levelorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [4, 5, 2, 3, 1]
    
    
def test_get_node():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    tree = RBTree(root) 

    assert tree.get_node(1) == root
    assert tree.get_node(2) == root.left
    assert tree.get_node(3) == root.right
    assert tree.get_node(4) == None

def test_rotate_left():
    root = Node(1)
    root.right = Node(2)

    tree = RBTree(root) 

    tree._rotate_left(root)

    assert tree.Root.key == 2
    assert tree.Root.left.key == 1

def test_rotate_right():
    root = Node(2)
    root.left = Node(1)

    tree = RBTree(root)  

    tree._rotate_right(root)

    assert tree.Root.key == 1
    assert tree.Root.right.key == 2
    
def test_insert_cases():
    root = Node(13, 'k')
    root.left = Node(3, 'r')
    root.right = Node(14, 'r')
    root.left.parent = root
    root.right.parent = root
    root.left.left = Node(2, 'k')
    root.left.right = Node(8, 'k')
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left = Node(16, 'k')
    root.right.right = Node(9, 'k')
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    tree = RBTree(root)  

    new_node = Node(10, 'r')
    tree.insert(new_node)

    assert tree.Root.color == 'k'
    assert new_node.parent.color == 'k'

    #checking the color of the new node's uncle
    assert new_node.parent.parent.right.color == 'k'
    
    
def test_insert_and_insert_from():
    tree = RBTree()  
    tree.insert(1, 'a')
    assert tree.get_node(1).value == 'a'

    tree.insert_from([(2, 'b'), (3, 'c')])
    assert tree.get_node(2).value == 'b'
    assert tree.get_node(3).value == 'c'

def test_get_max_and_get_min():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)

    tree = RBTree(root)

    assert tree.get_max().key == 3
    assert tree.get_min().key == 1

def test_get_element_count_and_get_height():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)

    tree = RBTree(root)

    assert tree.get_element_count() == 3
    assert tree.get_height() == 2
    
def test_delete_cases():
    root = Node(13, 'k')
    root.left = Node(3, 'r')
    root.right = Node(14, 'r')
    root.left.parent = root
    root.right.parent = root
    root.left.left = Node(2, 'k')
    root.left.right = Node(8, 'k')
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left = Node(16, 'k')
    root.right.right = Node(9, 'k')
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    tree = RBTree(root)  
    tree.delete(7)

    assert tree.Root.color == 'k'
    assert tree.get_node(1).parent.right.color == 'k'
    
def test_delete_cases():
    root = Node(11, 'k')
    root.left = Node(2, 'r')
    root.right = Node(14, 'r')
    root.left.parent = root
    root.right.parent = root
    root.left.left = Node(1, 'k')
    root.left.right = Node(7, 'k')
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left = Node(15, 'k')
    root.right.right = Node(8, 'k')
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    tree = RBTree(root)  
    tree.delete(7)

    assert tree.Root.color == 'k'
    assert tree.get_node(1).parent.right.color == 'k'

    tree.delete_from([1, 2, 3])

    assert tree.Root.color == 'k'
