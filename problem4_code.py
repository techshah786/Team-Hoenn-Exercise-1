
from typing import List, Dict


class InventorySystem:
    def __init__(self):
        """Start with an empty inventory."""
        self._inventory: Dict[str, dict] = {}



    #helper methods
    def _check_text(self, value, field):
        """Make sure the given field is a non-empty string."""
        if not isinstance(value, str) or value.strip() == "":
            raise Exception(f"{field} must be a non-empty string.")

    def _check_nonnegative_int(self, value, field):
        """Make sure the given field is a non-negative integer (not bool)."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise Exception(f"{field} must be an integer.")
        if value < 0:
            raise Exception(f"{field} cannot be negative.")

    def _check_nonnegative_number(self, value, field):
        """Make sure the given field is a non-negative number (int or float)."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise Exception(f"{field} must be a number.")
        if value < 0:
            raise Exception(f"{field} cannot be negative.")



    def add_product(self, product_id: str, name: str, quantity: int, price: float):
        """
        Add a new product or update an existing one.
        Product IDs are unique.
        """
        # Validate inputs
        self._check_text(product_id, "product_id")
        self._check_text(name, "name")
        self._check_nonnegative_int(quantity, "quantity")
        self._check_nonnegative_number(price, "price")

        # If product_id exists, update it; otherwise add new
        if product_id in self._inventory:
            # Update existing product
            self._inventory[product_id].update(
                {"name": name, "quantity": quantity, "price": price}
            )
        else:
            # Add new product
            self._inventory[product_id] = {
                "id": product_id,
                "name": name,
                "quantity": quantity,
                "price": price,
            }

    def remove_product(self, product_id: str) -> bool:
        """
        Remove a product from inventory.
        Returns True if removed, False if product doesn't exist.
        """
        if product_id in self._inventory:
            del self._inventory[product_id]
            return True
        return False

    def get_inventory_value(self) -> float:
        """Calculate the total value of all products."""
        total = 0.0
        for item in self._inventory.values():
            total += item["quantity"] * item["price"]
        return total

    def search_products(self, keyword: str) -> List[dict]:
        """Find all products whose names contain the keyword (case-insensitive)."""
        keyword = keyword.lower()
        results = []
        for item in self._inventory.values():
            if keyword in item["name"].lower():
                results.append(
                    {
                        "id": item["id"],
                        "name": item["name"],
                        "quantity": item["quantity"],
                        "price": item["price"],
                    }
                )
        return results


if __name__ == "__main__":
    inventory = InventorySystem()
    inventory.add_product("A001", "Wise Glasses", 5, 1200.00)
    inventory.add_product("A002", "Muscle Band", 20, 25.50)

    print("Total inventory value:", inventory.get_inventory_value())
    print("Search 'mu':", inventory.search_products("mu"))

    # Updating an existing product
    inventory.add_product("A001", "Wise Glasses", 10, 1100.00)
    print("After update, value:", inventory.get_inventory_value())
