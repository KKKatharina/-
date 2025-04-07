from flask import Flask, render_template, request, redirect

app = Flask(__name__)
records = []

@app.route('/')
def index():
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
            'description': request.form['description'],
            'date': request.form['date']
        }
        records.append(new_record)
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    # 使用 index 來找到並刪除紀錄
    if 0 <= index < len(records):
        records.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
