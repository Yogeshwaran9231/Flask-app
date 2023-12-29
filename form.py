from flask import Flask,render_template,request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/home')
def checkpoints():
    checkpoint=[{'serialNumber':'1', 'checklist':"Check for general cleanliness", 'checkpoints':"Should Free from dirt and oil"},
                {'serialNumber':'2', 'checklist':"Check for oil & Air leakages", 'checkpoints':"Should be free from leakages"},
                {'serialNumber':'3', 'checklist':"Check for grease lubrication", 'checkpoints':"Grease the chuck every 24 hrs"},
                {'serialNumber':'4', 'checklist':"Check Coolant oil level", 'checkpoints':"	Should be with in max and min mark"},
                {'serialNumber':'5', 'checklist':"Check Lubrication oil level", 'checkpoints':"	Should be with in max and min mark"},
                {'serialNumber':'6', 'checklist':"Check Hydraullic oil level", 'checkpoints':"	Should be with in max and min mark"},
                {'serialNumber':'7', 'checklist':"Check any Abnormal sound", 'checkpoints':"Should be within machine harmonics"},
                {'serialNumber':'8', 'checklist':"Check any Abnormal smell", 'checkpoints':"Should not have abnormal smell / fumes / smoke"},
                {'serialNumber':'9', 'checklist':"Check / Ensure neccesary screw fittings and tightness", 'checkpoints':"	For its correct / proper tightness"},
                {'serialNumber':'10', 'checklist':"Check the Emergency push buttons", 'checkpoints':"	For its proper functioning"},
                {'serialNumber':'11', 'checklist':"	Check work offset value after switching on the machine", 'checkpoints':"To ensure that the previous work offset value matches with existing value"},
                {'serialNumber':'12', 'checklist':"Check work offset value whenever is power restored after power failure", 'checkpoints':"To ensure that the previous work offset value matches with existing value"}]
    return render_template("base.html",checkpoint=checkpoint)

if __name__ == '__main__':  
   app.run(debug = True)  