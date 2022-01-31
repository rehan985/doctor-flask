from crypt import methods
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('uhome.html')

@app.route("/register")
def register():
    return render_template('uregister.html')

@app.route("/")
def login():
    return render_template('ulogin.html')

@app.route("/login_validation", methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    if email=='rehan@gmail.com'and password=='earth':
        return  redirect('/home')
    else :
        return " INVALID USERNAME AND PASSWORD ."

@app.route('/logout')
def logout():
    return redirect('/')
    
    
    # "The email is {} and password is {} ".format(email,password)



if __name__=='__main__':
    app.run(host='192.168.10.13',port='5000',debug=True)   
  
   
       