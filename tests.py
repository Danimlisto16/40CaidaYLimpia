
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Ford', 'year': 2005},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

if cars[0] == cars[1]:
    print(True)
    cars.remove({'car': 'Ford', 'year': 2005})

print(cars)
