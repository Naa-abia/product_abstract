from abc import ABC, abstractmethod
from itertools import product

class Product:
    name = "Nido"
    type = "Essentia"
    price = "GHS 70"
    expiry_date = "12/12/34"
    weight = "1 KG"
    bar_code = 12321
    production_date = "12/23/12"

class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product:Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass 

class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print(f"Saving the product : {product.name}...\n") 

    def edit_product(self, product:Product):
        print(f"Hello Abia ! Change weight: {product.weight} ?")

    def get_product_by_id(self, product:Product):
        print(f"Hello Abia ! Searching for your product {product.bar_code}...Please wait a min. Thank you.")

    def upload_product_image(self):
        print("Hey there! Uploading your image....70%")

    def get_all_products(self):
        print("Fetching the list of all inventory, Please wait")

    def delete_product(self, product:Product):
        print(f"Deleting:{product.name},{product.weight}")

product_manager = ProductManager()
product_manager.create_product(product=Product)
product_manager.edit_product(product=Product)
product_manager.get_all_products()
product_manager.get_product_by_id(product=Product)
product_manager.upload_product_image()
product_manager.delete_product(product=Product)
