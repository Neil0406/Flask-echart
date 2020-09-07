from flask import Flask
from flask import render_template
from hiskio_cl import hiskio
from 六角學院_cl import six
from 緯育_cl import wei
from job104 import job104
 
app = Flask(__name__)
 
 
@app.route("/")
def chart():
    title, avg = hiskio()                 #hiskio
    class_name , price ,people = six()    #六角學院 
    title1, avg1, mylist = wei()
    job, num = job104()                     
    
    return render_template('index.html', title=title, avg=avg, classname = class_name, price = price,
            people = people , title1 = title1, avg1 = avg1, mylist = mylist, job = job ,num = num
    
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)

