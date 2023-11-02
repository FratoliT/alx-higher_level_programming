#!/usr/bin/python3
"""Locked class"""

class LockedClass:
"""prevents the user from intializing anything except first_name. """

  __slots__ = ["first_name"]
