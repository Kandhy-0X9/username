from flask import Flask, render_template_string, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret in production

# In-memory user storage (for demo purposes)
users = {}

# Simple sign-up form HTML
signup_form = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Register</title>
	<style>
		body {
			background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
			font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
			display: flex;
			justify-content: center;
			align-items: center;
			height: 100vh;
			margin: 0;
		}
		.container {
			background: #fff;
			padding: 2rem 2.5rem;
			border-radius: 12px;
			box-shadow: 0 4px 24px rgba(0,0,0,0.12);
			width: 350px;
		}
		h2 {
			text-align: center;
			color: #4e54c8;
			margin-bottom: 1.5rem;
		}
		label {
			display: block;
			margin-bottom: 0.5rem;
			color: #333;
		}
		input[type="text"], input[type="email"], input[type="password"] {
			width: 100%;
			padding: 0.5rem;
			margin-bottom: 1rem;
			border: 1px solid #ccc;
			border-radius: 6px;
			font-size: 1rem;
		}
		input[type="submit"] {
			width: 100%;
			padding: 0.7rem;
			background: #4e54c8;
			color: #fff;
			border: none;
			border-radius: 6px;
			font-size: 1rem;
			cursor: pointer;
			transition: background 0.2s;
		}
		input[type="submit"]:hover {
			background: #5f6bc2;
		}
		.messages {
			margin-bottom: 1rem;
		}
		.messages ul {
			padding: 0;
			list-style: none;
		}
		.messages li {
			background: #f8d7da;
			color: #721c24;
			padding: 0.5rem;
			border-radius: 4px;
			margin-bottom: 0.5rem;
		}
	</style>
</head>
<body>
	<div class="container">
		<h2>Register</h2>
		<form method="POST">
			<label for="username">Username</label>
			<input type="text" id="username" name="username" required>
			<label for="email">Email</label>
			<input type="email" id="email" name="email" required>
			<label for="password">Password</label>
			<input type="password" id="password" name="password" required>
			<input type="submit" value="Sign Up">
		</form>
		<div class="messages">
		{% with messages = get_flashed_messages() %}
		  {% if messages %}
			<ul>
			{% for message in messages %}
			  <li>{{ message }}</li>
			{% endfor %}
			</ul>
		  {% endif %}
		{% endwith %}
		</div>
	</div>
</body>
</html>
'''

@app.route('/register', methods=['GET', 'POST'])
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


