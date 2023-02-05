from amazon import amazon_scraping
from trips import trips_scraping
from jio_mart import jio_mart_scraping
from flask import Flask, render_template, request
app = Flask(__name__)


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

@app.route("/getCheapestFare", methods=['POST'])
def getfares():
   if request.method == 'POST':
      start = request.form.get("start_location")
      destination = request.form.get("end_location")
      date = request.form.get("departure_date")
      
      trips_data = trips_scraping(start, destination, date)
      global trips_array
      trips_array = []
      
      for i in range(0, len(trips_data)):
         trips_array.append(trips_data[i])
   return render_template("flight_results.html")

@app.route("/getFlightData", methods=['GET'])
def sendtripsData():
   return trips_array

@app.route("/contact", methods=['POST'])
def contactUs():
   return render_template("contact.html")

@app.route("/groceries", methods=['POST'])
def groceries():
   return render_template("groceries.html")

@app.route("/findCheapestGroceries", methods=['POST'])
def getCheapestGroceries():
   if request.method == "POST":
         groceries_input = request.form.get("find_groceries")
         jio_mart_res = jio_mart_scraping(groceries_input)
         
         global jio_mart_data
         jio_mart_data = []
         
         for i in range(0, len(jio_mart_res)):
            jio_mart_data.append(jio_mart_res[i])
   return render_template("groceries_result.html")

@app.route("/findGroceries", methods=['GET'])
def jioMartSendData():
   return jio_mart_data

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)