from flask import Flask, render_template, request, redirect, url_for
import dbUtils

app = Flask(__name__)

@app.route('/')
def index():
    records = dbUtils.get_all_records()
    income = sum(r['amount'] for r in records if r['type'] == 'income')
    expense = sum(r['amount'] for r in records if r['type'] == 'expense')
    balance = income - expense
    return render_template('index.html', records=records, income=income, expense=expense, balance=balance)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_record = {
            'type': request.form['type'],
            'amount': float(request.form['amount']),
            'description': request.form.get('description', ''),
            'date': request.form['date']
        }
        dbUtils.insert_records(new_record)
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    dbUtils.delete_records(record_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
