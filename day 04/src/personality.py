import random


def turrets_generator():
    while True:
        neuroticism = random.randint(0, 100)
        openness = random.randint(0, 100)
        conscientiousness = random.randint(0, 100)
        extraversion = random.randint(0, 100)
        agreeableness = random.randint(0, 100)
        traits = [neuroticism, openness,
                  conscientiousness, extraversion, agreeableness]
        if sum(traits) != 100:
            continue
        methods = {
            'shoot': lambda self: print('Shooting'),
            'search': lambda self: print('Searching'),
            'talk': lambda self: print('Talking')
        }
        turret = type('Turret', (), methods)()
        turret.neuroticism = neuroticism
        turret.openness = openness
        turret.conscientiousness = conscientiousness
        turret.extraversion = extraversion
        turret.agreeableness = agreeableness
        yield turret


turrets = turrets_generator()

turret1 = next(turrets)
print(turret1.neuroticism, turret1.openness, turret1.conscientiousness,
      turret1.extraversion, turret1.agreeableness)
turret1.shoot()
turret1.search()
turret1.talk()
