immutable_var = 3, 5.5, 'Hello', True, ['Bye', 12]
print(immutable_var)

# immutable_var[1] = 5
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Почитав информацию на разных источниках, пришел к выводу, что кортежи существуют для исключения
# случайного изменения данных в больших проектах и предотвращения дальнейшего мучительного поиска ошибки.
# Вобщем для облегчения работы

mutable_list = [3, 5.5, 'Hello', True]
mutable_list[2] = 'Bye'
mutable_list[3] = 3 > 5
print(mutable_list)
