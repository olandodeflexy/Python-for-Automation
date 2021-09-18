def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds
    


hours, minutes, remaining_seconds =  convert_seconds(5000)
print(hours, minutes, remaining_seconds)
print("******************************************")
print("")



def attempts(n):
    x = 1
    while x < n:
        print("Attempts " + str(x))
        x += 1
    print("Done")

attempts(5)
print("******************************************")
print("")


def square(n):
    return n*n


print(square(5))
print("******************************************")
print("")


friends = ["kofi", "ama", "adjoa", "kweku"]
for friend in friends:
    print("Hi  " + friend)
    
print("******************************************")
print("")
    

values = [20, 30, 40, 50, 60]
sum = 0 
length = 0
for value in values:
    sum += value
    
print("Total sum: " + str(sum) + " Average " + str(sum/length))
print("******************************************")
print("")


