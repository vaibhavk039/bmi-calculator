from flask import Flask,request,render_template


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])

def bmi():
     bmi=0  
     classi=''
     health=''
     if request.method=="POST": 
       
        weight=request.form.get('weight')
        height=request.form.get('height')
        if weight=='' or height=='':
            bmi='No value entered!!'
            classi='No value entered!!'
            health='No value entered!!'
        else:    
            weight=float(weight)
            height=float(height)
            bmi=round(weight/((height/100)**2),2)
            if bmi < 18.5:
                classi='Underweight'
                health='Minimal'
            elif bmi > 18.5 and bmi <24.9:
                classi='Normal Weight'
                health='Minimal'
            elif bmi > 25 and bmi <29.9:
                classi='Over Weight'
                health='Increased'
            elif bmi > 30 and bmi <34.9:
                classi='Obese'
                health='High'
            elif bmi > 35 and bmi <39.9:
                classi='Severly Obese'
                health='Very High'
            else:
                classi='Morbidly Obese'
                health='Extremely High'

                        


        
     return render_template("/index.html",bmi=bmi,classi=classi,health=health)
        
    

if __name__ == '__main__':

     app.run(debug=True)    