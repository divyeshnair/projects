from flask import Flask ,jsonify,request,render_template
#import MySQLdb

app =Flask(__name__)
a=0
b=1
#conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='testdb')
#x = conn.cursor()
   
@app.route('/map',methods=['GET'])
def jo():
   return render_template('check.html')
   

@app.route('/getValues', methods=['GET'])
def signUpUser():
   print a
   print b
   return jsonify(x=a,y=b)

def mod(val1,val2):
    global a
    global b
    a=val1
    b=val2
    

@app.route('/sendValues', methods=['POST'])
def see():
    a=request.form.get("a")
    b=request.form.get("b")
    mod(a,b)
    print a,b
    return "you said" + str(a)+str(b)

@app.route('/postVal', methods=['POST'])
def yo():
    aa=request.form.get("a")
    #f = open("see.txt",'a')
    #f.write(aa)
    #f.write("\n")
    #x.execute("insert into val values(%s,'1')"%(aa))
    #conn.commit()   
    return "Thanks man"    

app.debug=True
app.run(host='0.0.0.0',threaded=True)
