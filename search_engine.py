import os, time
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
from build_table import *

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
final_table, table1 = [],[]
ref = {'Avengers-AgeofUltron': ['Avengers-Age of Ultron (2015)', 'tt2395427'], 'GuardiansoftheGalaxyVol2': ['Guardians of the Galaxy Vol.2 (2017)', 'tt3896198'], 'TheAmazingSpiderMan2':['The Amazing Spider-Man 2 (2014)','tt1872181'],'ADogsPurpose':['A Dogs Purpose(2017)','tt1753383'], 'InsideOut':['Inside Out(2015)','tt2096673'],'TheFateoftheFurious':['The Fate of the Furious(2017)','tt4630562'], 'BeautyandtheBeast':['Beauty and the Beast(2017)','tt2771200'], 'Interstellar':['Interstellar (2014)','tt0816692'], 'TheHobbit-TheBattleoftheFiveArmies':['The Hobbit: The Battle of the Five Armies (2014)','tt2310332'], 'CaptainAmerica-CivilWar':['Captain America: Civil War (2016)','tt3498820'], 'It':['It (2017)','tt1396484'], 'TheHungerGames-Mockingjay-Part2':['The Hunger Games: Mockingjay - Part 2 (2015)','tt1951266'], 'TheHungerGames-Mockingjay-Part1':['The Hunger Games: Mockingjay - Part 1 (2014)','tt1951265'], 'CaptainAmerica-TheWinterSoldier':['Captain America: The Winter Soldier (2014)','tt1843866'], 'JurassicWorld':['Jurassic World','tt0369610'],'CatsandDogs':['Cats and Dogs (2001)','tt0239395'], 'JusticeLeague':['Justice League (2017)','tt0974015'], 'TheJungleBook':['The Jungle Book (2016)','tt3040964']}

@app.before_request
def before_request():
  print "searh engine starts..."



@app.teardown_request
def teardown_request(exception):
  print "search engine tears..."



@app.route('/')
def homepage():
  return render_template("homepage.html")


@app.route('/do_query_post', methods = ['POST'])
def do_search():
  start_time = time.time()
  a, c, result = [],[],[]
  query = str(request.form['query'])
  tmp = Sentence_Match(final_table, query, table1)
  for s in tmp:
    result.append(str(s)[:-4])
  for ll in result:
    try:
      b = []
      b.append('http://www.imdb.com/title/'+ref[ll][1])
      b.append(ref[ll][0])
      a.append(b)
    except:
      print ref[ll]

  num = len(result)
  query = query.replace(" ","_")
  c.append(query)
  time_passed = time.time()-start_time
  context = dict(data = a, data2 = c, data3 = num, data4 = time_passed)
  return render_template("result.html", **context)


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8113, type=int)
  def run(debug, threaded, host, port):

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=True, threaded=threaded)
  
  table1 = Build_Table()
  final_table = Final_Table(table1)
  ref['DawnofthePlanetoftheApes'] = ['Dawn of the Planet of the Apes (2014)', 'tt2103281']
  ref['Maleficent'] = ['Maleficent (2014)','tt1587310']
  ref['TheMartian'] = ['The Martian (2015)','tt3659388']
  ref['Deadpool'] = ['Deadpool (2016)','tt1431045']
  ref['Minions'] = ['Minions (2015)', 'tt2293640']
  ref['TheSecretLifeofPets'] = ['The Secret Life of Pets (2016)','tt2709768']
  ref['DeathataFuneral'] = ['Death at a Funeral (2007)','tt0795368']
  ref['Mission-Impossible-RogueNation'] = ['Mission: Impossible - Rogue Nation (2015)', 'tt2381249']
  ref['Thor-Ragnarok'] = ['Thor: Ragnarok (2017)','tt3501632']
  ref['DespicableMe3'] = ['Despicable Me 3 (2017)','tt3469046']
  ref['PiratesoftheCaribbean-DeadMenTellNoTales'] = ['Pirates of the Caribbean: Dead Men Tell No Tales (2017)','tt1790809']
  ref['Transformers-AgeofExtinction'] = ['Transformers: Age of Extinction (2014)','tt2109248']
  ref['Dunkirk'] = ['Dunkirk (2017)', 'tt5013056']
  ref['RogueOne'] = ['Rogue One (2016)','tt3748528']
  ref['WolfWarrior2'] = ['Wolf Warrior II (2017)','tt7131870']
  ref['FantasticBeastsandWheretoFindThem'] = ['Fantastic Beasts and Where to Find Them (2016)','tt3183660']
  ref['Spectre'] = ['Spectre (2015)','tt2379713']
  ref['WonderWoman'] = ['Wonder Woman (2017)', 'tt0451279']
  ref['FindingDory'] = ['Finding Dory (2016)', 'tt2277860']
  ref['SpiderMan-Homecoming'] = ['Spider-Man: Homecoming (2017)', 'tt2250912']
  ref['X-Men-DaysofFuturePast'] = ['X-Men: Days of Future Past (2014)', 'tt1877832']
  ref['Furious7'] = ['Furious 7 (2015)','Furious7']
  ref['StarWars-TheForceAwakens'] = ['Star Wars: The Force Awakens (2015)', 'tt2488496']
  ref['Zootopia'] = ['Zootopia (2016)','tt2948356']
  ref['GuardiansoftheGalaxy'] = ['Guardians of the Galaxy (2014)', 'tt2015381']
  ref['SuicideSquad'] = ['Suicide Squad (2016)', 'tt1386697']
  ref['PiratesoftheCaribbean-TheCurseoftheBlackPearl'] = ['Pirates of the Caribbean: The Curse of the Black Pearl (2003)', 'tt0325980']
  ref['PiratesoftheCaribbeanDeadMansChest'] = ['Pirates of the Caribbean: Dead Mans Chest (2006)', 'tt0383574']
  ref['PiratesoftheCaribbean-AtWorldsEnd'] = ['Pirates of the Caribbean: At Worlds End (2007)', 'tt0449088']
  ref['LaLaLand'] = ['La La Land (2016)','tt3783958']
  ref['TheLegendof1900'] = ['he Legend of 1900 (1998)', 'tt0120731']
  ref['FiftyShadesofGrey'] = ['Fifty Shades of Grey (2015)', 'tt2322441']
  ref['Twilight'] = ['Twilight (2008)', 'tt1099212']
  ref['HarryPotter7'] = ['Harry Potter and the Deathly Hallows (2011)', 'tt1201607']
  ref['HarryPotter6'] = ['Harry Potter and the Half-Blood Prince (2009)', 'tt0417741']
  ref['MoneyBall'] = ['MoneyBall (2011)', 'tt1210166']
  ref['Troy'] = ['Troy (2004)', 'tt0332452']
  ref['Avatar'] = ['Avatar (2009)', 'tt0499549']
  ref['AbrahamLincoln-VampireHunter'] = ['Abraham Lincoln: Vampire Hunter (2012)', 'tt1611224']
  ref['TheLure'] = ['The Lure (2015)', 'tt5278832']
  ref['FiftyShadesDarker'] = ['Fifty Shades Darker (2017)', 'tt4465564']
  ref['TheTwilightSaga-NewMoon'] = ['The Twilight Saga: New Moon (2009)', 'tt1259571']
  ref['Transformers'] = ['Transformers (2007)', 'tt0418279']
  ref['TheLordoftheRings'] = ['The Lord of the Rings: The Fellowship of the Ring (2001)', 'tt0120737']
  ref['TheLordoftheRings-TheTwoTowers'] = ['The Lord of the Rings: The Two Towers (2002)', 'tt0167261']

  
  run()


