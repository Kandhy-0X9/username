from flask import Flask, render_template_string, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret in production

# In-memory user storage (for demo purposes)
users = {}

# Simple sign-up form HTML
signup_form = '''
	<h2>Sign Up</h2>
	<form method="POST">
		Username: <input type="text" name="username" required><br>
		Email: <input type="email" name="email" required><br>
		Password: <input type="password" name="password" required><br>
		<input type="submit" value="Sign Up">
	</form>
	{% with messages = get_flashed_messages() %}
	  {% if messages %}
		<ul>
		{% for message in messages %}
		  <li>{{ message }}</li>
		{% endfor %}
		</ul>
	  {% endif %}
	{% endwith %}
'''

@app.route('/PROTOCOL404', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		if username in users:
			flash('Username already exists!')
		else:
			users[username] = {
				'email': email,
				'password': generate_password_hash(password)
			}
			flash('Sign up successful!')
			return redirect(url_for('register'))
	return render_template_string(signup_form)

if __name__ == '__main__':
	app.run(debug=True)


