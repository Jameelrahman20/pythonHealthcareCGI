#!C:\Python311\python.exe
print("Content-type:text/html\n\r")



print('''
<html>
<head>
    <title>Report Entry Panel</title>
    <link rel="stylesheet" href="style1.css">
</head>
<body>
    <div class="Report-form">
        <center><h2 style='color:blue;'>Patient Report Entry</h2></center>
        <form action="mail.py" method="post">
            <input type="text" name="Patient_Name" placeholder="Patient Name">
            <input type="text" name="id" placeholder="Patient-ID">
            <input type="text" name="Patient_age" placeholder="Patient Age">
            <input type="text" name="Gender" placeholder="Gender">
            <input type="text" name="num" placeholder="Patient Contact Number">
            <input type="email" name="email" placeholder="Patient Email-ID">
            <input type="text" name="b" placeholder="Patient Blood Group">
            <input type="text" name="temp" placeholder="Patient Body temperature (C/F)">
            <input type="text" name="hw" placeholder="Patient Height/Weight (Cm/Kg)">
            <input type="text" name="sl" placeholder="Patient Sugar Level (mg/dL)">
            <input type="text" name="bp" placeholder="Patient Blood Pressure Level (mmHg)">
            <input type="text" name="dn" placeholder="Consulted Doctor Name">
            <input type="text" name="d" placeholder="Diagnosis">
            <input type="text" name="ds" placeholder="Diagnosis summary">
            <input type="text" name="pm1" placeholder="Prescriped  Medicine-1 M-units(AM/BM)/A-units(AM/BM)/N-units(AM/BM) Time-(M/A/N)">
            <input type="text" name="pm2" placeholder="Prescriped  Medicine-2 M-units(AM/BM)/A-units(AM/BM)/N-units(AM/BM)) Time-(M/A/N)">
            <input type="text" name="mr" placeholder="Medicine Stock/End Reminder Date">
            <input type="text" name="ar" placeholder="Next Appointment Date">
            <center><button type="submit">Submit</button></center>
        </form>
    </div>
</body>
</html>
''')

