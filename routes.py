from datetime import datetime

from flask import render_template, Flask, request, session, redirect, url_for, flash

app = Flask(__name__)

def register_routes(app,db):
        @app.route('/', methods=["GET","POST"])
        def home():
            return render_template("index.html")

        @app.route('/about', methods=["GET","POST"])
        def about():
            return render_template("about.html")

        @app.route('/login', methods=["GET","POST"])
        def login ():
            userID = session.get("userID")
            if userID != None:
                redirect(url_for("home"))
                return redirect(url_for("home"))
            if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]
                from models import User
                user = User.query.filter_by(username = username).first()
                if user and user.password == password:
                    print("Logged in")
                    session['userID'] = user.userID
                    return render_template("account.html")
                else:
                    print("Failed to log in")
            return render_template("login.html")

        @app.route('/register', methods=["GET","POST"])
        def register():
            if request.method == "POST":
                print("")
                from app import db
                from models import User
                new_user = User(forename=request.form["forename"],
                                surname=request.form["surname"],
                                email=request.form["email"],
                                username=request.form["username"],
                                password=request.form["password"],
                                phone_number=request.form["phone_number"],
                                home_address=request.form["home_address"],
                                date_of_birth=request.form["date_of_birth"],
                                join_date=datetime.now())
                existing = User.query.filter_by(email=request.form["email"]).first()
                if existing:
                    # flash("Email already registered", "error")
                    return redirect(url_for('register'))
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('home'))
            return render_template("register.html")

        @app.route('/booking', methods=["GET","POST"])
        def booking ():
            if request.method == "POST":
                from models import TicketBooking
                from datetime import datetime
                new_booking = TicketBooking(session["userID"],datetime.now())
                db.session.add(new_booking)
                db.session.commit()
                number = int(request.form["number"])
                for i in range(number):
                    print(f"tb:{new_booking.ticket_bookingID}, t:{i}")
            return render_template("booking.html")

        @app.route('/educational_visits', methods=["GET","POST"])
        def educational_visits ():
            return render_template("educational_visits.html")

        @app.route('/environment', methods=["GET","POST"])
        def environment ():
            return render_template("environment.html")

        @app.route('/accessibility', methods=["GET","POST"])
        def accessibility ():
            return render_template("accessibility.html")


        @app.route('/account', methods=["GET","POST"])
        def account ():
            if "userID" not in session:
                return redirect(url_for("home"))
            userID = session.get("userID")
            from models import Ticket, TicketBooking
            bookings = TicketBooking.query.filter_by(userID=userID)
            tickets = []
            for booking in bookings:
                tickets.extend(Ticket.query.filter_by(ticket_booking_id = booking.ticketbooking_id).all())
            print(bookings)
            return render_template("account.html")

        @app.route('/ticket_booking', methods=["GET","POST"])
        def ticket_booking ():
            if request.method == "POST":
                from models import TicketBooking
                from datetime import datetime
                new_booking = TicketBooking(session["userID"],datetime.now())
                db.session.add(new_booking)
                db.session.commit()
                number = int(request.form["number"])
                for i in range(number):
                    print(f"tb:{new_booking.ticket_bookingID}, t:{i}")
            return render_template("ticket_booking.html")

        @app.route('/room_booking', methods=["GET","POST"])
        def room_booking ():
            return render_template("room_booking.html")

        @app.route('/checkout', methods=["GET", "POST"])
        def checkout():
            return render_template("checkout.html")

        @app.route('/logout', methods=["GET", "POST"])
        def logout():
            print("Successfully logged out")
            session.clear()
            return render_template("index.html")

if __name__ == '__main__':
    app.run()