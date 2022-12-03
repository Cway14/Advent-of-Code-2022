f = open("./scores.txt", "r")

# A = Rock
# B = Paper
# C = Scissors
#
# X = lose
# Y = draw
# Z = win
#
A = 0
B = 1
C = 2

X_score = 1
Y_score = 2
Z_score = 3

elf_moves = {"A": 0, "B": B, "C": C}
scores = {"X": X_score, "Y": Y_score, "Z": Z_score}

loss_score = 0
tie_score = 3
win_score = 6
win_scores = {"X": loss_score, "Y": tie_score, "Z": win_score}
shape_scores = {"Rock": 1, "Paper": 2, "Scissors": 3}

score = 0
total = 0
for round in f:
    elf_move = round[0]
    should_win = round[2]
    
    score += win_scores[should_win]

    if elf_move == "A":
        if should_win == "X":
            my_move = "Scissors"
        elif should_win == "Y":
            my_move = "Rock"
        elif should_win == "Z":
            my_move = "Paper"
    elif elf_move == "B":
        if should_win == "X":
            my_move = "Rock"
        elif should_win == "Y":
            my_move = "Paper"
        elif should_win == "Z":
            my_move = "Scissors"
    elif elf_move == "C":
        if should_win == "X":
            my_move = "Paper"
        elif should_win == "Y":
            my_move = "Scissors"
        elif should_win == "Z":
            my_move = "Rock"

    score += shape_scores[my_move]
    total += score
    score = 0
    

print(total)