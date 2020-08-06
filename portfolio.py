from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

'''
@app.route('/index.html')
def index_page():
    return render_template('index.html')

@app.route('/works.html')
def works_page():
    return render_template('works.html')

@app.route('/work.html')
def work_page():
    return render_template('work.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')
'''

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

'''
In contact.html, we have added action inn line 62 as Submit_form and method as post
so when form is submitted in web page,it will post info to user
as form submitted huraayyy!
'''

'''
I have added name attributes(email,subject,message) in contact/html for forms
and user details will be recieved by browser, check in developer tools
'''

def write_to_file(data):  # Getting user's filled form data into file.txt
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')

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



