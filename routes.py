from flask import render_template, redirect
from forms import RegisterUser, AddProductClass, AddProductCategory, LoginUser
from extensions import app, db
from models import Product, ProductCategory, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
category_ids = [1, 3]


@app.route("/")
def home_page():
    furnitures = Product.query.filter(Product.category_id.in_(category_ids)).limit(4).all()
    AC = Product.query.filter_by(category_id=2).limit(4).all()
    pools = Product.query.filter_by(category_id=4).limit(4).all()
    return render_template("main_page.html", products=Product.query.all(), categories=ProductCategory.query.all(),
                           AC=AC, User=User.query.all(), furnitures=furnitures, pools = pools)


@app.route("/product/<int:id>")
def product(id):
    product = Product.query.get(id)
    category_id = product.category_id
    same_category_products = Product.query.filter_by(category_id= category_id).filter(Product.id != id).limit(4).all()
    if not product:
        return render_template("404.html", id=id)

    return render_template("product.html", product=product, categories=ProductCategory.query.all(), product_category = same_category_products)


@app.route("/log", methods=["POST", "GET"])
def log():
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            print(form.errors)
    return render_template("log_in.html", form=form, categories=ProductCategory.query.all())


@app.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect("/")


@app.route("/reg", methods=["POST", "GET"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        file = form.profile_picture.data
        filename = secure_filename(file.filename)
        file_path = os.path.join("static", "ProfilePiqtures", filename)
        file.save(os.path.join(app.root_path, file_path))

        new_user = User(email=form.email.data,
                        password=form.password.data,
                        username=form.username.data,
                        profile_piqture=filename,
                        phone_number=form.phone_number.data,
                        country=form.country.data,
                        role="user")

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect("/")
    else:
        print(form.errors)
    return render_template("register.html", form=form, categories=ProductCategory.query.all())


@app.route("/add_product", methods=['GET', 'POST'])
@login_required
def add_product():
    if current_user.role != "admin":
        return redirect("/")
    form = AddProductClass()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data,
                              image_url=form.image_url.data,
                              price=form.price.data,
                              text=form.text.data,
                              category_id=form.category_id.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect("/")
    return render_template("add_product.html", form=form, categories=ProductCategory.query.all())


@app.route("/edit_product/<int:id>", methods=["POST", "GET"])
@login_required
def edit_product(id):
    product = Product.query.get(id)
    if not product:
        return render_template("404.html", id=id)

    form = AddProductClass(name=product.name, text=product.text, price=product.price, image_url=product.image_url,
                           category_id=product.category_id)

    if form.validate_on_submit():
        product.name = form.name.data
        product.text = form.text.data
        product.price = form.price.data
        product.image_url = form.image_url.data
        product.category_id = form.category_id.data

        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)

    return render_template("edit_product.html", form=form, categories=ProductCategory.query.all())


@app.route("/delete_product/<int:id>", methods=["DELETE", "GET"])
@login_required
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return render_template("404.html", id=id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")


@app.route("/add_category", methods=['GET', 'POST'])
@login_required
def addCategory():
    form = AddProductCategory()
    if form.validate_on_submit():
        new_category = ProductCategory(name=form.category_name.data,
                                       id=form.id.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)
    return render_template("add_category.html", form=form, categories=ProductCategory.query.all())


@app.route("/products/<int:category_id>")
@app.route("/products")
def products(category_id):
    if category_id:
        products = ProductCategory.query.get(category_id).products
    else:
        products = Product.query.all()
    return render_template("products.html", products=products, categories=ProductCategory.query.all())


@app.route("/profile/<int:user_id>")
@login_required
def profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template("404.html", id=user_id)
    return render_template("profile.html", user=user, categories=ProductCategory.query.all())


@app.route("/search/<string:name>")
def search(name):
    products = Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    return render_template("products.html", products=products)

@app.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("users.html", users=users)