from inspect import classify_class_attrs
from home import db,mongo

class User_indi(db.Model):
    __tablename__="user_individual"
    idno = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(25),nullable=False)
    lname = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    password = db.Column(db.String(),nullable=False)
    aadhar = db.Column(db.String(16),nullable=False, unique=True)

    def __init__(self,fname,lname,email,password,aadhar):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.password = password
        self.aadhar = aadhar

class User_org(db.Model):
    __tablename__="user_organ"
    idno = db.Column(db.Integer,primary_key=True)
    orgname = db.Column(db.String(),nullable=False)
    hod = db.Column(db.String(),nullable=False)
    oemail = db.Column(db.String(120),nullable=False)
    contact = db.Column(db.String(12),nullable=False,unique=True)
    branch = db.Column(db.String(),nullable=False)
    passw = db.Column(db.String(),nullable=False)

    def __init__(self,orgname,hod,oemail,contact,branch,passw):
        self.orgname=orgname
        self.hod=hod
        self.oemail=oemail
        self.contact=contact
        self.branch=branch
        self.passw=passw

class Message_user(db.Model):
    __tablename__='message_details'
    idno = db.Column(db.Integer,primary_key=True)
    no_of_bodies = db.Column(db.Integer,nullable=False)
    street_name = db.Column(db.String(),nullable=False)       
    area = db.Column(db.String(),nullable=False)
    landmark = db.Column(db.String(),nullable=False)
    city = db.Column(db.String(),nullable=False)
    pincode = db.Column(db.String(),nullable=False)

    def __init__(self,no_of_bodies,street_name,area,landmark,city,pincode):
        self.no_of_bodies=no_of_bodies
        self.street_name=street_name
        self.area=area
        self.landmark=landmark
        self.city=city
        self.pincode=pincode

