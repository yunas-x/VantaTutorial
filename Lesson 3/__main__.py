from Cat import Cat, CatSpecies
from CatJSONConverter import CatJSONConverter
from JSONFile import JSONFile

cat = Cat("Moorzik", 2, 1, CatSpecies.British)
cat_json = CatJSONConverter(cat).convert()

try:
    JSONFile("moorzik.json").write(cat_json)
except TypeError:
    print("Не тот тип")
except ValueError:
    print("Плохой путь")
except Exception:
    print("Ошибка")
