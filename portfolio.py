from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



def write_to_csv(data):  # Getting user's filled form data into file.txt
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/Submit_form', methods=['POST', 'GET'])
def Submit_form():
    '''
    with this function we will get user's contact form input
    in python output
    '''
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return "Something wrong.Try again!"



