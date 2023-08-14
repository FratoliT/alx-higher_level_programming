#!/usr/bin/python3
# prints intigers which are on the list

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
