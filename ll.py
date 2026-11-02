""" Связный список """

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # head = Node(100)
# # second_node = Node(200)

# # это наследник или что ? Если я не ошибаюсь это композиция
# # по идее мы в объект передали другой клас с свойством "data" 
# # в итоге у нас есть как бы класс в классе
# # вызов длинноват
# # head.next = second_node
# # print(head.data, head.next.data)

# # Инициализируем класс связного списка
# class Linked_list:
#     def __init__(self):
#         self.head = None

#     # стандартный метод для добавления элемента
#     def append(self, val):
#         new_node = Node(val)

#         # Устанавливаем шапку если её нет 
#         if self.head is None:
#             self.head = new_node
#             return
#         # текущий элемент присваивается класс Node
#         current = self.head

#         # Если метод next класса Node не None
#         # Тогда текущим становится Next
#         # не понимаю
#         # в current объект Node можно запросить next
#         # если в текущем объекте ноды next не пуст, то. Стоп. Рисуй графраспределения
#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     def traverse(self):
#         current = self.head

#         while current is not None:
#             print(current.data)
#             current = current.next

# ll = Linked_list()
# ll.append(10)
# # ll.append(200)

# print(ll.traverse())
# # Всё правильно работает

# Связный список Еще раз. на бумажке я понял
# Так, сначала план, что мы делаем
# Первое что нужно сделать это прописать класс узла
# Он нам нужен чтобы записывать данные и переключаться, но всё в ручную
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 

# node = Node('например текст')
# node_next = Node('какой-то дополнительный узел данных')
# #  сейчас задача связать в одну часть всё
# node.next = node_next
# print(node.value)        
# print(node.next.value)
# # И так всё получилось
# # связные списки используются тогда когда нужно перемещаться по элементам вперёд и назад
# # обычный список не позволяет так делать
# # сейчас нужно написать слой который будет автоматически добавлять элемент в список и устанавливать его следующую часть последовательности
# # нам нуден класс связка, с функцией добавления элемента и перебор по списку
# # вообще я представляю себе это как лесенку где нам нужно двигаться по ступеням вперёд
# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def append(self,value): # стандартное имя метода
#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     def traverse(self):
#         current = self.head

#         while current is not None:
#             print(current.value)
#             current = current.next

# ll = Linked_list()
# ll.append(10)
# ll.append(100)
# ll.traverse()




#########################################
#            # Связный список
#########################################