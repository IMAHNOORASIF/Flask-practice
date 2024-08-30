# from flask import Flask , redirect,url_for
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hello! This is the main page <h1>HELLO<h1>'

# @app.route('/<name>')
# def user(name):
#     return f'hello {name}!'

# @app.route('/admin')
# def admin():
#     return redirect(url_for('user',name = 'Admin!'))

# if __name__ == '__main__':
#     app.run()

#.....................day2................................
# from flask import Flask , redirect,url_for , render_template
# app = Flask(__name__)
# @app.route("/<name>")
# def home(name):
#     return render_template("index.html",content = name,r=3)
# if __name__ == '__main__':
#     app.run()
#..................
# <!doctype html>
# <html>
# <head>
#     <title>Home page</title>
#     </head>
#     <body>
# 	    <h1>Home Page</h1>
#       {% for i in range(10)%}
#         {%if i%2==1 %}
#           <p>{{i}}</P>
#         {%endif%}
#      {%endfor%}
#     </body>
# </html>
#....................................
# @app.route("/<name>")
# def home(name):
    # return render_template("index.html" , content = ['manoo','hiba','sami'])
    
# <!doctype html>
# <html>
# <head>
#     <title>Home page</title>
#     </head>
#     <body>
# 	    <h1>Home Page</h1>
#       {% for i in content %}
#         <p>{{i}}</P>
#       {%endfor%}
#     </body>
# </html>
#     #...........
# from flask import Flask , redirect,url_for , render_template
# app = Flask(__name__)
# @app.route("/<name>")
# def home(name):
#     return render_template("index.html" , content={"a":2, "b":"hello"})
# if __name__ == '__main__':
#     app.run()

# # ['hiba','manoo','rabia','sami']
#...............................
# <!doctype html>
# <html>
# <head>
#     <title>Home page</title>
#     </head>
#     <body>
# 	    <h1>Home Page</h1>
#       {% if content == "true" %}
#          <p>True!</P>
#         {%else%}
#           <p>False</p>
      
#       {%endif%}

#     </body>
# </html>
#..................................
# from flask import Flask , redirect,url_for,render_template
# app = Flask(__name__) 
# @app.route('/')
# def home():
#     return render_template('index.html')



# if __name__ == '__main__':
#     app.run(debug=True)

#.................Baseclass.........
# <!doctype html>
# <html>
# <head>
#     <title>{%block title%}{%endblock%}</title>
#     </head>
#     <body>
# 	    <h1>Manoo's Website</h1>
#         {%block content%}
#         {%endblock%}


#     </body>
# </html> 

#............................index.html class//////////
# {%extends 'base.html'%}
# {%block title%}Home Page{%endblock%}
# {%block content%}
# <h1>Testing</h1>
# {%endblock%}
