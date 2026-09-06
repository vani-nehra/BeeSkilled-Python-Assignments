class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:

    def __init__(self):
        self.products = []
        self.tax_rate = 18

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.total_price()

        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()

        return subtotal + tax

    def display_bill(self):

        print("\n")
        print("=" * 55)
        print("                    BILL")
        print("=" * 55)

        print(f"{'Product':<20}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 55)

        for product in self.products:
            total = product.total_price()

            print(
                f"{product.name:<20}"
                f"{product.price:<10}"
                f"{product.quantity:<10}"
                f"{total:<10}"
            )

        print("-" * 55)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':<40}{subtotal:.2f}")
        print(f"{'Tax (18%)':<40}{tax:.2f}")
        print(f"{'Grand Total':<40}{total:.2f}")

        print("=" * 55)



product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 500, 2)
product3 = Product("Keyboard", 1000, 1)

bill = Bill()

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

bill.display_bill()