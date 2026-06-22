from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hi this is my first api"

products = [
    Product(id=1,name="mobile", description="moto edge 60", price=99.99, quantity=10),
    Product(id=2,name="Laptop", description="macbook pro 32 1TB", price=9999.99, quantity=7),
    Product(id=3,name="book", description="motion book for animals", price=999.99, quantity=4),
    Product(id=6,name="bat", description="sgs bats for child", price=9.99, quantity=30),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
           return product
    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"
        
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
           del products[i]
           return "Product deleted successfully"
    
    return "Product not found"
        


