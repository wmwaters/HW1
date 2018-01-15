## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
#http://www.html.am/html-codes/forms/html-checkbox-code.cfm
#https://openweathermap.org/current
#Austin McCall


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
app = Flask(__name__)
app.debug = True
import requests
import json

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def SI364_Welcome():
	return 'Welcome to SI 364!'

@app.route('/movie/<movie_name>')
def movie_dict(movie_name):
	req = requests.get('https://itunes.apple.com/search?term=' + movie_name + '&media=movie')
	dict_text = json.loads(req.text)
	return str(dict_text)

@app.route('/question')
def fave_number():
	p = """
	<!DOCTYPE html>
	<html>
	<body>
	<form action = "/result" method = "POST">
	Your favorite number:<br>
	<input type = "text" name = "fave_number">
	<br>
	<input type = "submit" value = "Submit">
	</form>
	</body>
	</html>
	"""
	return p

@app.route('/result', methods = ['GET','POST'])
def display_result():
	if request.method == 'POST':
		number = int(request.form['fave_number'])
		number = number * 2
	return ("Double your favorite number is: " + str(number))

@app.route('/problem4form', methods = ['GET','POST'])
def problem4():
	p = """
	<!DOCTYPE html>
	<html>
	<body>
	Weather Search
	<form action = "/problem4form" method = "POST">
	Enter a 5-digit US zip code to do a weather search:<br>
	<input type = "text" name = "entered_zip"><br>
	In what units would you like to see temperature displayed (select at least one)?<br>
	<input type = "checkbox" name = "unit" value = "f"> Fahrenheit<br>
	<input type = "checkbox" name = "unit" value = "c"> Celsius<br>
	<input type = "checkbox" name = "unit" value = "k"> Kelvin<br>
	<input type = "submit" value = "Submit">
	</form>
	</body>
	</html>
	"""
	if request.method == 'POST':
		req = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + request.form['entered_zip'] + '&APPID=PUT API KEY HERE FROM OPEN WEATHER MAP')
		json_dict = json.loads(req.text)
		requested_units = dict(request.form)['unit']
		ans = "The weather in " + str(json_dict['name']) + " is " + str(json_dict['weather'][0]['description'] + ".")
		ans2 = ""
		if ('k' in requested_units):
			ans2 += "<br>It is " + str(int(json_dict['main']['temp'])) + " degrees Kelvin."
		if ('f' in requested_units):
			fah = ((9 / 5) * (int(json_dict['main']['temp']) - 273)) + 32
			ans2 += "<br>It is " + str(int(fah)) + " degrees Fahrenheit."
		if ('c' in requested_units):
			cel = int(json_dict['main']['temp']) - 273
			ans2 += "<br>It is " + str(cel) + " degrees Celsius."
		return (p + ans + ans2)
	else:
		return p

if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
