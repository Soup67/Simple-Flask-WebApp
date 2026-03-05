from numpy import integer
from app import db

class User(db.Model):
    __tablename__ = "user"
    userID = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    forename = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(11), nullable=False)
    phone_number = db.Column(db.CHAR(11), nullable=True)
    home_address = db.Column(db.String(11), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    loyalty_points = db.Column(db.Integer, nullable=False)

    def __init__(self, forename, surname, username, password, email, phone_number, home_address, date_of_birth, join_date):
        from datetime import datetime
        self.username = username
        self.password = password
        self.email = email
        self.forename = forename
        self.surname = surname
        self.phone_number = phone_number
        self.home_address = home_address
        self.date_of_birth = date_of_birth
        self.join_date = datetime.now()
        self.loyalty_points = 0


class Room(db.Model):
    __tablename__ = "room"
    roomID = db.Column(db.Integer,primary_key=True, nullable=False)
    room_name = db.Column(db.String(45), nullable=False)
    room_price = db.Column(db.Numeric(10,2), nullable=False)
    room_timeslot = db.Column(db.DateTime, nullable=False)
    room_capacity = db.Column(db.Integer, nullable=False)

    def __init__(self, room_name, room_price, room_timeslot, room_capacity):
        self.room_name = room_name
        self.room_price = room_price
        self.room_timeslot = room_timeslot
        self.room_capacity = room_capacity


class RoomBooking(db.Model):
    __tablename__ = "room_booking"
    bookingID = db.Column(db.Integer,primary_key=True, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey("user.userID"), nullable=False)
    roomID = db.Column(db.Integer,db.ForeignKey("room.roomID"), nullable=False)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", foreign_keys=[userID])
    room = db.relationship("Room", foreign_keys=[roomID])
    

    def __init__(self, ticket_start_date, ticket_end_date):
        self.ticket_start_date = ticket_start_date
        self.ticket_end_date = ticket_end_date



