"""
Тесты Binary Search Tree  

Вставка/Поиск/Удаление
"""

#======================================================
# копия исходника, для посмотреть
#======================================================


# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

# def insert(root, newValue):
#     if root is None:
#         root = BinaryTreeNode(newValue)
#         return root
#     if newValue < root.data:
#         root.leftChild = insert(root.leftChild, newValue)
#     else:
#         root.rightChild = insert(root.rightChild, newValue)
#     return root

# def search(root, value):
#     if root is None:
#         return False
#     elif root.data == value:
#         return True
#     elif root.data > value:
#         return search(root.leftChild, value)
#     else:
#         return search(root.rightChild, value)

# root = insert(None, 50)
# insert(root, 20)
# insert(root, 53)
# insert(root, 11)
# insert(root, 22)
# insert(root, 52)
# insert(root, 78)

# print(root.data)
# print(root.leftChild.data)
# print(root.rightChild.data)


# ========================================
# переписал потестить потрогать
# ========================================

# class BST:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None

# def insert(root, new_value):
#     if root is None:
#         root = BST(new_value)
#         return root
#     if root.data < new_value:
#         root.right_child = insert(root.right_child, new_value)
#     else:
#         root.left_child = insert(root.left_child, new_value)
#     return root

# def search(root, value):
#     if root is None: 
#         return False
#     elif root.data == value:
#         return True
#     elif root.data < value:
#         return search(root.right_child, value)
#     else:
#         return search(root.left_child, value)

# root = insert(None, 50)
# insert(root, 20)
# insert(root, 53)
# insert(root, 11)
# insert(root, 22)
# insert(root, 52)
# insert(root, 78)

# print(root.data)
# print(root.left_child.data)
# print(root.right_child.data)


# ========================================
# Должно быть удаление узлов, хочу сам
# имена изломаны, не хочу ничего придумывать и повторяться
# ========================================
class BST:
    def __init__(self,data):
        self.data = data
        self.lch = None 
        self.rch = None

def insert(root, nval, /):
    if root is None:
        root = BST(nval)
        return root
    if root.data < nval:
        root.rch = insert(root.rch, nval)
    else: 
        root.lch = insert(root.lch, nval)
    return root

def search(root, val, /):
    if root is None:
        return False
    elif root.data == val:
        return True
    elif root.data < val:
        return search(root.rch, val)
    else:
        return search(root.lch, val)

root = insert(None, 30)
insert(root, 55)
insert(root, 50)
insert(root, 53)
insert(root, 58)
insert(root, 57)
insert(root, 42)
insert(root, 14)
insert(root, 10)

print(search(root,50))

# Попробую сделать самостоятельно удаление
# я думаю что это должно работать по типу вставки только с none

# print('========= delete 50 ручками')
# print(root.data)
# print(root.rch.data)
# root.rch.lch = None # тут 50
# print(root.rch.lch)
# так хорошо. руками это работает.
# print(search(root,42))
# print('========= delete')

def delete(root, val, /):
    if root.data == val:
        root = None
    elif root.data < val:
        root.rch = delete(root.rch, val)
    else:
        root.lch = delete(root.lch, val)
    return root

print('========= delete')
delete(root, 50)
print('========= search 50')
print(search(root,50))
print('========= search 42')
print(search(root,42))

# вывод
# True
# ========= delete
# ========= search 50
# False
# ========= search 42
# False


# Рекурсивная версия есть. 
# Думаю как и с бинарным поиском должна быть итеративная