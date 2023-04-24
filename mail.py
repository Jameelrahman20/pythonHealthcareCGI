#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

import cgi
import pymysql
form=cgi.FieldStorage()

db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="newdb")
cur=db.cursor()

a1=form.getvalue("Patient_Name")
a2=form.getvalue("id")
a3=form.getvalue("Patient_age")
a4=form.getvalue("Gender")
a5=form.getvalue("num")
a6=form.getvalue("email")
a7=form.getvalue("b")
a8=form.getvalue("temp")
a9=form.getvalue("hw")
a10=form.getvalue("sl")
a11=form.getvalue("bp")
a12=form.getvalue("dn")
a13=form.getvalue("d")
a14=form.getvalue("ds")
a15=form.getvalue("pm1")
a16=form.getvalue("pm2")
a17=form.getvalue("mr")
a18=form.getvalue("ar")

query="insert into newtable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18]
cur.execute(query,val)
db.commit()


print('''
<html>
<head>
    <title>Patient Report Table</title>
    <link rel="stylesheet" href="style2.css">
    <link rel="stylesheet" href="style3.css">
</head>
<body>
    <center><h1 style='color:indigo;'>Patient Report Details</h1></center>
<table>
    <tr>
        <th>Name</th>
        <th>ID</th>
        <th>AgeGender</th>
        <th>Gender</th>
        <th>Contact Number</th>
        <th>Email-ID</th>
        <th>Blood Group</th>
        <th>Body Temperature (C/F)</th>
        <th>Height(cm)/Weight(kg)</th>
        <th>Sugar level(mg/dL)</th>
        <th>Blood Pressure(mmhg)</th>
        <th>Consulted Doctor</th>
        <th>Diagnosis</th>
        <th>Diagnosis Summary</th>
        <th>Medicine-1 Units/Timings</th>
        <th>Medicine-2 Units/Timings</th>
        <th>Madicine Stock/End Remainder Date</th>
        <th>Next Appointment Date</th>
    </tr>''')
cur.execute("select * from newtable")
for i in cur:
    print('''
        <tr>''')
    print("<td>",i[0],"</td>")
    print("<td>",i[1],"</td>")
    print("<td>",i[2],"</td>")
    print("<td>",i[3],"</td>")
    print("<td>",i[4],"</td>")
    print("<td>",i[5],"</td>")
    print("<td>",i[6],"</td>")
    print("<td>",i[7],"</td>")
    print("<td>",i[8],"</td>")
    print("<td>",i[9],"</td>")
    print("<td>",i[10],"</td>")
    print("<td>",i[11],"</td>")
    print("<td>",i[12],"</td>")
    print("<td>",i[13],"</td>")
    print("<td>",i[14],"</td>")
    print("<td>",i[15],"</td>")
    print("<td>",i[16],"</td>")
    print("<td>",i[17],"</td>")
    print('''
        </tr>''')
print('''</table>
<form action="comapre2.py" method=post>
    <div class="container">
        <button class="btn" type="submit">Next</button><br><br>
    </div>
</form>    
    <center><a href="http://localhost/MainProject%20-1/comapre1.py"<button class="block">Back</a></button></center>
</body>
</html>
''')







