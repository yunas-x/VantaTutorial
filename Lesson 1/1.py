apples = int(input("Введите количество яблок: "))
people = int(input("Введите количество человек: "))

# apples_to_person = apples // people
# remainder = apples % people

apples_to_person, remainder = divmod(apples, people) # Находим одновременно и частное и остаток от деления

### Подумать как справиться с падежами!!!

#if apples_to_person == 1:
#    m = "яблоко"
#    ...
#elif pples_to_person in range(2, 5):
#    m = "яблока"
#    ...

msg = f"Каждому достанется {apples_to_person} яблок, останется {remainder} яблок" # Форматирование строк с помощью f-строк

print(msg)