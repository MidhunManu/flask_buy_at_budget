from amazon import amazon_scraping
from flask import Flask, render_template, request
app = Flask(__name__)

# shopping_get_data = []

@app.route('/')
def hello_world():
   return render_template("shopping.html")

@app.route("/shopping", methods=['POST'])
def shopping():
   return render_template('shopping.html')

@app.route("/shopitem", methods=['POST'])
def scrapShopping():
   if request.method == 'POST':
      product_name = request.form.get('product_name_html')
      amazon = amazon_scraping(product_name)
      
      global shopping_get_data
      shopping_get_data = []
      for i in range(0, len(amazon)):
         shopping_get_data.append(amazon[i])
      
      return render_template("shopping_result.html")
   
@app.route("/getdata", methods=["GET"])
def getShoppingData():
   return shopping_get_data

@app.route("/trips", methods=['POST'])
def trips():
   return render_template('trips.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)