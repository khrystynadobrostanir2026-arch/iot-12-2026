class Furniture:
    def __init__(self, name, coordinates):
        self._name = name
        self._coordinates = list(coordinates)

    def __del__(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_coordinates(self):
        return self._coordinates

    def set_coordinates(self, coordinates):
        self._coordinates = list(coordinates)

    def display(self):
        print(f"Об'єкт: {self._name}, Координати: {self._coordinates}")


class Bed(Furniture):
    def __init__(self, coordinates, material="Wood"):
        super().__init__("Bed", coordinates)
        self._material = material

    def display(self):
        print(f"Ліжко (Bed), Матеріал: {self._material}, Координати: {self._coordinates}")


class Table(Furniture):
    def __init__(self, coordinates, shape="Rectangle"):
        super().__init__("Table", coordinates)
        self._shape = shape

    def display(self):
        print(f"Стіл (Table), Форма: {self._shape}, Координати: {self._coordinates}")


class Carpet(Furniture):
    def __init__(self, coordinates, color="Blue"):
        super().__init__("Carpet", coordinates)
        self._color = color

    def display(self):
        print(f"Килим (Carpet), Колір: {self._color}, Координати: {self._coordinates}")


class Room:
    def __init__(self, name="Dream Room"):
        self._name = name
        self._items = []

    def __del__(self):
        pass

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item_name):
        self._items = [item for item in self._items if item.get_name() != item_name]

    def Rearrangement(self, item_name, new_coordinates):
        for item in self._items:
            if item.get_name() == item_name:
                item.set_coordinates(new_coordinates)

    def display_room(self):
        print(f"Кімната: {self._name}")
        for item in self._items:
            item.display()


if __name__ == "__main__":
    room = Room("Кімната моєї мрії")

    bed = Bed([0, 0, 0], "Velvet")
    table = Table([2, 3, 0], "Round")
    carpet = Carpet([1, 1, 0], "Beige")

    room.add_item(bed)
    room.add_item(table)
    room.add_item(carpet)

    room.display_room()

    print("\n--- Зміна координат (Rearrangement) ---")
    room.Rearrangement("Table", [4, 5, 0])
    room.display_room()

    print("\n--- Видалення об'єкта ---")
    room.remove_item("Carpet")
    room.display_room()