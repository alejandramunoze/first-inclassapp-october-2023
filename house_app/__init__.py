





# this is the "web_app/__init__.py" file...

from flask import Flask

from house_app.routes.home_routes import home_routes
#from house_app.routes.book_routes import book_routes
#from house_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)