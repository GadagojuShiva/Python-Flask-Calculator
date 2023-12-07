# Import necessary modules from the Flask framework
from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template when the root URL is accessed
    return render_template('index.html')

# Define a route for handling form submissions with the 'POST' method
@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve the mathematical expression from the form data
    expression = request.form['expression']
    
    try:
        # Attempt to evaluate the mathematical expression using the 'eval' function
        result = eval(expression)
        # Render the 'index.html' template with the result and original expression
        return render_template('index.html', result=result, expression=expression)
    except Exception as e:
        # If an error occurs during evaluation, capture the exception and display an error message
        error_message = f"Error: {str(e)}"
        # Render the 'index.html' template with the error message and original expression
        return render_template('index.html', error=error_message, expression=expression)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(port=8000)
