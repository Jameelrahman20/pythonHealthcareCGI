#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

import pymysql,cgi
form=cgi.FieldStorage()

db=pymysql.Connect(host="localhost", user="root" , password="10114nov",database="sign")
cur=db.cursor()


e=form.getvalue("em")
f=form.getvalue("ps")


cur.execute("select * from signinto")
for i in cur:
    if i[1]==e:
        if i[2]==f:
            print('''
            <html>
            <head>
                <title>Welcome Page</title>
                <link rel="stylesheet" href="style1.css">
            </head>
            <body>
                <div class="Report-form">
                    <center><h1 style='color:indigo;'>Welcome to AHR Healthcare</h1></center>
                     <form action="comapre1.py" method="post">
                        <center><button type="submit">Proceed</button></center>
                    </form>
                </div>
            </body>
            </html>
            ''')
