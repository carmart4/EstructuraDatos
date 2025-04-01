# -*- coding: utf-8 -*-
"""

Test para Práctica 4

@date: 26/03/2025

"""


class LinkedList:

    """ Clase Nodo 
    Un nodo contiene un elemento de información, item y
    la referencia al nodo que le sucede en la secuencia, next
    """
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next # otro Nodo
        
        def GetItem(self):
            return self.item
        
        def GetNext(self):
            return self.next
        
        def SetItem(self, item):
            self.item = item
        
        def SetNext(self,next):
            self.next = next
            
    def __init__(self,contents=[]):
        self.__first = LinkedList.__Node(None,None)
        self.__last = self.__first
        self.__numItems = 0
        for e in contents:
            self.append(e)
           
    def __getitem__(self,index):
        if index >= 0 and index < self.__numItems:
            cursor = self.__first.GetNext()
            for i in range(index):
                cursor = cursor.GetNext() 
        else:
            raise IndexError("LinkedList \
                             index out of range")
        return cursor.GetItem()
    
    def __setitem__(self,index,val):
        if index >= 0 and index < self.__numItems:
            cursor = self.__first.GetNext()
            for i in range(index):
                cursor = cursor.GetNext() 
            cursor.SetItem(val)
        else:
            raise IndexError("LinkedList \
                             assignment index out of range") 
        return
        
    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))
        result = LinkedList()
        cursor = self.__first.GetNext()
        while cursor != None:
            result.append(cursor.GetItem())
            cursor = cursor.GetNext()
        cursor = other.__first.GetNext()
        while cursor != None:
            result.append(cursor.GetItem())
            cursor = cursor.GetNext()        
        return result
    
    def append(self,item):
        node = LinkedList.__Node(item)
        self.__last.SetNext(node)
        self.__last = node
        self.__numItems += 1
        
    def insert(self,index,item):
        cursor = self.__first
        if index < self.__numItems:
            for i in range(index):
                cursor = cursor.GetNext()
            node = LinkedList.__Node(item, cursor.GetNext())
            cursor.SetNext(node)
            self.__numItems += 1
        else:
            self.append(item)        
            
    def __str__(self):
        s = ""
        for i in range(self.__numItems):
            s += str(self[i]) 
            if i != self.__numItems - 1:
                s += ";"
        return s
            
def main():
    milista = LinkedList([1,2,3])
    print(milista)
    
    milista[0] = 987
    print(milista)
    
    otralista = LinkedList([4,5,6,7,8,9])
    
    l = milista + otralista
    print(l)
    
    print(l[3])

    
if __name__ == "__main__":
    main()    