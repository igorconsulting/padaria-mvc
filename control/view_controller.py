from view.home_screen import HomeScreen
from view.display_builder import Display
from control.customer_controller import CustomerController
from control.product_controller import ProductController
from model.product import Product
from model.customer import Customer

class ViewController(Display):
    def __init__(self):
        super().__init__()
        self.home_screen = HomeScreen()
        self.product_controller = ProductController()
        self.customer_controller = CustomerController()

    def move_screen(self,command:str) -> None:
        """
        Moves the application to the appropriate screen based on the command.

        Args:
            command (str): The user's command input.
        """
        if command == '1':
            self.register_product()
        elif command == '2':
            self.register_customer()
        elif command == '3':
            self.search_customer_by_name()
        elif command == '4':
            self.search_customer_by_state()
        elif command == '5':
            self.search_product_by_name()
        elif command == '6':
            self.search_product_by_taste()
        elif command == '7':
            self.show_all_customers()
        elif command == '8':
            self.show_all_products()
        elif command == '0':
            self.show_message("Saindo do sistema. Obrigado!")
            exit()
        else:
            self.show_message("Comando inválido. Tente novamente.")

    def register_product(self):
        self.show_message("\n--- Register Product ---")
        name = input("Enter product name: ")
        taste = input("Enter product taste: ")
        price = input("Enter product price (e.g., 12.99): ")
        
        try:
            product = Product(name, taste, price)
            self.product_controller.add_product(product)
            self.show_message("Product registered successfully!")
        except ValueError as e:
            self.show_message(f"Error: {e}")

    def register_customer(self):
        self.show_message("\n--- Register Customer ---")
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        state = input("Enter customer state: ")
        
        customer = Customer(name, phone, state)
        self.customer_controller.add_customer(customer)
        self.show_message("Customer registered successfully!")

    def search_product_by_name(self):
        self.show_message("\n--- Search Product by Name ---")
        name = input("Enter product name to search: ")
        
        products = self.product_controller.get_all_products()
        found = [product for product in products if name.lower() in product.name.lower()]
        
        if found:
            for product in found:
                self.show_message(str(product))
        else:
            self.show_message("No products found with that name.")

    def search_product_by_taste(self):
        self.show_message("\n--- Search Product by Taste ---")
        taste = input("Enter product taste to search: ")

        cleaned_taste = taste.lower()
        
        products = self.product_controller.get_products_by_taste(cleaned_taste)

        if products:
            for product in products:
                self.show_message(str(product))
        else:
            self.show_message("No products found with that taste.")

    def search_customer_by_name(self):
        self.show_message("\n--- Search Customer by Name ---")
        name = input("Enter customer name to search: ")

        cleaned_name = name.lower()
        
        customers = self.customer_controller.get_customers_by_name(cleaned_name)
        
        if customers:
            for customer in customers:
                self.show_message(str(customer))
        else:
            self.show_message("No customers found with that name.")

    def search_customer_by_state(self):
        self.show_message("\n--- Search Customer by State ---")
        state = input("Enter customer state to search: ")

        cleaned_state = state.lower()
        
        customers = self.customer_controller.get_customers_by_state(cleaned_state)
        
        if customers:
            for customer in customers:
                self.show_message(str(customer))
        else:
            self.show_message("No customers found in that state.")

    def show_all_products(self):
        self.show_message("\n--- All Products ---")
        products = self.product_controller.get_all_products()
        
        if products:
            for product in products:
                self.show_message(str(product))
        else:
            self.show_message("No products found in the database.")

    def show_all_customers(self):
        self.show_message("\n--- All Customers ---")
        customers = self.customer_controller.get_all_customers()
        
        if customers:
            for customer in customers:
                self.show_message(str(customer))
        else:
            self.show_message("No customers found in the database.")

    def display(self) -> None:
        while True:
            command = self.home_screen.display()
            self.move_screen(command)
