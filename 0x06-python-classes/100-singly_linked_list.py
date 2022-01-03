#!/usr/bin/python3
"""This module defines two classes: Node and SinglyLinkedList"""


class Node:
    """defines the node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes instances of the Node
        Args:
            data (int): The data of the New node
            next_node (Node): The next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the value of the data of the Node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Returns the next Node of the linked list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the value of the next node of the list"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes instances of the SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        of the SinglyLinkedList(in increasing order)"""
        my_node = Node(value)
        if self.__head is None:
            self.__head = my_node
        elif self.__head.data > value:
            my_node.next_node = self.__head
            self.__head = my_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            my_node.next_node = temp.next_node
            temp.next_node = my_node

    def __str__(self):
        """prints the SinglyLinkedList to stdout, one Node number per line"""
        my_str = ""
        while self.__head is not None:
            my_str += str(self.__head.data)
            if self.__head.next_node is not None:
                my_str += '\n'
            self.__head = self.__head.next_node
        return ("".join(my_str))
