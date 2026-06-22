from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Product as ProductORM
from database import SessionLocal
from schemas import ProductCreate, Product

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "Hi this is my first api"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(ProductORM).all()
    return db_products

@app.get("/product/{id}", response_model=Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(ProductORM).filter(ProductORM.id == id).first()

@app.post("/product", response_model=Product)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = ProductORM(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# @app.put("/product")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return "Product added successfully"
        
#     return "Product not found"

# @app.delete("/product")
# def delete_product(id: int):
#     for i in range(len(products)):
#         if products[i].id == id:
#            del products[i]
#            return "Product deleted successfully"
    
#     return "Product not found"
        


