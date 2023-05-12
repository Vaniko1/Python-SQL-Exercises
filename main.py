import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("movies_ranking.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT * FROM movies WHERE Genre='Drama'")
# მე-6 ხაზზე ბრძანება იძახებს იმ ფილმების ინფორმაციას ბაზიდან, რომელების ჟანრიც არის დრამა.

# record_one = cursor.fetchone()
# record_two = cursor.fetchmany()
# record_three = cursor.fetchall()
#
# print('fetchone:', record_one)
# print('fetchmany:', record_two)
# print('fetchall:', record_three)

# ქვემოთ მოცემული კოდი საშუალებას გვაძლევს, რომ ჩავამატოთ ჩვენთვის სასურველი ფილმი და მისი მონაცემები ჩვენს ბაზაში

# user_film = input('შეიყვანეთ თქვენთვის სასურველი ფილმი: ')
# user_genre = input('შეიყვანეთ ამ ფილმის ჟანრი: ')
# user_leadStudio = input('შეიყვანეთ ამ ფილმის სტუდიოს სახელი: ')
# user_worldWideGross = float(input('შეიყვანეთ ამ ფილმის მსოფლიო world wide gross: '))
# user_year = input('შეიყვანეთ ამ ფილმის გამოშვების წელი: ')
#
# user_info = (user_film, user_genre, user_leadStudio, user_worldWideGross, user_year)
#
# cursor.execute('INSERT INTO movies (Film, Genre, LeadStudio, WorldwideGross, Year) VALUES (?, ?, ?, ?, ?)', user_info)
#
# conn.commit()

# ქვემოთ მოცემული კოდი საშუალებას გვაძლევს, რომ შევცვალოთ კომედიის ჟანრის ფილმების გამოშვების წლები

# update_year = int(input('შეიყვანეთ თქვენთვის სასურველი წელიწადი: '))
#
# cursor.execute("UPDATE movies SET Year=:pr WHERE Genre='Comedy'", {'pr': update_year})
# print(cursor.rowcount)
# conn.commit()


# ეს კოდი საშუალებას გვაძლევს, რომ წავშალოთ ფილმის მონაცემები, ფილმის გამოცემის წლოვანების მიხედვით, ანუ ავირჩევთ წელს და
# მაგ ფილმის მონაცემები ბაზიდან წაიშლება.

# user_delete = int(input("რომელი წლების ფილმები გინდათ რომ წავშალოთ ბაზიდან? "))
#
# cursor.execute("DELETE FROM movies WHERE Year=:pr", {'pr': user_delete})
# print(cursor.rowcount)
# conn.commit()

# ქვემოთ მოცემული კოდით ვნახავთ დიაგრამას იმის შესახებ, თუ რამდენი კომედიის, ანიმაციის, დრამის, რომანტიკისა და ფენტეზის ფილმი
# არის ბაზაში.

# fig, ax = plt.subplots()
#
# cursor.execute("SELECT * FROM movies WHERE genre='Comedy'")
#
# comedy = len(cursor.fetchall())
#
# cursor.execute("SELECT * FROM movies WHERE genre='Animation'")
#
# animation = len(cursor.fetchall())
#
# cursor.execute("SELECT * FROM movies WHERE genre='Drama'")
#
# drama = len(cursor.fetchall())
#
# cursor.execute("SELECT * FROM movies WHERE genre='Romance'")
#
# romance = len(cursor.fetchall())
#
# cursor.execute("SELECT * FROM movies WHERE genre='Fantasy'")
#
# fantasy = len(cursor.fetchall())
#
# print(comedy, animation, drama, romance, fantasy)
#
#
# fruits = ['Comedy', 'Animation', 'Drama', 'Romance', 'Fantasy']
# counts = [comedy, animation, drama, romance, fantasy]
# bar_labels = ['red', 'blue', '_red', 'orange', 'green']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
#
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('ფილმების რაოდენობა')
# ax.set_title('ფილმების რაოდენობა ფერისა და რიცხვების მიხედვით')
# ax.legend(title='ჟანრის ფერები')
#
# plt.show()


conn.close()