@app.route('/sending')
def testing():
    a=10
    b=20
    c=[a,b]
    return redirect(url_for('receive',c=c))
@app.route('/receive/<c>')
def receive(c):
    data=c
    print("data",data)
    return render_template('receive.html', data=data)
