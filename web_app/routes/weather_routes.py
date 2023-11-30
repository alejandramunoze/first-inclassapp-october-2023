

# this is the "web_app/routes/weather_routes.py" file...

from flask import Blueprint, request, render_template
from app.weather_app import get_forecast

weather_routes = Blueprint("weather_routes", __name__)


@weather_routes.route("/weather/form",methods=["GET", "POST"])
def weather():
    return render_template("forecast_form.html")
        
@weather_routes.route("/weather",methods=["GET", "POST"])
def weather_result():
    print("WEATHER RESULTS...")
    
    if request.method == "POST": #this is the form!
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("RESULT DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args - which this it would be sth like http://127.0.0.1:5000/stocks/dashboard?symbol=TSLA
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    zip_code = request_data.get("zip code") or "20057"

    try:
        forecast = get_forecast(zip_code=zip_code) 
        data = forecast.to_dict("forecast records")
        flash("Fetched Real-time Weather Data!", "success")
        return render_template("forecast_result.html", zip_code=zip_code)

    except Exception as err: # if anything goes wrong in the fetching of the data
        print('OOPS', err)

        flash("Weather Forecast Error. Please check your zip code and try again!", "danger")
        return redirect("/weather/form")
   



