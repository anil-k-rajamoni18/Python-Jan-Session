from flask import Flask, render_template, request
import requests
import random
import hashlib
import string


# object creation for Flask class.

app = Flask(__name__)

#routes

@app.route('/')
def home_page():
	return render_template('home.html',data='Hey Hi Im from BackEnd Flask')


@app.route("/home")
def main_page():
	return render_template('index.html')

def Generator(pass_len):
    password = ''

    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    return password


@app.route('/random',methods=['POST'])
def random_method():
	if request.method=='POST':
		length = int(request.form['password_len'])
	
		res = f"Hey \n Your Random Strong password \n of length \n {length} is \n "+""+Generator(length)
		return render_template('result1.html',result=res)


def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching :{res.status_code} ,check the api and try again')

    return res


def get_password_leaks_counts(hashes, hash_to_check):


    hashes = (line.split(':') for line in hashes.text.splitlines())



    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


@app.route('/pwned',methods=['POST'])
def pwned():

	if request.method=='POST':
		password = request.form['password']

		sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

		first_5_char, tail = sha1_password[:5], sha1_password[5:]

		response = request_api_data(first_5_char)
		hacked_count = get_password_leaks_counts(response, tail)
		if hacked_count:
			return render_template('result1.html',result=f'{password } was found {hacked_count} times  ... \n you should change it')
		else:
			return render_template('result1.html',result=f'{password} not found ! carry on .')


if __name__ =='__main__':
	app.run(debug=True)
