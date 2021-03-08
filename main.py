### les operateurs servent a compare 2 valeur.

# == equivalent ?


# != different ?


# > ou < strictement superieur ou strictement inferieur

#>= ou <= inferieur ou egale /superieur ou egale


f = open("departments.csv","r")
data = f.read()
rows = data.split("\n")


department=[]
population=[]


for row in rows:
  value = row.split(",")
  population.append(int(value[1]))
  department.append(value[0])

print("departement avec ain comparaison")
first = department[0] == "Ain"
print(first)
second = department[1] == "Ain"
print(second)
third = department[2] == department[len(department) -1]
print(third)
print("population avec ain comparaison")
first_pop = population[0] > 500000
second_pop = population[0] > 650000
third_pop = population[0] >= population[-1]

print(first_pop)
print(second_pop)
print(third_pop)

###Condition if

age =35
greater=(age>12)
if greater: ### si greater et vrai, par defaut
  print(age)

###exercice

result =0

if department[5] == "Ardèche":
  result =1
  print(result)


condition2 = False

if population[0] > 600000:
  if population[1] > 300000:
    condition2 = True
  
print(condition2)

###conidition if et format
found = False

for dep in department:
  if dep == "Paris":
    found =True

if found is True:
  print("paris est la !!!")

  ###
  counter = 0
  index = 0

  for dep in department:
    if dep == "Paris":
      index = counter
    counter +=1
  
print(index)
print(counter)

#### exercice
mtmillion=[]


for dep in population:
  if dep > 1000000:
    mtmillion.append(dep)

print(mtmillion)