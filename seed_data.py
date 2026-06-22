

from database import SessionLocal, engine, Base
from models import Product as ProductORM

Base.metadata.create_all(bind=engine)


initial_products = [
    {"id": 1, "name": "mobile", "description": "moto edge 60", "price": 99.99, "quantity": 10},
    {"id": 2, "name": "Laptop", "description": "macbook pro 32 1TB", "price": 9999.99, "quantity": 7},
    {"id": 3, "name": "book", "description": "motion book for animals", "price": 999.99, "quantity": 4},
    {"id": 6, "name": "bat", "description": "sgs bats for child", "price": 9.99, "quantity": 30},
]

def seed_products():
    db = SessionLocal()
    try:
        for item in initial_products:
            exists = db.query(ProductORM).filter_by(id=item["id"]).first()
            if not exists:
                db.add(ProductORM(**item))
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed_products()