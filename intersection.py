list_1 = ['apple', 'banana', 'orange', 'strawberry', 'kiwi', 'dragonfruit']
list_2 = ['blueberry', 'kiwi', 'strawberry', 'mango', 'dragonfruit']


solution = list(filter(lambda x: x in list_2, list_1))
print(solution)