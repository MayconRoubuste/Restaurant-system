"""
Product: Represent menu items, like food and drinks
Order: To manage items asked by the client
Restaurant: To manage menu and client's orders
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        return f'Product: {self.name}, Price: {self.price}'


class Order:
    def __init__(self):
        self.item = []

    def add_product(self, product):
        self.item.append(product)

    def calc_total(self):
        total = sum(product.price for product in self.item)
        return total

    def show_info(self):
        info = 'Order items: \n'
        for product in self.item:
            info += f'- {product.show_info()}\n'
        info += f'Total: R${self.calc_total():.2f}'
        return info


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_product_to_menu(self, product):
        self.menu.append(product)

    def list_menu(self):
        for product in self.menu:
            print(product.show_info())

    def create_order(self):
        return Order()


def main():
    restaurant = Restaurant()

    # Adding products to menu
    restaurant.add_product_to_menu(Product('French Fries', 16.00))
    restaurant.add_product_to_menu(Product('Pork Chops', 25.00))
    restaurant.add_product_to_menu(Product('T-bone', 30.00))
    restaurant.add_product_to_menu(Product('Cream brule', 27.30))
    restaurant.add_product_to_menu(Product('Soda', 6.00))

    order = restaurant.create_order()

    while True:
        print('\n1. Show menu')
        print('2. Add product to order')
        print('3. Show order and total')
        print('4. Exit')

        choice = input('What the user wants to do? ')

        if choice == '1':
            print('Menu: ')
            restaurant.list_menu()

        elif choice == '2':
            product_name = input('Type the product name you wish to add to the order: ')
            for product in restaurant.menu:
                if product.name.lower() == product_name.lower():
                    order.add_product(product)
                    print(f'{product_name} added to order.')
                    break
            else:
                print('Product not found')

        elif choice == '3':
            print('Order resume: ')
            print(order.show_info())

        elif choice == '4':
            print('Exiting...')
            break


if __name__ == '__main__':
    main()
