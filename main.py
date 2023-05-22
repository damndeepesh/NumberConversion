from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    input_value = request.form["input_value"]
    input_type = request.form["input_type"]
    output_type = request.form["output_type"]

    # Convert the value
    if input_type == "Binary":
        if output_type == "Decimal":
            result = int(input_value, 2)
        elif output_type == "Hexadecimal":
            result = int(input_value, 2)
        elif output_type == "Octal":
            result = int(input_value, 8)
    elif input_type == "Decimal":
        if output_type == "Binary":
            result = bin(int(input_value))[2:]
        elif output_type == "Hexadecimal":
            result = hex(int(input_value))[2:]
        elif output_type == "Octal":
            result = oct(int(input_value))[2:]
    elif input_type == "Hexadecimal":
        if output_type == "Binary":
            result = bin(int(input_value, 16))[2:]
        elif output_type == "Decimal":
            result = int(input_value, 16)
        elif output_type == "Octal":
            result = oct(int(input_value, 16))[2:]
    elif input_type == "Octal":
        if output_type == "Binary":
            result = bin(int(input_value, 8))[2:]
        elif output_type == "Decimal":
            result = int(input_value, 8)
        elif output_type == "Hexadecimal":
            result = hex(int(input_value, 8))[2:]

    return render_template("result.html", input_value=input_value, input_type=input_type, output_type=output_type, result=result)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)