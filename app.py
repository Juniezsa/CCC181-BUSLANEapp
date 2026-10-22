"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the demo. A real app would load this from a database later.
BUS_TYPE = [{"id": 1, "Bus Type": "Aircon", "Trips": "Non-Stop", "Capacity": 45},
            {"id": 2, "Bus Type": "Aircon", "Trips": "Regular Trip", "Capacity": 45},
            {"id": 3, "Bus Type": "Non-Aircon", "Trips": "Non-Stop", "Capacity": 30}
            ]

#Each Ticket: Number, Name, Bus Type, Departure Time, Destination, From, Passenger Type, Priority, Status
#Passenger Type consists: Regular, Student, Senior Citizen,and PWD
#Priority; Who to board first/sits at front of the bus: Senior Citizen and PWD
#Status: Waiting, On-Board, In Route, Arrived
TICKETS = [{"Number":1, "Name": "Denice Agoncillo", "Bus Type": 1, "Departure Time": "04:00 AM", "Destination": "Iligan City", "From": "Cagayan De Oro", "Passenger Type": "Student", "Priority": False, "Status": "Arrived"},
           {"Number":2, "Name": "Mark Johnson", "Bus Type": 1, "Departure Time": "04:00 AM", "Destination": "Iligan City", "From": "Cagayan De Oro", "Passenger Type": "PWD", "Priority": True, "Status": "Arrived"},
           {"Number":3, "Name": "John Doe", "Bus Type": 2, "Departure Time": "09:00 AM", "Destination": "Iligan City", "From": "Cagayan De Oro", "Passenger Type": "Regular", "Priority": False, "Status": "On-Board"},
           {"Number":4, "Name": "Jane Smith", "Bus Type": 3, "Departure Time": "10:00 AM", "Destination": "Iligan City", "From": "Cagayan De Oro", "Passenger Type": "Senior Citizen", "Priority": True, "Status": "Waiting"},
           
           ]


@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html", name="Ana", tickets=TICKETS, buses={b['id']: b for b in BUS_TYPE})


@app.route("/queue/<int:ticket_id>")
def ticket(ticket_id):
    # <int:ticket_id> only matches numbers, so /queue/abc returns 404.
    return render_template("ticket.html", ticket_id=ticket_id)


@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, CCC181!"


if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)