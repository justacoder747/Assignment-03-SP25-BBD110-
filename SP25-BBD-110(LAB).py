#Part A

person ={
    'name': 'Noor',
    'age': 21,
    'hobby':'Reading'
}

#Part B

text = "hello world"
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

#Part C

inventory = {'mangoes':7,'bananas':12}


#Part D

orders=['stationary','clothig','electronics','clothing']

#Part E

grades={'Noor':74, 'Muhammad':82,'Ali':88}
average= sum(grades.values())/len(grades)
print("Average grade:",average)

#Part F

products = {
    'pen':{'quantity': 70, 'price':8},
    'pencil':{'quantity': 80, 'price':8}
}

#Part G

gradebook = {
    "Noor": {"Math": 75, "English": 80},
    "Muhammad": {"Math": 62, "English": 95},
    "Ali": {"Math": 68, "English": 89}
}

averages = {}

for student, subjects in gradebook.items():
    total = 0
    count = 0
    for subject, mark in subjects.items():
        total += mark
        count += 1
    avg = total / count
    averages[student] = avg
    print(f"{student}'s average grade is: {avg}")

print()

subject = "Math"
scores = {}

for student, subjects in gradebook.items():
    scores[student] = subjects[subject]

student_names = list(scores.keys())
highest = student_names[0]
lowest = student_names[0]

for name in scores:
    if scores[name] > scores[highest]:
        highest = name
    if scores[name] < scores[lowest]:
        lowest = name

print("Highest grade in", subject, ":", scores[highest], "by", highest)
print("Lowest grade in", subject, ":", scores[lowest], "by", lowest)
print()

sorted_names = []

while len(averages) > 0:
    names = list(averages.keys())
    top = names[0]
    for name in names:
        if averages[name] > averages[top]:
            top = name
    sorted_names.append(top)
    del averages[top]

print("Students sorted by average grade:")
for name in sorted_names:
    print(name)

#Part H

products = {
    "pen": {"price": 20, "quantity": 600},
    "book": {"price": 500, "quantity": 30}
}
cart={}

def add_to_cart(item, qty):
    if item in products and products[item]["quantity"] >= qty:
        cart[item] = cart.get(item, 0) + qty
        products[item]["quantity"]-=qty

otal = sum(products[item]["price"] * cart[item] for item in cart)

discount = 0.10  
tax = 0.08       
total_after_discount = total * (1 - discount)
final_price = total_after_discount * (1 + tax)
print(f"Total:{final_price}")



