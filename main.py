from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json,os,math
from datetime import datetime

from werkzeug.utils import secure_filename

with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server=True
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] =params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)

if local_server:
        app.config['SQLALCHEMY_DATABASE_URI'] =params['local_uri']

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prood_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Comments(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tag_line= db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    slug = db.Column(db.String(21), nullable=False)
    img_file = db.Column(db.String(12), nullable=True)



@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['num_of_post']))
    # [0: params['no_of_posts']]
    # posts = posts[]
    page = request.args.get('page')#t will take only one object, a "dictionary"
    # type of object (as stated in the previous answers).
    # This "dictionary" object, however,
    # can have as many elements as needed... (dictionaries have paired elements called Key, Value).
    '''
    the request.args is bringinga dictionary" object
    for you.The "dictionary" object is similar to other collection-type of objects in Python,
     in that it can store many elements in one single object.Therefore the answer to your question
    '''
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['num_of_post']): (page - 1) * int(params['num_of_post']) + int(params['num_of_post'])]
    # Pagination Logic
    # First
    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif (page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


#why we use params???And posts=posts????


@app.route("/about")
def about():
       return render_template('about.html',params=params)


@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user'] :#jdi already logged in thak
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params,posts=posts)



    if request.method=='POST':#pass krtesi value
        username=request.form.get('uname')#fromhtml uname
        userpass= request.form.get('pass')
        if(username==params['admin_user'] and userpass==params[ "admin_password"]):
            #set The session variable easy way uname ba user OWn choice
             session['user']=username
             posts=Posts.query.all()
        #REDIRECT TO ADMIN PANNEL
             return render_template('dashboard.html',params=params,posts=posts)


    return render_template('login.html',params=params)

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edid(sno):
      if 'user' in session and session['user'] == params['admin_user'] :
              if request.method == 'POST':
                 box_title = request.form.get('title')
                 tline=request.form.get('tline')
                 slug=request.form.get('slug')
                 content=request.form.get('content')
                 img_file=request.form.get('img_file')
                 date=datetime.now()

                 if sno == '0':
                    post=Posts(title=box_title,slug=slug,content=content,img_file=img_file,tag_line=tline,date=date)
                    db.session.add(post)
                    db.session.commit()
                    flash("Your Post is Uploaded successfully", "success")
                 else:
                     post=Posts.query.filter_by(sno=sno).first()
                     post.title=box_title
                     post.slug=slug
                     post.content=content
                     post.tagline=tline
                     post.img_file=img_file
                     post.date=date
                     db.session.commit()
                     return redirect('/edit/'+sno)
              post = Posts.query.filter_by(sno=sno).first()
              return  render_template('/edit.html',params=params,post=post,sno=sno)

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
            if request.method=="POST":
                f=request.files['file1']
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
                flash("uploaded successfully", "success")

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
                     Post = Posts.query.filter_by(sno=sno).first()
                     db.session.delete(Post)
                     db.session.commit()
                     flash("Deleted successfully")
    return redirect('/dashboard')

@app.route("/cut/<string:sno>", methods=['GET','POST'])
def cut(sno):

         comment = Comments.query.filter_by(sno=sno).first()
         db.session.delete(comment)
         db.session.commit()
         flash("Deleted successfully")
         return redirect('/')



@app.route("/<string:post_slug>", methods=['GET','POST'])#variable post_slug FUnction eo dite hobe rules
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()#We use first for Unique Same name slug hobe na
    # slug=post_slug and it works as pass info from database
    comments=Comments.query.all()

    if (request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        date = datetime.now()
        message = request.form.get('message')
        comment = Comments(name=name,  msg=message, date=date, email=email)
        db.session.add(comment)
        db.session.commit()
        flash("Your Comment is submited successfully","success")
        return redirect(request.url)
    return render_template('post.html', params=params, post=post,comments=comments)



@app.route("/contact", methods = ['GET', 'POST']) #Get Fatch krte hoy Get dara Get request Post Use For More Sequrity
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        #fetch kra sesh ekhon add krbo
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )



    return render_template('contact.html',params=params)


app.run(debug=True)