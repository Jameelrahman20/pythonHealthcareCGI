#!C:\Python311\python.exe
print("Content-type:text/html\n\r")


import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.Connect(host="localhost", user="root" , password="10114nov",database="sign")
cur=db.cursor()


a=form.getvalue("n")
b=form.getvalue("e")
c=form.getvalue("p")
d=form.getvalue("rp")

query="insert into signinto values(%s,%s,%s)"
val=[a,b,c]

cur.execute(query,val)
db.commit()

if c==d:
    print('''
    <html>
    <head>
            <title>Signup/Login Page</title>
            <link rel="stylesheet" href="style.css">	
    </head>
    <body>
            <div class="hero">
               <div class="form-box">
                    <div class="button-box">
                            <div id="btn"></div>
                            <button type="button" class="toggle-btn" onclick="login()">Log In</button>
                            <button type="button" class="toggle-btn" onclick="signup()">Signup</button>
                    </div>
                    <form id="signup" class="input-group" action="Signup_Backend.py" method="post">
                            <h5 style="color:blue;">AHR Healthcare</h5>
                            <input type="text" class="input-field " name="n" placeholder="admin Name" required>
                            <input type="email" class="input-field" name="e" placeholder="admin Email-ID" required>
                            <input type="password" class="input-field" name="p" placeholder="Password" required>
                            <input type="password" class="input-field" name="rp" placeholder="Reenter-Password" required>
                            <input type="checkbox" class="check-box"><span>I agree to the terms & conditions</span>
                            <button type="submit" class="submit-btn">Signup</button>
                    </form>
                    <form id="login" class="input-group" action="compare.py" method="post">
                            <h2 style="color:blue;">AHR Healthcare</h2>
                            <input type="email" class="input-field" name="em" placeholder="admin Email-ID" required>
                            <input type="password" class="input-field" name="ps"  placeholder="admin Password" required>
                            <input type="checkbox" class="check-box"><span>Remember Password</span>
                            <button type="submit" class="submit-btn">Login</button>
                    </form>		
               </div>
            </div>
            <script>
            var x = document.getElementById("login");
            var y = document.getElementById("signup");
            var z = document.getElementById("btn");
            
            function signup(){
                    x.style.left = "-400px";
                    y.style.left = "50px";
                    z.style.left = "110px";
            }
            function login(){
                    x.style.left = "50px";
                    y.style.left = "450px";
                    z.style.left = "0px";
            }
            </script>
            
    </body>
    </html> 
    ''')
else:
    print("<center><h1 style=color:red;>",a,"your Signup is Unsuccessfull</h1><center>")
    
