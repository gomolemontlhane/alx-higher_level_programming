#!/usr/bin/python3
"""
Module that defines the MyList class.
"""

class MyList(list):
    """
    MyList class, inherits from the list class.

    Public instance method:
    - def print_sorted(self): prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)
    my_list.print_sorted()
    print(my_list)
