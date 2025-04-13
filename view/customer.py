class CustomerView:
    def input_customer_data(self):
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        state = input("Enter customer state: ")
        return name, phone, state

    def show_customer(self, customer):
        print(str(customer))

    def show_customers(self, customers):
        if not customers:
            print("No customers found.")
        for customer in customers:
            self.show_customer(customer)

    def show_message(self, message: str):
        print(message)
