import smtplib
from email.message import EmailMessage
from flask import render_template,redirect,url_for,request,session,flash
from flask.templating import render_template_string
from .forms import Register_Indi,Login_Indi,Register_org,Login_org,Message_Send,File_upload
from home import app,db,bcrypt,mongo
from .data import User_indi,User_org,Message_user
import psycopg2

app.config['FILE_ALLOWED']=["PNG","JPG","JPEG","TXT","GIF"]


@app.route("/")
def home():
    return render_template('home.html',title="HOME")

#registration page routes
@app.route('/register')
def register():
    return render_template('register.html',title="SIGN UP")

@app.route('/register_indi',methods=['GET','POST'])
def register_indi():
    formo=Register_Indi()
    if formo.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(formo.password.data).decode('utf-8')
        user=User_indi(fname=formo.fname.data,lname=formo.lname.data,email=formo.email.data,password=hashed_pw,aadhar=formo.aadhar.data)

        exist_user=User_indi.query.filter_by(email=formo.email.data).first()
        if exist_user==None:
            db.session.add(user)
            db.session.commit()
            flash("Welcome","success")
            return redirect(url_for('login_indi'))
        else:
            return '<h1>Sorry already exits</h1>'

    return render_template("register_indi.html",form=formo,title="SIGNUP AS INDIVIDUAL")

@app.route("/register_org",methods=['GET','POST'])
def register_org():
    formor=Register_org()
    if request.method=='POST':
        hashed_pw=bcrypt.generate_password_hash(formor.passw.data).decode('utf-8')
        user1=User_org(orgname=formor.orgname.data,hod=formor.hod.data,oemail=formor.official_email.data,contact=formor.contact.data,branch=formor.branch.data,passw=hashed_pw)
        
        existingUser=User_org.query.filter_by(contact=formor.contact.data).first()

        if existingUser==None:
            db.session.add(user1)
            db.session.commit()
            flash("Welcome","success")
            return redirect(url_for("home"))
        
        else:
            flash("Sorry user already exits!!")
            return redirect(url_for('login'))
        
    return render_template("register_org.html",form=formor,title="SIGN UP AS ORGANISATION")


#login page routes
@app.route('/login')
def login():
    return render_template('login.html',title="LOGIN")

@app.route('/login_indi',methods=['GET','POST'])
def login_indi():
    forml=Login_Indi()
    if forml.validate_on_submit():
        existingUser=User_indi.query.filter_by(email=forml.email.data).first()
        if existingUser and bcrypt.check_password_hash(existingUser.password,forml.password.data):
            flash("Welcome back !!","success")
            return render_template("home.html",title="HOME")
        else:
            flash("Email does not exist!!")
            return render_template("register.html",title="REGISTER AS INDIVIDUAL")
    return render_template("login_indi.html",title="LOGIN AS INDIVIDUAL",form=forml)

@app.route('/login_org',methods=['GET','POST'])
def login_org():
    forml=Login_org()
    if request.method=='POST':
        existingUser=User_org.query.filter_by(contact=forml.contact.data).first()
        if existingUser and bcrypt.check_password_hash(existingUser.passw,forml.passw.data):
            flash("Welcome back","success")
            return redirect(url_for("home"))
        else:
            flash("You are not registered!!")
            return render_template("register.html",title="REGISTER")
    return render_template("login_org.html",title="LOGIN AS ORGANISATION",form=forml)

@app.route('/message',methods=['GET','POST'])
def message():
    form=Message_Send()
    if request.method=='POST':
        user=Message_user(no_of_bodies=form.no_of_bodies.data,street_name=form.street_name.data,area=form.area.data,landmark=form.landmark.data,city=form.city.data,pincode=form.pincode.data)
        db.session.add(user)
        db.session.commit()

        number=request.form['no_of_bodies']
        street=request.form['street_name']
        area=request.form['area']
        landmark=request.form['landmark']
        city=request.form['city']
        pincode=request.form['pincode']

        #email sending
        msg=EmailMessage()
        msg['Subject']='Information about the corpses'
        msg['From']='The team of Dignity to the Dead'

        conn = psycopg2.connect(host="localhost",database="register",user="postgres",password="postpass")
        cur=conn.cursor()
        sql="SELECT oemail FROM user_organ"
        cur.execute(sql)
        recipients = cur.fetchall()
        r=len(recipients)
        l=[]
        for i in range(0,r):
            l.append(recipients[i][0])
        print(l)
        msg['To']=','.join(l)
        msg.set_content(f"Number of bodies : {number},\nStreet Name : {street},\nArea : {area},\nLandmark : {landmark},\nCity: {pincode},\npicode: {pincode}")

        s = smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.login("dignitytothedead@gmail.com","dhasubgopbha")
        s.send_message(msg)
        s.quit()
        print("sent mail")
        flash('Thank you for your kindness!!')
        return redirect(url_for('home'))
    return render_template('message.html',form=form,title='ADD ON')

@app.route('/create',methods=['GET','POST'])
def create():
    form=File_upload()
    print(form)
    if request.method=='POST':
            print("entered")
            username = request.form['Name']
            email = request.form['email']
            filetoupload = request.files['filetoupload']
            filen = filetoupload.filename
            mongo.save_file(filetoupload.filename,filetoupload)
            mongo.db.file_send.insert({'username':username,'email':email,'file_name':filen})
            print("hello")
    return render_template('picture.html',form=form)

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)




