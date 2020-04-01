import flask

from controllers import SearchController, RecommendationController

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.after_request
def func(response):
    response.headers["Content-type"] = "text/json"
    return response

RecommendationController.RecommendationController.register(app,  route_base='/recommendation')
SearchController.SearchController.register(app,  route_base='/search')

@app.route('/', methods=['GET'])
def func():
    return 'welcome'

app.run()
