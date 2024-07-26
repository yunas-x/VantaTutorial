class File:

    folder = "/Users/yunas_x/Documents/VantaProgramingIntro/Lesson 3/jsons/"

    def __init__(self, file_name: str) -> None:
        self.path = File.folder + file_name

    def write(self, content: str):
        # Мы могли бы сюда преобразование
        # Но если бы нам пришлось бы менять
        # Пришлось бы занова все тестировать
        with open(self.path, "w") as fp:
            fp.writelines(content)