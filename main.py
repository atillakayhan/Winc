# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1
def greet(name, template='Hello, <name>!'):
    new_template = template.replace('<name>', name)
    return new_template

print(greet('atilla', 'yooow <name>'))

#Part 2
dict_info_planets = {
        'sun': 274, 'jupiter': 24.9, 'neptune': 11.2, 'saturn': 10.4,
        'earth': 9.8, 'uranus': 8.9, 'venus': 8.9, 'mars': 3.7, 
        'mercury': 3.7, 'moon': 1.6, 'pluto': 0.6
    }
def force(mass, body='earth'):
    world = (dict_info_planets[body])
    calculation = (mass * world)
    return round(calculation)
print(force(100))

#part 3
def pull(m1, m2, d):
    gravity = 6.674*10**-11
    distance_2 = d ** 2
    calculation_1 = (m1 *m2) / distance_2
    calculation_2 = gravity * calculation_1
    return calculation_2
print(pull(800, 1500, 3))