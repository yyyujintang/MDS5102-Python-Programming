#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q4_new.py
@Time    :   2021/10/04 16:57:07
@Finish  :   2021/10/04 19:27:34
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''


class Node():
    def __init__(self,element,parent=None,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

class Tree():
    def __init__(self):
        self.root = None
    def get_root(self):
        return self.root
    def insert(self,val):
        # 1.Establish a new node
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return True
        else:
            current = self.root
            parentNode = None
            while current is not None:
                parentNode = current
                if current.element > val:
                    current = current.left
                    if current is None:
                        parentNode.left = newNode
                        return True
                else:
                    current = current.right
                    if current is None:
                        parentNode.right = newNode
                        return True
        return False
    def search(self,val):
        if self.root is None:
            return None
        q = [self.root]
        p = []
        res = [self.root.element]
        while q != []:
            pop_node = q.pop(0)
            p.append(pop_node)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.element)
 
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.element)
        # if val in res:
        #     return val
        for i,ele in enumerate(res):
            if ele == val:
                return p[i]
    def delete(self):
        if self.root.left == None:
            pass
        else:
            self.root.left = None
        if self.root.right == None:
            pass
        else:
            self.root.right = None
        if self.root == None:
            pass
        else:
            self.root = None
    def printTree(self):
        if self.root is None:
            print("Nothing in Tree")
        else:
            q = [self.root]
            res = [self.root.element]
            while q != []:
                pop_node = q.pop(0)
                if pop_node.left is not None:
                    q.append(pop_node.left)
                    res.append(pop_node.left.element)
    
                if pop_node.right is not None:
                    q.append(pop_node.right)
                    res.append(pop_node.right.element)

            print("Values in tree:\n",sorted(res))



        
def main():
    tree = Tree()
    tree.insert(8)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(15)
    tree.printTree()

    print(tree.search(10))
    print(tree.search(10).element)
    print(tree.search(20))

    tree.delete()
    tree.printTree()

    content = [1,5,99,15,100,35,23,20,16,13]
    for num in content:
        tree.insert(num)
    tree.printTree()

main()



