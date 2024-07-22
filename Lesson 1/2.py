msg = input("Введите последовательность слов: \n") # вводим строку

words = msg.split() # делим ее на слова

# Функция сортировки
def sort_key(x: str):
    return (-len(x), x.lower()) 
    # сортируем по длине и по алфавиту (приводим к нижнему регистру, чтобы корректно сравнить большие и маленькие буквы)

words.sort(key=sort_key)

print("Три наиболее длинных слова:")
print(*words[:3])

