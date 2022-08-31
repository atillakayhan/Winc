# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1
scorer_0 = "Ruud Gullit " #First player to score a goal 
scorer_1 = "Marco van Basten " #Second player to score a goal 
goal_0 = 32 #minute of the first goal
goal_1 = 54 #minute of the second goal

scorers = (scorer_0 + str(goal_0), scorer_1 + str(goal_1))
print (scorers)
report = f"{scorer_0}scored in the {goal_0}nd minute \n{scorer_1}scored in the {goal_1}th minute " 
print (report)

#part 2
player = "Ronald Koeman "
first_name = player[:6]
print (player.find("Ronald"))
print (player.find("Koeman"))
last_name = player[7:13] #13 omdat je dan de spatie niet meerekent bij len(last_name)
print (first_name)
print (last_name)
last_name_len = (len(player[7:13])) #alleen de lengte van achternaam
last_name_len_1 = player[7:] + str(len(last_name)) #met naam en lengte in 1
print (last_name_len)
print (last_name_len_1)

name_short = f"{first_name[0]}. {last_name} "
print (name_short)

chant = f"{first_name}! {first_name}! {first_name}! {first_name}! {first_name}! {first_name}!"
print (chant)
print (len(chant)) #hiermee kijken hoelang de zin is en dus wat de laatste letter/getal is
good_chant = (chant[46] != " ") #vergelijking van laatste letter (chant) met "spatie" (46 omdat het via de 0 begint ipv 1)
print (good_chant) #geeft aan true dus laatste letter van chant is geen spatie






