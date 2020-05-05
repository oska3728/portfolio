from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

# def write_to_file(data):
# 	with open('database.txt', mode='a') as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',newline='\n', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
"""
def survey_to_csv(info):
	with open('survey.csv',newline='\n', mode='a') as survey:
		birthday = info["birthday"]
		gender = info["gender"]
		country = info["country"]
		survey_writer = csv.writer(survey, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		survey_writer.writerow([birthday,gender,country])
"""
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('./thankyou.html')
	else:
		return 'something went wrong. Try again'

"""
@app.route('/submit_survey', methods=['POST', 'GET'])
def submit_survey():
	if request.method == 'POST':
		info = request.form.to_dict()
		survey_to_csv(info)
		return redirect('./index.html')
	else:
		return 'something went wrong. Try again'
		"""
