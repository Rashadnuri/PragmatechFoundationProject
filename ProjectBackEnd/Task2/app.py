from flask import Flask,render_template

app=Flask(__name__,template_folder='front')

isciler= [
    {
        'ad':'Rashad',
        'soyad':'Nuriyev',
        'email':'resadnuri@gmail.com'

    },
    {
        'ad':'Arif',
        'soyad':'Quliyev',
        'email':'arif1212@gmail.com'

    },
    {
        'ad':'Hesen',
        'soyad':'Eliyev',
        'email':'hesen232@gmail.com'

    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/work')
def work():
    return render_template('work.html' , isciler=isciler)

if __name__=='__main__':
    app.run(debug=True)