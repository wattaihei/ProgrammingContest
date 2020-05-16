import sys
input = sys.stdin.readline

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 


class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.key == key: 
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check  
                        self.node.key = replacement.key 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            self.rebalance()
        else: 
            return
    
    def search(self,key):
        if self.node == None:
            return False
        if self.node.key > key:
            if self.node.left == None:
                return False
            else:
                return self.node.left.search(key)
        if self.node.key < key:
            if self.node.right == None:
                return False
            else:
                return self.node.right.search(key)
        return True # self.key == key
    
    def search_lower(self,key,key_lower=None):
        if self.node == None:
            return key_lower
        if self.node.key > key:
            if self.node.left == None:
                return key_lower
            else:
                return self.node.left.search_lower(key,key_lower)
        if self.node.key < key:
            key_lower = self.node.key
            if self.node.right == None:
                return key_lower
            else:
                return self.node.right.search_lower(key,key_lower)
        #self.key == key
        if self.node.left == None:
            return key_lower
        else:
            if key_lower == None:
                return self.node.left.end_higher(self.node.left.key)
            else:
                return max(key_lower,self.node.left.end_higher(self.node.left.key))
    
    def search_higher(self,key,key_higher=None):
        if self.node == None:
            return key_higher
        if self.node.key > key:
            key_higher = self.node.key
            if self.node.left == None:
                return key_higher
            else:
                return self.node.left.search_higher(key,key_higher)
        if self.node.key < key:
            if self.node.right == None:
                return key_higher
            else:
                return self.node.right.search_higher(key,key_higher)
        #self.key == key
        if self.node.right == None:
            return key_higher
        else:
            if key_higher == None:
                return self.node.right.end_lower(self.node.right.key)
            else:
                return min(key_higher,self.node.right.end_lower(self.node.right.key))
        
    
    def end_lower(self,end_lower_key):
        if self.node.left == None:
            return end_lower_key
        else:
            end_lower_key = self.node.left.key
            return self.node.left.end_lower(end_lower_key)
    
    def end_higher(self,end_higher_key):
        if self.node.right == None:
            return end_higher_key
        else:
            end_higher_key = self.node.right.key
            return self.node.right.end_higher(end_higher_key)
    
    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 



def main():
    S = list(input().rstrip())
    data = []
    Q = int(input())
    for _ in range(Q):
        A = list(map(str, input().split()))
        data.append(A)

    dic = {}
    for i, s in enumerate(S):
        if not s in dic.keys():
            rs = AVLTree()
            rs.insert(i)
            dic[s] = rs
        else:
            dic[s].insert(i)

    for A in data:
        if A[0] == '1':
            l, s = int(A[1])-1, A[2]
            for al, root in dic.items():
                if root.search(l):
                    dic[al].delete(l)
            if not s in dic.keys():
                rs = AVLTree()
                rs.insert(l)
                dic[s] = rs
            else:
                dic[s].insert(l)

        elif A[0] == '2':
            count = 0
            l, r = int(A[1])-1, int(A[2])-1
            for root in dic.values():
                if root.search(l) or root.search(r) or root.search_higher(l) != root.search_higher(r):
                    count += 1
            print(count)

if __name__ == "__main__":
    main()