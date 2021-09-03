# "_" = white, "B" = blue, "R" = red
# jeder der möchte kann das programm noch ausbauen

colors = {
    "B": "cornflowerblue",
    "R": "red",
    "G": "green",
    "_": "white"
}

pixelart = [["_","_","_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_","_","_"],
            ["_","_","_","R","_","_","R","_","_","_"],
            ["_","_","_","R","_","_","R","_","_","_"],
            ["_","_","_","R","_","_","R","_","_","_"],
            ["_","_","_","_","_","_","_","_","_","_"],
            ["_","B","_","_","_","_","_","_","B","_"],
            ["_","B","_","_","_","_","_","_","B","_"],
            ["_","_","B","B","B","B","B","B","_","_"],
            ["_","_","_","_","_","_","_","_","_","_"]
            ]

counter = 0
LE = 10

for i in range(len(pixelart)):
    for j in range(len(pixelart[i])):
        counter += 1
        print(f'RECHTECK("r{counter}")')
        print(f"r{counter}.verschiebeNach({j*LE}, {i*LE})")
        print(f"r{counter}.setzeHoehe({LE})\nr{counter}.setzeBreite({LE})")
        
        if pixelart[i][j] in colors:
            print(f'r{counter}.fuellen("{colors[pixelart[i][j]]}")')
        else:
            print(f'r{counter}.fuellen("black")')
