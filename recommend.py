from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
app = Flask(__name__,template_folder='/var/www/html/GameW/',static_folder='/var/www/html/GameW/')

import xlrd
import statistics 
from statistics import mode 
import MySQLdb

def connection():
	
	conn = MySQLdb.connect(host="localhost",
                           user = "newuser",
                           passwd = "password",
                           db = "login")
	c = conn.cursor()

	return c, conn

'''@app.route('/')
def homepage():
	content="Woah"
	c, conn = connection()
	sql = "Select * from search2 where data != ' ';"
	c.execute(sql)
	conn.commit()
	data = list(c.fetchall())

	#print(data)

	main_data=[]

	for i in data:
		main_data.append(list(i))
	dict=({'Adventure':{'God of War','Minecraft','Fortnite','Watch Dogs','Grand Theft Auto V','Spiderman','Past Cure'},'Horror':{'Resident Evil 2','Resident Evil 3','Doom Eternal','Outlast','Days Gone','Detention','Amnesia'},'Multiplayer':{'Warzone','CS-GO','Modern Warfare','Black Ops 4','Destiny 2','Far Cry 5','Apex Legends','Uncharted 4','Dota 2','Rainbow Six','Dota'},'Racing':{'Project Cars','Gran Turismo','F1','Forza Horizon','NFS Payback','Most Wanted','MotoGP'},'Sports':{'Fifa','NBA','NFL','PES','Fifa 19','Cricket 2019','WWE'}})

	for i in main_data:
		if(i[1] in dict['Adventure']):
			i.append('Adventure')
		if(i[1] in dict['Sports']):
			i.append('Sports')
		if(i[1] in dict['Horror']):
			i.append('Horror')
		if(i[1] in dict['Multiplayer']):
			i.append('Multiplayer')
		if(i[1] in dict['Racing']):
			i.append('Racing')
		
	#print(main_data)
	sql2 = "Select * from loggedin where user != ' ';"
	c.execute(sql2)
	conn.commit()
	usernames_list = list(c.fetchall())
	
	username=usernames_list[len(usernames_list)-1][1]
	#algorithm1 - Users Most viewed
	#username='ksgoutham1999@gmail.com'
	ctr=0
	for i in main_data:
	
		if(len(i) < 4):
			main_data.pop(ctr)
		ctr=ctr+1
	
	main_data.sort()
	user=[]
	for i in main_data:
		if(i[0]==username):
			user.append(i)
	#print(user)
	user_genre=[0,0,0,0,0]
	All_genre=['Adventure','Horror','Multiplayer','Racing','Sports']
	for i in user:
		#print(i)
		if i[3]=='Adventure':
			user_genre[0]=user_genre[0]+1
		elif i[3]=='Horror':
			user_genre[1]=user_genre[1]+1
		elif i[3]=='Multiplayer':
			user_genre[2]=user_genre[2]+1
		elif i[3]=='Racing':
			user_genre[3]=user_genre[3]+1
		elif i[3]=='Sports':
			user_genre[4]=user_genre[4]+1
	print(user_genre)

	users_current_games=[]
	for i in user:
		users_current_games.append(i[1])
	#print(users_current_games)

	recommended=[]
	maxposition = user_genre.index(max(user_genre)) 
	#print(maxposition)
	count1=0

	for i in (dict[All_genre[maxposition]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			count1=count1+1
			if(count1==2):
				break
	#print(recommended)
	content = recommended

	#algorithm2 - Users Most recent
	user.sort(key = lambda x: x[2])
	#print(user)
	latest2=[]
	latest2.append(user[-1])
	latest2.append(user[-2])
	#print(latest2)
	last2=[]
	for i in latest2:
		last2.append(i[3])
	#print(last2)
	#print(dict[last2[0]])
	for i in (dict[last2[0]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	for i in (dict[last2[1]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	print(recommended)

	content = recommended

	
	return render_template("sample.html",content=content)


@app.route('/page2')
def page2():
	c, conn = connection()
	sql = "Select * from search2 where data != ' ';"
	c.execute(sql)
	conn.commit()
	data = list(c.fetchall())

	#print(data)

	main_data=[]

	for i in data:
		main_data.append(list(i))
	dict=({'Adventure':{'God of War','Minecraft','Fortnite','Watch Dogs','Grand Theft Auto V','Spiderman','Past Cure'},'Horror':{'Resident Evil 2','Resident Evil 3','Doom Eternal','Outlast','Days Gone','Detention','Amnesia'},'Multiplayer':{'Warzone','CS-GO','Modern Warfare','Black Ops 4','Destiny 2','Far Cry 5','Apex Legends','Uncharted 4','Dota 2','Rainbow Six','Dota'},'Racing':{'Project Cars','Gran Turismo','F1','Forza Horizon','NFS Payback','Most Wanted','MotoGP'},'Sports':{'Fifa','NBA','NFL','PES','Fifa 19','Cricket 2019','WWE'}})

	for i in main_data:
		if(i[1] in dict['Adventure']):
			i.append('Adventure')
		if(i[1] in dict['Sports']):
			i.append('Sports')
		if(i[1] in dict['Horror']):
			i.append('Horror')
		if(i[1] in dict['Multiplayer']):
			i.append('Multiplayer')
		if(i[1] in dict['Racing']):
			i.append('Racing')
		
	#print(main_data)
	sql2 = "Select * from loggedin where user != ' ';"
	c.execute(sql2)
	conn.commit()
	usernames_list = list(c.fetchall())
	username=usernames_list[len(usernames_list)-1][1]
	#algorithm1 - Users Most viewed
	#username='ksgoutham1999@gmail.com'
	
	ctr = 0
	#print(main_data)
	for i in main_data:
		
		if(len(i) < 4):
			main_data.pop(ctr)
		ctr=ctr+1	

	main_data.sort()
	user=[]
	for i in main_data:
		if(i[0]==username):
			user.append(i)
	#print(user)
	user_genre=[0,0,0,0,0]
	All_genre=['Adventure','Horror','Multiplayer','Racing','Sports']
	for i in user:
		#print(i)
		if i[3]=='Adventure':
			user_genre[0]=user_genre[0]+1
		elif i[3]=='Horror':
			user_genre[1]=user_genre[1]+1
		elif i[3]=='Multiplayer':
			user_genre[2]=user_genre[2]+1
		elif i[3]=='Racing':
			user_genre[3]=user_genre[3]+1
		elif i[3]=='Sports':
			user_genre[4]=user_genre[4]+1
	print(user_genre)

	users_current_games=[]
	for i in user:
		users_current_games.append(i[1])
	
	recommended=[]
	maxposition = user_genre.index(max(user_genre)) 
	#print(maxposition)
	count1=0

	for i in (dict[All_genre[maxposition]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			count1=count1+1
			if(count1==2):
				break
	#print(recommended)
	#content = recommended

	#algorithm2 - Users Most recent
	user.sort(key = lambda x: x[2])
	#print(user)
	latest2=[]
	latest2.append(user[-1])
	latest2.append(user[-2])
	#print(latest2)
	last2=[]
	for i in latest2:
		last2.append(i[3])
	#print(last2)
	#print(dict[last2[0]])
	for i in (dict[last2[0]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	for i in (dict[last2[1]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	print(recommended)

	content = recommended
	return render_template("sample.html",content=content)'''

@app.route('/')
def recommend():
	

	c, conn = connection()
	sql = "Select * from search2 where data != ' ';"
	c.execute(sql)
	conn.commit()
	data = list(c.fetchall())

	#print(data)

	main_data=[]

	for i in data:
		main_data.append(list(i))
	dict=({'Adventure':{'God of War','Minecraft','Fortnite','Watch Dogs','Grand Theft Auto V','Spiderman','Past Cure'},'Horror':{'Resident Evil 2','Resident Evil 3','Doom Eternal','Outlast','Days Gone','Detention','Amnesia'},'Multiplayer':{'Warzone','CS-GO','Modern Warfare','Black Ops 4','Destiny 2','Far Cry 5','Apex Legends','Uncharted 4','Dota 2','Rainbow Six','Dota'},'Racing':{'Project Cars','Gran Turismo','F1','Forza Horizon','NFS Payback','Most Wanted','MotoGP'},'Sports':{'Fifa','NBA','NFL','PES','Fifa 19','Cricket 2019','WWE'}})

	for i in main_data:
		if(i[1] in dict['Adventure']):
			i.append('Adventure')
		if(i[1] in dict['Sports']):
			i.append('Sports')
		if(i[1] in dict['Horror']):
			i.append('Horror')
		if(i[1] in dict['Multiplayer']):
			i.append('Multiplayer')
		if(i[1] in dict['Racing']):
			i.append('Racing')
		
	#print(main_data)
	sql2 = "Select * from loggedin where user != ' ';"
	c.execute(sql2)
	conn.commit()
	usernames_list = list(c.fetchall())
	username=usernames_list[len(usernames_list)-1][1]
	#algorithm1 - Users Most viewed
	#username='ksgoutham1999@gmail.com'
	
	ctr = 0
	#print(main_data)
	for i in main_data:
		
		if(len(i) < 4):
			main_data.pop(ctr)
		ctr=ctr+1	

	main_data.sort()
	user=[]
	for i in main_data:
		if(i[0]==username):
			user.append(i)
	#print(user)
	if(len(user)==0):
		print("Unavailable")
		return render_template("sample.html",content="UNAVAILABLE")

	user_genre=[0,0,0,0,0]
	All_genre=['Adventure','Horror','Multiplayer','Racing','Sports']
	for i in user:
		#print(i)
		if i[3]=='Adventure':
			user_genre[0]=user_genre[0]+1
		elif i[3]=='Horror':
			user_genre[1]=user_genre[1]+1
		elif i[3]=='Multiplayer':
			user_genre[2]=user_genre[2]+1
		elif i[3]=='Racing':
			user_genre[3]=user_genre[3]+1
		elif i[3]=='Sports':
			user_genre[4]=user_genre[4]+1
	print(user_genre)

	users_current_games=[]
	for i in user:
		users_current_games.append(i[1])
	
	recommended=[]
	maxposition = user_genre.index(max(user_genre)) 
	#print(maxposition)
	count1=0

	for i in (dict[All_genre[maxposition]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			count1=count1+1
			if(count1==2):
				break
	#print(recommended)
	#content = recommended

	#algorithm2 - Users Most recent
	user.sort(key = lambda x: x[2])
	#print(user)
	latest2=[]
	latest2.append(user[-1])
	latest2.append(user[-2])
	#print(latest2)
	last2=[]
	for i in latest2:
		last2.append(i[3])
	#print(last2)
	#print(dict[last2[0]])
	for i in (dict[last2[0]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	for i in (dict[last2[1]]):
		if(i not in users_current_games and i not in recommended):
			recommended.append(i)
			break
	print(recommended)

	games=[]
	for i in main_data:
		games.append(i[1])
	recommended.append(mode(games))

	content = recommended
	print(recommended)
	return render_template("sample.html",content=content)
	
@app.route('/search',methods=["GET"])
def search():
	c, conn = connection()
	sql = "Select * from search2 where data != ' ';"
	c.execute(sql)
	conn.commit()
	data = list(c.fetchall())
	main_data=[]

	for i in data:
		main_data.append(list(i))
	search_name = main_data[len(main_data)-1][1]
	print(search_name)
	content = search_name
	return render_template("search.html",content=content)

if __name__ == "__main__":
	app.run(port='8090')

