#!/usr/bin/env python
# Author: Tyler Sanderson <tylerbtbam@gmail.com>
#
# This file is part of PyBST.
#
# PyBST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyBST.  If not, see <http://www.gnu.org/licenses/>.

import collections

class Node:
    def __init__(self,key,value):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value

class BSTree:
    def __init__(self,*args):

        self.Root = None

        if len(args) == 1:
            if isinstance(args[0],collections.Iterable):
                for x in args[0]:
                    self.insert(x[0],x[1])
            else:
                raise TypeError(str(args[0]) + " is not iterable")

    def is_valid(self, *args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node:
            return True

        if node.left:
            if not node.left.parent == node:
                raise Exception("Left child of node " + str(node.key) + " is adopted by another node!")

        if node.right:
            if not node.right.parent == node:
                raise Exception("Right child of node " + str(node.key) + " is adopted by another node!")

        if node.parent and node.parent.left == node:
            if node.key > node.parent.key:
                raise Exception("Node " + str(node.key) + " is to the left of " + str(node.parent.key) + " but is larger")

        if node.parent and node.parent.right == node:
            if node.key < node.parent.key:
                raise Exception("Node " + str(node.key) + " is to the right of " + str(node.parent.key) + " but is smaller")

        return (self.is_valid(node.left) and self.is_valid(node.right))

    def preorder(self,*args):
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        elements.append(node)

        if node.left:
            self.preorder(node.left,elements)
        if node.right:
            self.preorder(node.right,elements)

        return elements

    def inorder(self,*args):
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        if node.left:
            self.inorder(node.left,elements)

        elements.append(node)

        if node.right:
            self.inorder(node.right,elements)

        return elements

    def postorder(self,*args):
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        if node.left:
            self.postorder(node.left,elements)

        if node.right:
            self.postorder(node.right,elements)

        elements.append(node)

        return elements

    def levelorder(self):
        q = collections.deque()
        q.appendleft(self.Root)
        lst = []
        while len(q) != 0:
            removed = q.pop()
            lst.append(removed)
            visit = self.get_node(removed,self.Root)
            if visit.left:
                q.appendleft(visit.left)
            if visit.right:
                q.appendleft(visit.right)

        return lst

    def get_node(self,key,*args):
        if len(args) == 0:
            start = self.Root
        else:
            start = args[0]

        if not start:
            return None
        if key == start.key:
            return start
        elif key > start.key:
            return self.get_node(key,start.right)
        else:
            return self.get_node(key,start.left)

    def insert(self,key,value,*args):
        if not isinstance(key,(int,long,float)):
            raise TypeError(str(key) + " is not a number")
        else:
            if not self.Root:
                self.Root = Node(key,value)
            elif len(args) == 0:
                if not self.get_node(key,self.Root):
                    self.insert(key,value,self.Root)
            else:
                child = Node(key,value)
                parent = args[0]
                if child.key > parent.key:
                    if not parent.right:
                        parent.right = child
                        child.parent = parent
                    else:
                        self.insert(key,value,parent.right)
                else:
                    if not parent.left:
                        parent.left = child
                        child.parent = parent
                    else:
                        self.insert(key,value,parent.left)

    def insert_from(self,seq):
        if isinstance(seq,collections.Iterable):
            for x in seq:
                self.insert(x[0],x[1])
        else:
            raise TypeError(str(iter) + " is not iterable")

    def get_max(self,*args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node.right:
            return node
        else:
            return self.get_max(node.right)

    def get_min(self,*args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node.left:
            return node
        else:
            return self.get_min(node.left)

    def get_element_count(self,*args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        left = 0
        right = 0

        if node:
            if node.left:
                left = self.get_element_count(node.left)
            if node.right:
                right = self.get_element_count(node.right)

            return 1 + left + right
        else:
            return 0

    def get_height(self,*args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node or (not node.left and not node.right):
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def _delete_leaf(self,node):
        par_node = node.parent

        if par_node:
            if par_node.left == node:
                par_node.left = None
            else:
                par_node.right = None

            del node

    def _delete_leaf_parent(self,node):
        par_node = node.parent

        if node.key == self.Root.key:
            if node.right:
                self.Root = node.right
                node.right = None
            else:
                self.Root = node.left
                node.left = None

        else:
            if par_node.right == node:
                if node.right:
                    par_node.right = node.right
                    par_node.right.parent = par_node
                    node.right = None
                else:
                    par_node.right = node.left
                    par_node.right.parent = par_node
                    node.left = None
            else:

                if node.right:
                    par_node.left = node.right
                    par_node.left.parent = par_node
                    node.right = None
                else:
                    par_node.left = node.left
                    par_node.left.parent = par_node
                    node.left = None

        del node

    def _switch_nodes(self,node1,node2):
        switch1 = node1
        switch2 = node2
        temp_key = switch1.key
        temp_value = switch1.value

        if switch1.key == self.Root.key:
            self.Root.key = node2.key
            self.Root.value = node2.value
            switch2.key = temp_key
            switch2.value = temp_value

        elif switch2.key == self.Root.key:
            switch1.key = self.Root.key
            self.Root.key = temp_key
            self.Root.value = temp_value
        else:
            switch1.key = node2.key
            switch1.value = node2.value
            switch2.key = temp_key
            switch2.value = temp_value

    def _delete_node(self,node):
        if self.get_height(node.left) > self.get_height(node.right):
            to_switch = self.get_max(node.left)
            self._switch_nodes(node,to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = self.get_max(node.left)
                self._delete_leaf(to_delete)
            else:
                to_delete = self.get_max(node.left)
                self._delete_leaf_parent(to_delete)
        else:
            to_switch = self.get_min(node.right)
            self._switch_nodes(node,to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = self.get_min(node.right)
                self._delete_leaf(to_delete)
            else:
                to_delete = self.get_min(node.right)
                self._delete_leaf_parent(to_delete)

    def delete(self,key):
        node = self.get_node(key,self.Root)

        if node:
            if not (node.left or node.right):
                self._delete_leaf(node)

            elif not (node.left and node.right):
                self._delete_leaf_parent(node)

            else:
                self._delete_node(node)

    def delete_from(self,seq):
        if isinstance(seq,collections.Iterable):
            for x in seq:
                self.delete(x)
        else:
            raise TypeError(str(iter) + " is not iterable")
