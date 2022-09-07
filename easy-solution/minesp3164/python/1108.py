class Solution(object):
    def defangIPaddr(self, address):
        list = address.split(".")
        return "[.]".join(list)