
class TreeNode(object):
    def __init__(self, val, data):
        self.val = val
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
 
class AVL_Tree(object):
    def insert(self, root, key,data):
        if not root:
            return TreeNode(key,data)
        elif key < root.val:
            root.left = self.insert(root.left, key,data)
        else:
            root.right = self.insert(root.right, key,data)
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root, ls):
 
        if not root:
            return
        self.preOrder(root.left,ls) vb
        print("{0} ".format(root.val), end="")
        ls.append((root.val,root.data))
        
        self.preOrder(root.right,ls)
        
 
 
# Driver program to test above function
myTree = AVL_Tree()
root = None
 
"""root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)"""
 







vowels=['a','e','i','o','u']
word='ghuntee'
dictionary = {
    "bhunno" : ["fry"],
    "mange" : ["want","ask","need","desire"],
    "waqt" : ["time"],
    "kar" : ["do"],
    "hai" : ["exist","it's"],
    "yeh" : ["this","it"],
    "masala" : ["spices"],
    "jub" : ["when"],
    "ki" : ["belong"],
    "ghanti" : ["bell","alarm"],
    "baji" : ["ring"]
}
"""consonant_priority = 1
vowel_priority = 0.1
class tree:
    def __init__(self):
        self.branch={}
        self.value=None
    def add(self,i):
        if len(i)!=0:
            if not i[0] in self.branch:
                self.branch[i[0]] = tree()
            self.branch[i[0]].add(i[1:])
    def preorder(self):
        for i in self.branch.keys():
            print(i)
            self.branch[i].preorder()
            
t=tree()
for i in dictionary.keys():
    t.add(i)
t.preorder()
    
for i in range(len(word)):
    consonant = not word[i] in vowels
"""

def parse(s):
    k=[]
    c=''
    v = s[0] in vowels
    for i in s:
        if v and i in vowels:
            c += i
        elif not v and not i in vowels:
            c += i
        else:
            k.append(c)
            c = i
            v = not v
    k.append(c)
    return k

mat = 'ghanti'

#print(parse(word))
#print(parse(mat))

def similar(giv,dic):
    a1 = parse(giv)
    a2 = parse(dic)
    pen = 0
    if len(a2) != len(a1):
        pen = -abs(len(a2)-len(a1))
    for i in range(min(len(a1),len(a2))):
        if a2[i]!=a1[i]:
            if a2[i][0] in vowels: pen -= 1
            else: pen -= 10
    return pen

#print(similar(word,mat))
print("Similarity for "+word)

for i in dictionary.keys():
    #print(i,similar(word,i))
    root = myTree.insert(root,similar(word,i),i)

ls = []
myTree.preOrder(root,ls)
print(ls)

"""class Wor:
    def __init__(self,c):
        if c in ['a','e','i','o','u']:
            self."""

