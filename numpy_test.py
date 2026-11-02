import numpy as np

# Define a 1D array
my_array = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]],
                    dtype=np.int64)
# Define a 2D array
my_2d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]],
                       dtype=np.int64)
# Define a 3D array
my_3d_array = np.array([[[1, 2, 3, 4],
                         [5, 6, 7, 8]],
                        [[1, 2, 3, 4],
                         [9, 10, 11, 12]]],
                       dtype=np.int64)
# Print the 1D array
print("Printing my_array:")
print(my_array)
# Print the 2D array
print("Printing my_2d_array:")
print(my_2d_array)
# Print the 3D array
print("Printing my_3d_array:")
print(my_3d_array)

# Printing my_array:st_project\pdf\my_practice\test_zone>
# [[1 2 3 4]
#  [5 6 7 8]]
# Printing my_2d_array:
# [[1 2 3 4]
#  [5 6 7 8]]
# Printing my_3d_array:
# [[[ 1  2  3  4]
#   [ 5  6  7  8]]

#  [[ 1  2  3  4]
#   [ 9 10 11 12]]]


print('Атрибуты')
my_2d_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int32)

# Print out memory address
print(my_2d_array.data)

# Print out the shape of `my_array`
print(my_2d_array.shape)

# Print out the data type of `my_array`
print(my_2d_array.dtype)

# Print out the stride of `my_array`
print(my_2d_array.strides)

# <memory at 0x00000242F90B35E0>
# (2, 4)
# int64
# (32, 8)

print('Создание массивов')

ones = np.ones((3,4)) # заполняет единицами float
print(ones) 

zeros = np.zeros((2,3,4), dtype = np.int16) # заполняет нулями
print(zeros)

random = np.random.random((2,2)) # float точность 8 знаков, набор случайных
print(random)

empty = np.empty((3,7)) # я даже не знаю, экспоненциальные
print(empty)

full = np.full((2,2),7) # заполняет указанным значением 7
print(full)

arange = np.arange(10,26,5) # от 10 до 25, с шагом 5, последний не включён
print(arange)

print(np.linspace(0,2,9)) # float от 0 до 2, длина 9, равномерный разброс 

print( np.eye(3,5,2) ) # диагональ в единичках, последний параметр смещает диагональ

print(np.identity(3)) # квадратная в единичках

print('Дополнительные функции')
# Create a numpy array with shape (2,4) and dtype int64
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

print("Количество измерений массива my_array:")
print(my_array.ndim)
print()

print("Number of elements in my_array:")
print(my_array.size)
print()

print("Information about the memory layout of my_array:")
print(my_array.flags)
print()

print("Length of one array element in bytes:")
print(my_array.itemsize)
print()

print("Total consumed bytes by my_array's elements:")
print(my_array.nbytes)
print()

print()
print('Операции над массивами')
print()

x = np.ones((5,5))
z = np.random.random((5,5))
print(x.shape, z.shape)
c = z + x
print(c)
print()
print('Разноразмерные')

x = np.array([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]],
            dtype=np.int64 )
y = np.random.random((5, 1, 4))
print(x, x.shape)
print(y, y.shape)
c = x + y
print(c, c.shape)

print('Некоторые тесты арифметики')
print('Некоторые тесты арифметики')
print('Некоторые тесты арифметики')
x = np.array([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]],
            dtype=np.int64 )
print(x.sum(),end='\n')
print(x.min(),end='\n')
print(x.max(),end='\n')
print(x.max(axis=1),end='\n')
print(x.max(axis=0),end='\n')
print(x.cumsum(),end='\n')
print(x.cumsum(axis=1),end='\n')
print(x.cumsum(axis=0),end='\n')
print(x.mean(),end='\n\n')
print(x.std())

print('Подмножества')
print('Подмножества')
print('Подмножества')
my_2d_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

print(my_2d_array[1][2])
print(my_2d_array[1,2])

my_3d_array = np.array([
    [[1,2,3,4], [5,6,7,8]],
    [[1,2,3,4], [9,10,11,12]]
    ], dtype=np.int64)

# Print subset
print(my_3d_array[1,1,2])

# Initialize 2D array
my_2d_array = np.array([
    [1,2,3,4], 
    [5,6,7,8], 
    [9,10,11,12]
    ], dtype=np.int64)

# Print subsets
print(my_2d_array[0:2,1])

# Initialize 3D array
my_3d_array = np.array([
    [[1,2,3,4], [5,6,7,8]],
    [[1,2,3,4], [9,10,11,12]]
    ], dtype=np.int64)

# Полный срез с [[ 1  2  3  4] [ 9 10 11 12]]
print(my_3d_array[1,...])


print('продвинутая индексация')
print('продвинутая индексация')
print('продвинутая индексация')
my_array = np.array([1,2,3,4])
my_3d_array = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [9,10,11,12]]], dtype=np.int64)

# Try out a simple example
print(my_array[my_array<2])

# Specify a condition
bigger_than_3 = (my_3d_array >= 3)

# Use the condition to index our 3d array
print(my_3d_array[bigger_than_3])
print('=========')

my_2d_array = np.array([
    [1,2,3,4], 
    [5,6,7,8]
    ], dtype=np.int64)

# Select elements at (1,0), (0,1), (1,2) and (0,0)
print(my_2d_array[[1, 0, 1, 0],[0, 1, 2, 0]])
# Select a subset of the rows and columns
print(my_2d_array[[1, 0, 1, 0]][:,[0,1,2,0]])
# [1, 0, 1, 0]
    # [5,6,7,8]
    # [1,2,3,4]
    # [5,6,7,8]
    # [1,2,3,4]
# [:,[0,1,2,0] ":" Указывает на то что берём все строки из промежуточного массива
#  а дальше выборка по последовательности колонок [0,1,2,0]
    # [5,6,7,8] -> [5,6,7,5]
    # [1,2,3,4] -> [1,2,3,1]
    # [5,6,7,8] -> [5,6,7,5]
    # [1,2,3,4] -> [1,2,3,1]
my_3d_array = np.array([
    [[1,2,3,4], [5,6,7,8]], 
    [[1,2,3,4], [9,10,11,12]]
    ], dtype=np.int64)


print('транспонировать массивы ')
print('транспонировать массивы ')
print('транспонировать массивы ')

my_2d_array = np.array([
    [1,2,3,4], 
    [5,6,7,8]
    ], dtype=np.int64)

print(my_2d_array)
print(my_2d_array.shape)
print(np.transpose(my_2d_array))
print(my_2d_array.T)


print('resize')
print('resize')
print('resize')
x = np.ones((3,4))
print(x)
t = np.resize(my_2d_array, (2, 2, 5))
print(t)

t = np.reshape(my_2d_array, (4,2))
print(t)

t = np.reshape(my_2d_array, (8,1))
print(t)

t = np.reshape(my_2d_array, (2, 2, 2))
print(t)

t = np.pad(my_2d_array, [2,5], mode = 'constant')
print(t)

t = np.repeat(my_2d_array, 2, axis=1)
print(t)


print('Добавлять ')
print('Добавлять ')
print('Добавлять ')

arr = np.array([
    [1,2,3,4], 
    [5,6,7,8]
    ], dtype=np.int64)
t = np.append(arr, [[12,13,14,15],[121,131,141,151]], axis=0)
print(arr)
print(t)


my_array = np.array([1,2,3,4])
my_2d_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

# Insert `5` at index 1
print(np.insert(my_2d_array, 1, 5))

# Delete the value at index 1
print(np.delete(my_2d_array,[1]))

print()
print('слиянее разъединение')
print('слиянее разъединение')
print('слиянее разъединение')
print()

x = np.ones((4,))
my_array = np.array([1,2,3,4])
my_resized_array=np.resize(my_array,(2,4))
my_2d_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(my_2d_array)

# Concatentate `my_array` and `x`
print(np.concatenate((my_array,x)))

# Stack arrays row-wise
print(np.vstack((my_resized_array, my_2d_array)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.stack((a, b))

# Stack arrays row-wise
print(np.r_[my_resized_array, my_2d_array])

# Stack arrays horizontally
print(np.hstack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.column_stack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.c_[my_resized_array, my_2d_array])

print(np.histogram(my_2d_array))
print(np.histogram(my_3d_array, bins=range(0,13)))
