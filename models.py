from extensions import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    text = db.Column(db.String)
    image_url = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("product_category.id"))
    category = db.relationship("ProductCategory", back_populates="products")

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    products = db.relationship("Product", back_populates="category")

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    username = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    profile_piqture = db.Column(db.String)
    country = db.Column(db.String)
    role = db.Column(db.String)

    def __init__(self, email, password, username, phone_number, country, profile_piqture, role="user"):
        self.email = email
        self.password = generate_password_hash(password)
        self.username = username
        self.phone_number = phone_number
        self.profile_piqture = profile_piqture
        self.country = country
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        admin = User(email = "wolfdolf12@gmail.com",
                     password = "nika_inadze1",
                     username = "kotvumniy",
                     phone_number = 599235152,
                     profile_piqture="398536540_366188315733716_6000224412417250393_n.jpg",
                     country = "ge",
                     role = "admin")
        db.session.add(admin)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)