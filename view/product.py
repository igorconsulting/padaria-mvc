class ProductView:
    def input_product_data(self):
        name = input("Enter product name: ")
        taste = input("Enter product taste: ")
        price = input("Enter product price (e.g., 12.99): ")

        return name,taste,price

    def show_product(self, product):
        print(str(product))

    def show_products(self, products):
        if not products:
            print("No products found.")
        for product in products:
            self.show_product(product)

    def show_message(self, message):
        print(message)