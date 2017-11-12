from flask import Flask, send_from_directory, request, Request


app = Flask(__name__)

@app.route("/")
def serve_page():
    return send_from_directory(".", "client.html")

@app.route("/db")
def getDB():
    return open("todoDB", "r").read()

@app.route("/put", methods=["GET", "POST"])
def putDB():
    file = open("todoDB", "w")
    file.write(request.data.decode("utf-8"))
    file.flush()
    file.close()

    return "It went fine"





if __name__ == "__main__":
    app.run(debug=None, host="0.0.0.0", port=5000)