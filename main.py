#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

header = """
<!DOCTYPE html>
<html>
<head>
	<title>::Sign up::</title>
</head>
<body>

"""

form = """
<h1>Sign up below</h1>
<form method="get" action="/Logged">
	<label>
		Username: <input type="text" name="username" > 
	</label>

	<br />
	
	<label>
		Password: <input type="password" name="password"> 
	</label>

	<br />
	
	<label>
		Verify Password: <input type="password" name="vpassord"> 
	</label>

	<br />
	
	<label>
		E-mail (optional): <input type="text" name="email"> 
	</label>

	<br />

	<input type="submit">
</form>

"""

footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(header + form + footer)

class Logged(webapp2.RequestHandler):
	def get(self):
		user = self.request.get("username")
		passw = self.request.get("password")
		vpass = self.request.get("vpassord")
		emailsub = self.request.get("email")

		if not user:
			self.response.write(header + """
				<h1>Sign up below</h1>
				<form method="get" action="/Logged">
					<label>
						Username: <input type="text" name="username" > Please enter a valid Username
					</label>

					<br />
					
					<label>
						Password: <input type="password" name="password"> 
					</label>

					<br />
					
					<label>
						Verify Password: <input type="password" name="vpassord"> 
					</label>

					<br />
					
					<label>
						E-mail (optional): <input type="text" name="email value=\"""" + emailsub + """"> 
					</label>

					<br />

					<input type="submit">
				</form>
				"""+ footer)
		elif (passw != vpass):
			self.response.write(header + """
				<h1>Sign up below</h1>
				<form method="get" action="/Logged">
					<label>
						Username: <input type="text" name="username" value = \"""" + user + """">
					</label>

					<br />
					
					<label>
						Password: <input type="password" name="password"> 
					</label>

					<br />
					
					<label>
						Verify Password: <input type="password" name="vpassord"> Passwords don't rerematch
					</label>

					<br />
					
					<label>
						E-mail (optional): <input type="text" name="email" value=\"""" + emailsub + """"> 
					</label>

					<br />

					<input type="submit">
				</form>
				"""+ footer)

		elif (('@' not in emailsub) or ('.com' not in emailsub)):
			self.response.write(header + """
				<h1>Sign up below</h1>
				<form method="get" action="/Logged">
					<label>
						Username: <input type="text" name="username" value=\"""" + user + """">
					</label>

					<br />
					
					<label>
						Password: <input type="password" name="password"> 
					</label>

					<br />
					
					<label>
						Verify Password: <input type="password" name="vpassord"> 
					</label>

					<br />
					
					<label>
						E-mail (optional): <input type="text" name="email" value= \"""" + emailsub + """"> Please enter a valid e-mail
					</label>

					<br />

					<input type="submit">
				</form>
				"""+ footer)
		else:
			self.response.write(header + """
				<form method="get" action="/Logged">
					<h1>Hello,""" + user + """</h1>
				"""+ footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Logged', Logged)
], debug=True)
