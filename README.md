# VantaTutorial

## Урок 1

### Задание 1

У вас есть N яблок и M человек (задаются с консоли). Необходимо распределить яблоки так, чтобы у всех их было поровну.

- Вывести количество яблок у каждого и остаток яблок (считаем, что яблоки делятся только нацело). Например, дано 5 яблок на 3 человека, каждому достанется по 1 яблоку и 2 яблока останутся.
- Вывести количество яблок у каждого и остаток яблок. Однако теперь яблоки могут делиться на половинки. Например, дано 5 яблок на 3 человека, каждому достанется по 1.5 яблока и 0.5 яблока останутся.

Требования к интерфейсу:
Выводить приветственные сообщения при вводе значений с указанием что и в каком порядке вводится (если вводятся несколько значений в одной строке)
Распечатать ответ используя форматирование строк (например, «Каждому достанется по А яблок, В яблок осталось»). Обратите внимание, что в русском языке есть падежи

### Задание 2

Дана последовательность слов (без знаков препинания), которая вводится в одну строку с консоли. Необходимо найти три наиболее длинных слова в последовательности. Если два слова имеют одинаковую длину, то среди них выбирается первое по алфавиту. Самостоятельно определить поведение программы, если в последовательности меньше трех слов.

Пример входных данных:
«Мама мыла раму пришел кот сломал телевизор»

Пример выходных данных:
«Три наиболее длинных слова
- Телевизор
- Пришел
- Сломал»

Требования к интерфейсу аналогичные предыдущей задаче.

### Задание 3

Натуральное число называется простым, если делится нацело только на само себя и на единицу (единица простым числом обычно не является). С консоли вводится число до 10 тысяч (но можно и больше). Нужно найти его наибольший простой делитель. Простым делителем называется простое число, на которое данное число делится нацело.

Пример входных данных:
100

Пример выходных данных:
5

Пример входных данных:
289

Пример выходных данных:
17

## Урок 2

### Задание 1

Python является объектно-ориентированным языком. Почти любая конструкция (не считая подавляющее большинство ключевых слов), которая есть в данном языке является объектом. Объект можно рассматривать как нечто живое, у него есть характеристики (атрибуты), поведение (методы). Объект совмещает себе как структуру данных, так и алгоритмы, которые ее обрабатывают.
Вам необходимо создать два класса: Человек и Питомец. При желании можно выделить над ними родительский класс.

Атрибуты человека: 
- Имя
- Возраст
- Пол
- Питомцы (список питомцев) 

Атрибуты питомца:
- Кличка
- Возраст
- Вид животного (кошка, собака, крыса, обезьяна...)
- Пол

Для запуска перейти в родительский каталог к каталогу Lesson 2 и исполнить в команду:

```
python3 -m 'Lesson 2'
```

## Урок 3

### Задание 1

Вы разрабатываете систему для приюта с котиками. Вам важно вести их учет, для этого нужно периодически сохранять список котов в формате JSON и в формате текстового файла (в формате «Кличка - Возраст - Порода»). Для реализации задачи можно использовать код, разобранный на занятии.

Более подробно: нужно создать обертку над списком котов, которая будет преобразовывать его в нужный для записи формат. При преобразовании отдельного кота можно использовать имеющийся код (в случае текстового файла написать еще один преобразователь кота в текстовый формат). Сделать тестовых котов и записать их список в файлы.

## Examples (Примеры)

Перед запуском примера нужно установить зависимости:
- FastAPI
- Jinja2
- Pydantic

Зависимости устанавливаются командой:
```
pip install <название библиотеки>
```

Для запуска перейти в каталог с файлом main.py и выполнить в командной строке:

```
fastapi run main.py
```
