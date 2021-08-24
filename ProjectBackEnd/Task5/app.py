from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os 
import random

app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db=SQLAlchemy(app)

class News(db.Model):
    news_id=db.Column(db.Integer,primary_key=True)
    news_title=db.Column(db.String(100))
    news_nevs=db.Column(db.String(100))
    news_img=db.Column(db.String(100))

@app.route('/' , methods=['GET','POST'])
def index ():
    newss=News.query.all()
    if request.method=='POST':
        file=request.files['news_img']
        filename=secure_filename(file.filename)
        randomName=random.randint(1,1000)
        filename=str(randomName)+'.'+filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        title=request.form['news_title']
        nevs=request.form['news_nevs']
        img=request.form['news_img']
        news=News(
            news_title=title,
            news_nevs=nevs, 
            news_img=filename

        )
        db.session.add(news)
        db.session.commit()
        return redirect ('/')
    #select * from news
    return render_template('index.html' ,newss=newss)

@app.route('/admin' )
def admin():
    return render_template('admin.html')

@app.route('/panel' ,methods=['GET', 'POST'])
def panel():
   newss=News.query.all()
   if request.method=='POST':
        file=request.files['news_img']
        filename=secure_filename(file.filename)
        randomName=random.randint(1,1000)
        filename=str(randomName)+'.'+filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        title=request.form['news_title']
        nevs=request.form['news_nevs']
        img=request.form['news_img']
        news=News(
            news_title=title,
            news_nevs=nevs, 
            news_img=filename

        )
        db.session.add(news)
        db.session.commit()
        return redirect ('/')
    #select * from news
   return render_template('panel.html' ,newss=newss)

# @app.route('/delete/<int:id>')
# def delete(id):
#     news=News.query.filter_by(news_id=id).first()
#     db.session.delete(news)
#     db.session.commit()
#     return redirect('/')
#     return render_template('panel.html' , news=news)

@app.route('/add' , methods=['GET', 'POST'])
def add():
    newss=News.query.all()
    if request.method=='POST':
        file=request.files['file']
        filename=secure_filename(file.filename)
        randomName=random.randint(1,1000)
        filename=str(randomName)+'.'+filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        title=request.form['news_title']
        nevs=request.form['news_nevs']
        img=filename
        news=News(
            news_title=title,
            news_nevs=nevs, 
            news_img=filename

        )

        db.session.add(news)
        db.session.commit()
        return redirect ('/')
    #select * from news
    return render_template('add.html' , newss=newss)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):

    news=News.query.filter_by(news_id=id).first()
    if request.method=='POST':
        news=News.query.filter_by(news_id=id).first()
        news.news_title=request.form['news_title']
        news.news_nevs=request.form['news_nevs']
        
        db.session.commit()
        return redirect('/')
    return render_template('update.html', news=news)

@app.route('/delete/<int:id>')
def delete(id):
    news=News.query.filter_by(news_id=id).first()
    db.session.delete(news)
    db.session.commit()
    return redirect('/')
    return render_template('delete.html' , newss=newss)

@app.route('/about/<int:id>',methods=['GET','POST'])
def about(id):
    news=News.query.filter_by(news_id=id).first()
    if request.method=='POST':
        news=News.query.filter_by(news_id=id).first()
        news.news_title=request.form['news_title']
        news.news_nevs=request.form['news_nevs']
        
        db.session.commit()
        return redirect('/')
    return render_template('about.html', news=news)


# db.create_all()
if __name__=='__main__':
    app.run(debug=True)