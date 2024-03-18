from flask import Flask, render_template
import pymongo

app = Flask(__name__,
            static_url_path='',
            static_folder ='static',
            template_folder='templates',
            )

# Connect to MongoDB.
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Select database.
db = client["bakeryitems"]
# Inset data into a collection for bakeryitems.
collection = db["bakery_collection"]

# Define data for bakery items to be inserted into the database.
data = [
    {
        "name": "Slice of Black Cake", 
        "price": "$3.99", 
        "image": "black-cake-slice-2.JPG",
        "category":"cake",
        "description": "A rich, moist dessert made with rum-soaked fruits and dark sugar caramel. A Christmas and wedding tradition." 
    },
    {
        "name": "Whole Black Cake", 
        "price": "$2.50", 
        "image": "black-cake-whole.jpg",
        "category":"cake", 
        "description": "Indulge in the rich flavor of our Guyanese Black Cake, a moist delight made with rum-infused fruits and dark sugar caramel." 
    },
    {
        "name": "Pholouri", 
        "price": "$3.00", 
        "image":"pholouri.jpg",
        "category":"snack", 
        "description":"Enjoy crispy, golden-brown bites of fried split pea batter with a warm and fluffy center, a delightful treat bursting with flavor." 
    },
    {
        "name": "Bake",
        "price": "$2.99",
        "image": "bake.jpg",
        "category":"bread",
        "description":"Enjoy the classic flavor and texture of traditional fried bakes or floats for a delightful indulgence."
    },
    {
        "name":"Plait Bread",
        "price":"$5.00",
        "image":"plait-bread.jpg",
        "category":"bread",
        "description":"Indulge in a soft, fluffy loaf of Guyanese plait bread, perfect for the holidays paired with pepperpot or enjoyed any time." 

    },
    {
        "name":"Cross Buns",
        "price":"$2.00",
        "image":"cross-buns.jpg",
        "category":"bread", 
        "description":"Delight in the soft, sweet, and spiced goodness of our hot cross buns, baked to a golden brown finish and glazed with a sticky, simple syrup. Enjoy them as a cherished tradition on Good Friday, a highlight of the Guyanese Easter."
    },
    {
        "name":"Puri",
        "price":"$3.00",
        "image":"puri.jpg",
        "category":"bread", 
        "description":"Indulge in the delightful layers of our dhal puri, featuring paper-thin, savory yellow split pea mash encased in buttery dough. Pair this mouthwatering treat with your favorite saucy dish or dipping sauce for a truly satisfying experience."
    },
    {
        "name":"Roti",
        "price":"$3.00",
        "image":"roti.jpg",
        "category":"bread", 
        "description":"This Guyanese roti recipe yields paratha-style flatbreads with flaky, buttery layers that melt in your mouth. Perfect as a side dish, enjoy these delightful flatbreads with classic accompaniments like curry chicken or curry goat for a truly satisfying meal."
    }
]

# Check for existing data before insertion.
# I'm using the count_documents method to check for any existing documents in my collection before insertion.
# If the count is equal to 0, it means there are no existing documents, so I insert the new data into the database using insert_many().
# However, if the count is not 0, it means data is already present, so the insertion is skipped.
# I'm using this approach to prevent duplicates from appearing in my database whenever I save my Python file.
count = db.collection.count_documents({})
if count == 0:
    # Insert new data
    db.collection.insert_many(data)
    print("Data inserted successfully.")
else:
    print("Data already exists. Skipping insertion.")


# Flask application routes and decorators
@app.route("/")
def index():
    title = "P&S Bakery and Restaurant"
    cart_items = db.collection.find()
    bread_items = db.collection.find({"category":"bread"})
    cake_items = db.collection.find({"category":"cake"})
    snack_items = db.collection.find({"category":"snack"})
    return render_template("index.html", title=title, cart_items=cart_items, bread_items=bread_items, cake_items=cake_items, snack_items=snack_items)

@app.route('/bread')
def bread():
    return render_template("bread.html")

@app.route('/pastries')
def pastries():
    return render_template("pastries.html")

@app.route('/catering')
def catering():
    return render_template("catering.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/review')
def review():
    return render_template("review.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)