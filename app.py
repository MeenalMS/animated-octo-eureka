from flask import Flask
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

@app.route('/hello', methods=['POST'])
def hello():
    return render_template('hello.html', name = name)

if __name__ == '__main__':
   app.run()
