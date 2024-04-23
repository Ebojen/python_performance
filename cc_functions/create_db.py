from datetime import datetime
from typing import List
from typing import Optional

from faker import Faker
import sqlalchemy as sa
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    title: Mapped[Optional[str]]
    email: Mapped[str]
    street_address: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    zipcode: Mapped[int]
    orders: Mapped[List["Order"]] = relationship(
        back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return "".join(
            [
                "Customer(",
                f"id={self.id!r}, ",
                f"first_name={self.first_name!r}, ",
                f"last_name={self.last_name!r}, ",
                f"title={self.title!r}, ",
                f"email={self.email!r}, ",
                f"street_address={self.street_address}, ",
                f"city={self.city}, ",
                f"state={self.state}, ",
                f"zipcode={self.zipcode}",
                ")",
            ]
        )


engine = sa.create_engine("sqlite://", echo=True)
fake = Faker()


def make_customers() -> None:
    with Session(engine) as session:
        customers = [
            Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                title=fake.prefix(),
                email=fake.email(),
                street_address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zipcode=fake.zipcode(),
            )
            for _ in range(5)
        ]
        session.add_all(customers)
        session.commit()


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    package_count: Mapped[int]
    unit_cost: Mapped[float]

    def __repr__(self) -> str:
        return "".join(
            [
                "Product(",
                f"id={self.id}, ",
                f"product_name={self.product_name}, ",
                f"package_count={self.package_count}, ",
                f"unit_cost={self.unit_cost, }" ")",
            ]
        )


def make_products() -> None:
    with Session(engine) as session:
        products = [
            Product(
                product_name="Chocolate Chip Cookies", package_count=20, unit_cost=4.50
            ),
            Product(
                product_name="Chocolate Chip Cookies Jumbo Pack",
                package_count=40,
                unit_cost=8.00,
            ),
            Product(product_name="Sugar Cookies", package_count=20, unit_cost=4.00),
            Product(
                product_name="Sugar Cookies Jumbo Pack",
                package_count=40,
                unit_cost=7.50,
            ),
            Product(
                product_name="Peanut Butter Blossum Cookies",
                package_count=20,
                unit_cost=5.00,
            ),
            Product(
                product_name="Peanut Butter Blossum Cookies Jumbo Pack",
                package_count=40,
                unit_cost=9.00,
            ),
            Product(
                product_name="Wagon Wheel Cookies", package_count=20, unit_cost=4.50
            ),
            Product(
                product_name="Wagon Wheel Cookies Jumbo Pack",
                package_count=40,
                unit_cost=8.00,
            ),
            Product(
                product_name="Gooey Butter Cookies", package_count=20, unit_cost=6.00
            ),
            Product(
                product_name="Gooey Butter Cookies Jumbo Pack",
                package_count=40,
                unit_cost=11.00,
            ),
        ]
        session.add_all(products)
        session.commit()


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(sa.ForeignKey("customers.id"))
    updated_at: Mapped[datetime]
    total_cost: Mapped[float]
    order_details: Mapped["OrderDetail"] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )
    customer: Mapped["Customer"] = relationship(back_populates="orders", uselist=False)

    def __repr__(self) -> str:
        return "".join(
            [
                "Order(",
                f"id={self.id}, ",
                f"customer_id={self.customer_id}, ",
                f"updated_at={self.updated_at}, ",
                f"total_cost={self.total_cost}",
                ")",
            ]
        )


class OrderDetail(Base):
    __tablename__ = "order_details"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(sa.ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(sa.ForeignKey("products.id"))
    product: Mapped["Product"] = relationship()
    number_purchased: Mapped[int]
    purchase_cost: Mapped[float]
    order: Mapped["Order"] = relationship(back_populates="order_details", uselist=False)

    def __repr__(self) -> str:
        return "".join(
            [
                "OrderDetail(",
                f"id={self.id}, ",
                f"order_id={self.order_id}, ",
                f"product_id={self.product_id}, ",
                f"number_purchased={self.number_purchased}, ",
                f"purchase_cost={self.purchase_cost}",
                ")",
            ]
        )


def make_order():
    pass

def main():
    Base.metadata.create_all(engine)

    make_customers()

    with Session(engine) as session:
        stmt = sa.select(Customer)
        for customer in session.scalars(stmt):
            print(customer)
        session.commit()

    make_products()

    with Session(engine) as session:
        stmt = sa.select(Product)
        for product in session.scalars(stmt):
            print(product)
        session.commit()


if __name__ == "__main__":
    main()
