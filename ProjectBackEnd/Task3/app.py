import re
from flask import Flask,render_template,request,redirect




class News():
    def __init__(self,_id,_text,_textName,_date,_textCont):
        self.id = _id
        self.text = _text
        self.textName =_textName
        self.date = _date
        self.textCont = _textCont

newss=[]

_id=1
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('index.html',newss=newss)

@app.route("/newspage")
def newspage():
    return render_template('newspage.html',newss=newss)

@app.route("/showNews/<id>")
def show(id):
    for n in newss:
        if n.id==int(id):
            return render_template('newspage.html',xeber=n)
    return render_template('newspage.html')


@app.route("/admin")
def adminSide():
    return render_template('/admin/index.html',newss=newss)

@app.route("/admin/add_news",methods=['GET','POST'])
def admin_add_news():
    if request.method=='POST':
        global _id
        _text = request.form['text']
        _textName = request.form['textName']
        _date = request.form['date']
        _textCont = request.form['textCont']
        new=News(_id,_text,_textName,_date,_textCont)
        newss.append(new)
        _id +=1
        return redirect ('/')
    return render_template('/admin/add_news.html')

@app.route("/admin/newsRemove")
def removeSide():
    return render_template('admin/newsRemove.html',newss=newss)

@app.route("/admin/delete_news/<id>")
def news_delete(id):
    for new in newss:
        if new.id==int(id):
            newss.remove(new)
            return redirect('/admin')
    return redirect('/admin')


@app.route("/admin/change/<id>", methods=['GET','POST'])
def change(id):
    if request.method=='POST':
        _textName=request.form['textName']
        _text=request.form['text']
        _date=request.form['date']
        _textCont=request.form['textCont']
        for new in newss:
            if new.id==int(id):
                new.text=_text
                new.textName=_textName
                new.date=_date
                new.textCont=_textCont
                return redirect('/')
    for new in newss:
        if new.id==int(id):
            return render_template("admin/change.html",new=new)
    
    return redirect('/admin')

if __name__=='__main__':
    app.run(debug=True)