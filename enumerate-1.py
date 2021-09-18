files = ["file.txt", "tom.mp4", "sis.tf", "senta.tft", "nate.yaml", "san.sis"]
for i, file in enumerate(files):
    if i%2 == 0:
     print(file)

filed = ["file.txt", "tom.mp4", "sis.tf", "senta.tft", "nate.yaml", "san.sis"]

filled = [len(files) for files in filed]

print(filled)


multi3 = [x for x in range(1, 102) if x % 3 == 0]
print(multi3)