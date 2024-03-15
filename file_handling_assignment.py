with open("my_file.txt", "w") as f: 
    f.write("kndkjf nkjdfn k \n8665216320549784121 \nkjsdbf545fjbsuhdbn54\n")

with open("my_file.txt", "r") as f: 
    print(f.read())

with open("my_file.txt", "a") as f:
    f.write("fjsvj hsvhj bsc \nhcb hsdvc hvsb \nhzvc hgvchg \nvvc vzxc vzxcv nbzxc vzc \n")

 
try:
    f = open("my.txt")
except (FileNotFoundError,PermissionError):
    print("error reading file")


 