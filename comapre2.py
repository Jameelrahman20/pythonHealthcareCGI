#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

print('''
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equi="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width",initial-scale=1.0>
    <title>Alert Mail Box</title>
    <link rel="stylesheet" href="style4.css">
    <link rel="stylesheet" href="https://kit.fontawesome.com/941411a49e.css" crossorigin="anonymous">
</head>
<body>
    <form action="sent.py" method="post">
    <div class="container">
        <div class="box">
            <h3 style="color:indigo;">Mail Alert Box</h3>
            <div class="name1">
                <i class="fas fa-user"></i>
                <input type="email" placeholder="admin Mail-ID" id="name1" name="a1">
            </div>
            <div class="name">
                <i class="fas fa-user"></i>
                <input type="email" placeholder="Patient Mail-ID" id="name" name="a2">
            </div>
            <div class="email">
                <i class="fas fa-envelope"></i>
                <input type="text" placeholder="Subject" id="email" name="s1">
            </div>
            <div class="message-box">
                <textarea id="msg" cols="30" rows="10" placeholder="Message" name="m1"></textarea>
            </div>
             <div class="email">
                <i class="fas fa-envelope"></i>
                <input type="text" placeholder="Subject" id="email" name="s2">
            </div>
            <div class="message-box">
                <textarea id="msg" cols="30" rows="10" placeholder="Message" name="m2"></textarea>
            </div>
            <div class="email">
                <i class="fas fa-envelope"></i>
                <input type="text" placeholder="Subject" id="email" name="s3" >
            </div>
            <div class="message-box">
                <textarea id="msg" cols="30" rows="10" placeholder="Message" name="m3"></textarea>
            </div>
            <div class="email">
                <i class="fas fa-envelope"></i>
                <input type="text" placeholder="Subject" id="email" name="s4">
            </div>
            <div class="message-box">
                <textarea id="msg" cols="30" rows="10" placeholder="Message" name="m4"></textarea>
            </div>
            <div class="button">
                <button id="send">Send</button><br><br>
            </div>
            <div class="button1">
               <center><a href="http://localhost/MainProject%20-1/signup_frontend.html"<button class="block">logout</a></button></center>
            </div>
        </div>
    </div>
    </form>
</body>
</html>
''')
