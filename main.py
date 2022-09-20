# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1
scorer_0 = "Ruud Gullit " #First player to score a goal 
scorer_1 = "Marco van Basten " #Second player to score a goal 
goal_0 = 32 #minute of the first goal
goal_1 = 54 #minute of the second goal

scorers = f"{scorer_0}{goal_0}, {scorer_1}{goal_1}"
print (scorers)
report = f"{scorer_0}scored in the {goal_0}nd minute\n{scorer_1}scored in the {goal_1}th minute" 
print (report)

#part 2
player = "Paul Walker"
print (player.find(" ")) #geeft aan 6
first_name = player[0:(player.find(" "))] #van begin tot spatie is voornaam
print (first_name)
last_name = player[(player.find(" ")+ 1):(len(player))] #vanaf de spatie plus 1 zodat je de eerste letter van achternaam pakt en dan tot het eind van de hele naam
print (last_name)
last_name_len = len(player[(player.find(" ")+ 1):(len(player))]) 
print (last_name_len)

name_short = f"{first_name[0]}. {last_name}"
print (name_short)

chant = ((first_name) + '! ') * (len(first_name)- 1) + first_name + "!"
print (chant) 
print (len(chant)) #hiermee kijken hoelang de zin is en dus wat de laatste letter/getal is
good_chant = (chant[len(chant) - 1] != " ") #-1 omdat het vanaf 0 begint met tellen
print (good_chant) #geeft aan true dus laatste letter van chant is geen spatie



