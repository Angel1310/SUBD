from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'
mysql = MySQL(app)


@app.route('/movie_form')
def movie_form():
   return render_template('film.html')

@app.route('/actor_form')
def actor_form():
   return render_template('actors.html')

@app.route('/producer_form')
def producer_form():
   return render_template('company.html')

@app.route('/create_movie', methods = ['POST', 'GET'])
def create_movie():
    if request.method == 'POST':
        try:

            name = request.form['name']
            year = request.form['year']
            director = request.form['director']
            producer = request.form['producer']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO movie2 (name, year, director, producer) VALUES (%s, %s, %s, %s)", (name, int(year), director, int(producer)))
            mysql.connection.commit()
        except:
            cur.rollback()
        finally:
            cur.close()


    return render_template('film.html')

@app.route('/create_actor', methods = ['POST', 'GET'])
def create_actor():
    if request.method == 'POST':
        try:

            name = request.form['name']
            nationality = request.form['nationality']
            films = request.form['film']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO actor (name, nationality, film) VALUES (%s, %s, %s)", (name, nationality, films))
            mysql.connection.commit()
        except:
            cur.rollback()
        finally:
            cur.close()

    return render_template('actors.html')

@app.route('/create_producer', methods = ['POST', 'GET'])
def create_producer():
    if request.method == 'POST':
        try:
            name = request.form['name']
            capital = request.form['capital']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO producer (name, capital) VALUES (%s, %s)", (name, int(capital)))
            mysql.connection.commit()

        except:
            cur.rollback()
        finally:
            cur.close()

    return render_template('company.html')

@app.route('/show_movies')
def show_movies():
    movies = []
    try:



            cur = mysql.connection.cursor()
            resultValue = cur.execute("SELECT * FROM movie2")
            mysql.connection.commit()

            if resultValue > 0:
                movies = cur.fetchall()

    except:
        cur.rollback()
    finally:
        cur.close()

        return render_template('movies.html', movies = movies)

@app.route('/show_actors')
def show_actors():
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM actors")
			con.commit()
			actors = cur.fetchall()
	except:
		con.rollback()
	finally:
		con.close()


@app.route('/show_producers')
def show_producers():
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM producers")
			con.commit()
			producers = cur.fetchall()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM movies m WHERE m.id = ?", movie_id)
			con.commit()
			movie = cur.fetchone()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/actor/<int:actor_id>')
def actor(actor_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM actors a WHERE a.id = ?", actor_id)
			con.commit()
			producers = cur.fetchone()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/producer/<int:producer_id>')
def producer(producer_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM producers p WHERE p.id = ?", producer_id)
			con.commit()
			producers = cur.fetchone()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/delete_movie/<int:movie_id>')
def delete_movie(movie_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM movies m WHERE m.id = ?", movie_id)
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/delete_actor/<int:actor_id>')
def delete_actor(actor_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM actors a WHERE a.id = ?", actor_id)
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/delete_producer/<int:producer_id>')
def delete_producer(producer_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM producers p WHERE p.id = ?", producer_id)
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()

@app.route('/edit_movie/<int:movie_id>', methods = ['POST', 'GET'])
def edit_movie(movie_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			year = request.form['year']
			director = request.form['director']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE movies m SET m.name = ?, m.year = ?, m.director = ? WHERE m.id = ?", (name, year, director, movie_id))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

@app.route('/edit_actor/<int:actor_id>', methods = ['POST', 'GET'])
def edit_actor(actor_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			nationality = request.form['nationality']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE actors a SET a.name = ?, a.nationality = ? WHERE a.id = ?", (name, nationality, actor_id))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

@app.route('/edit_producer/<int:producer_id>', methods = ['POST', 'GET'])
def edit_producer(producer_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			capital = request.form['capital']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE producers p SET p.name = ?, p.capital = ? WHERE p.id = ?", (name, capital, producer_id))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

@app.route('/chose_movie_act/<int:actor_id>/<int:movie_id>')
def chose_movie_act(actor_id, movie_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE actors a SET a.film = ? WHERE a.id = ?", (movie_id, actor_id))
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()


if __name__ == '__main__':
	app.run(debug = True)
