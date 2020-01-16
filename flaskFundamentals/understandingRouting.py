from flask import Flask
app = Flask(__name__)

# 1.ocalhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")
@app.route('/')
def helloWorld():
    return 'Hello World'
# 2. localhost:5000/dojo - have it say "Dojo!" 
@app.route('/dojo')
def dojo():
    return 'Dojo'
# 3 4 5.localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request.
@app.route('/say/<name>')
def say(name):
    return "Hi " + name
# 6 7 .localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 35.  To do this use int().  For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, it should say "hello" 80 times.
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)
@app.route('/repeat/<qty>/<name>')
def repeat(qty, name):
    return name*int(qty)
if __name__ =='__main__':
    app.run(debug=True)
