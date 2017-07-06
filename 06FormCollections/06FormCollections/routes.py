from flask import Flask, url_for, request, render_template;
from app import app;



@app.route('/')
def intro():
    """Renders a sample page."""
    return "Welcome to form collections!"


@app.route('/create', methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('CreateQuestion.html');
    elif request.method=='POST':
        title=request.form['title'];
        createdQuestion=request.form['createQuestion'];
        answerQuestion=request.form['answerQuestion'];
        #Store in data in database 
        #Here is the database code 
        return render_template('CreatedQuestion.html',question=createdQuestion,answer=answerQuestion);
    else:
       return "<h2>Invalid Request</h2>";



@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method=='GET':
        #Send the user the from 
         #Read Question from the database from title
         #Database check code here...
        question=" What is your Name?";       
        #Read QUestion from the store code here...
        return render_template('AnswerQuestion.html',question=question);

    elif request.method=='POST':      
         submittedAnswer=request.form['answer'];
         #Check your submitted answer
         #Read from database Code here..
         answer='Shohag';
         if submittedAnswer==answer:
            return render_template('Correct.html');
         else:
             return render_template('Incorrect.html',submittedAnswer=submittedAnswer,answer=answer);
            
    else:
        return "<h2>Invalid Request</h2>";