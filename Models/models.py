# models.py
import json

class Item:
    def __init__(self, quantity: int, name: str):
        self.quantity = quantity
        self.name = name


class ShopList:
    def __init__(self):
        self.list_of_items = []
        self.backup_list_of_items = []
        self.categories = self.load_categories()

    def load_categories(self):
        with open("C:\Projects\Bots\pythonProject1\Categories\categories.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def add_item(self, quantity: int, name: str):
        self.list_of_items.append(Item(quantity, name))

    def add_item(self, quantity: int, name: str):
        self.list_of_items.append(Item(quantity, name))

    def remove_item(self, name: str):
        for item in self.list_of_items:
            if item.name == name:
                self.list_of_items.remove(item)
                return True
        return False

    def display(self):
        if self.list_of_items.__len__() == 0:
            return False
        categorized_items = self.categorize_items()
        display_output = []
        for category, items in categorized_items.items():
            display_output.append(f"{category}:")
            for item in items:
                display_output.append(f" - {item.quantity} {item.name}")
            display_output.append("")
        return "\n".join(display_output)

    def update_item_quantity(self, name: str, quantity: int) -> bool:
        for item in self.list_of_items:
            if item.name == name:
                item.quantity = quantity
                return True
        return False

    def categorize_items(self):
        sorted_items = {"שונות": []}
        flag = True
        for item in self.list_of_items:
            categorized = False
            for category, keywords in self.categories.items():
                if any(keyword in item.name for keyword in keywords):
                    if category not in sorted_items:
                        sorted_items[category] = []
                    sorted_items[category].append(item)
                    categorized = True
                    break
            if not categorized:
                if flag:
                    sorted_items["שונות"] = []
                    flag = False
                sorted_items["שונות"].append(item)
        result = {k: sorted_items[k] for k in sorted_items if k != "שונות"}
        result["שונות"] = sorted_items["שונות"]
        return result

    def reset(self) -> None:
        self.backup_list_of_items = self.list_of_items.copy()
        self.list_of_items.clear()

    def restore(self):
        self.list_of_items = self.backup_list_of_items.copy()