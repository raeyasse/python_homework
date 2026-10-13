# Task 1, print Hello
def hello():
    return "Hello!"

#Task 2 
def greet(name):
    return f"Hello, {name}!"

#print(greet("raey"))

#Task 3
def calc(num1, num2, operation = "multiply"):
   try:
       if operation == "multiply":
            return num1 * num2
       elif operation == "divide":
            return num1 / num2 
       elif operation == "int_divide":
            return num1 // num2 
       elif operation == "add":
            return num1 + num2 
       elif operation == "subtract":
            return num1 - num2 
       elif operation == "modulo":
            return num1 % num2 
       elif operation == "power":
            return num1 ** num2
       else:
            return "Invalid Operation"
   except ZeroDivisionError:
        return "You can't divide by 0!"
   except TypeError:
        return "You can't multiply those values!"

       
#print(calc(2,5,"divide"))

#Task 4 
def data_type_conversion(value,type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except (TypeError, ValueError):
        return f"You can't convert {value} into a {type}."

# print(data_type_conversion(2,"float"))

#Task 5
def grade(*args):
    try:
        avg = sum(args) // len(args)
        if avg >= 90:
           return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."


#print(grade(100,30,"F"))

#Task 6 
def repeat(string,count):
    new_str = ""
    for i in range(count):
        new_str = new_str + string
    return new_str

#print(repeat("Hello",5))

#Task 7
def student_scores(mode,**kwargs):
    match mode:
        case "best":
            best_student = ""
            highest_score = 0
            for key, value in kwargs.items():
                if value >= highest_score:
                    highest_score = value
                    best_student = key
            return best_student
        case "mean":
            return sum(kwargs.values()) // len(kwargs.keys())

#print(student_scores("best", Tomas=78, Raey=75, Inde=92))

#Task 8
def titleize(string):
    words = string.split()
    new_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in ("a","on", "an", "the", "of", "and", "is", "in"):
            new_words.append(word.capitalize())
        else:
            new_words.append(word)
    return " ".join(new_words)

#print(titeleize("Will jack and jill fetch a pail of water?"))

#Task 9 
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result = result + char
        else:
            result = result + "_"
    return result

#print(hangman("Sikuarbeshiro", "Yebol3arada"))

#task 10
def pig_latin(sentence):
    words = sentence.split()
    pig_words = []
    vowels = ("a","e","i","o","u")
    for word in words:
        if word[0] in vowels:
            pig_words.append(word + "ay")
        elif word.startswith("qu"):
            pig_words.append(word[2:] + "quay")
        elif word.startswith("squ"):
            pig_words.append(word[3:] + "squay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1
            pig_words.append(word[i:] + word[:i] + "ay")
    return " ".join(pig_words)

#print(pig_latin("see red robin climbs the clock tower"))