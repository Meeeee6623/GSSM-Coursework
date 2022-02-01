import random


def reset_cups():
    with open('cups.txt', 'w') as f:
        for _ in range(15):
            f.write('1,2,3\n')


def load_cups(file):
    with open(file, 'r') as f:
        cups = f.readlines()
        strings = [cup.replace('\n', '').split(',') for cup in cups]
        nums = []
        for cup in strings:
            temp = []
            for num in cup:
                tmp = int(num)
                temp.append(tmp)
            nums.append(temp)
        return nums


def save_data(cup_data):
    with open('cup_save.txt', 'w') as f:
        for line in cup_data:
            f.write(str(line).replace('[', '').replace(']', '') + '\n')


def back_propagate(cup_data, move_list):
    for move in move_list[::-1]:
        if len(cup_data[move[0]]) > 1:
            cup_data[move[0]].pop(move[1])
            return


def train_auto(cup_data, rounds):
    opponent = load_cups('perfect_cups.txt')
    for i in range(rounds):
        move_list = []
        num_coins = 15
        while num_coins > 0:
            if len(cup_data[num_coins - 1]) > 1:
                cup_choice = random.randint(0, len(cup_data[num_coins - 1]) - 1)
            else:
                cup_choice = 0
            move_list.append((num_coins - 1, cup_choice))
            num_coins -= cup_data[num_coins - 1][cup_choice]
            if num_coins < 1:
                back_propagate(cup_data, move_list)
                break
            num_coins -= random.choice(opponent[num_coins - 1])
            # if num_coins == 1:
            #     back_propagate(cup_data, move_list)
            #     break
        print(f'Round {i} complete!')
    print(opponent)

    return cup_data

def train_manual(cup_data, rounds):
    for i in range(rounds):
        print(cup_data)
        move_list = []
        num_coins = 15
        while num_coins > 0:
            if len(cup_data[num_coins - 1]) > 1:
                cup_choice = random.randint(0, len(cup_data[num_coins - 1]) - 1)
            else:
                cup_choice = 0
            move_list.append((num_coins - 1, cup_choice))
            num_coins -= cup_data[num_coins - 1][cup_choice]
            if num_coins < 1:
                print("You win!")
                back_propagate(cup_data, move_list)
                break
            num_coins -= int(input(f'There are currently {num_coins} coins. How many would you like to take?\n'))
            if num_coins == 1:
                print("You win!")
                back_propagate(cup_data, move_list)
                break
            elif num_coins < 1:
                print("The cups win!")
        print(f'Round {i} complete!')
        save_data(cup_data)

    return cup_data

def play_rounds(cup_data, rounds):
    w = 0
    l = 0
    for _ in range(rounds):
        num_coins = 15
        while num_coins > 0:
            num_coins -= random.choice(cup_data[num_coins - 1])
            if num_coins <= 1: w += 1; break
            num_coins -= random.randint(1, 3)
            if num_coins <= 0: l += 1; break

    print(f'Your cups won {w} times and lost {l} times!')
    return


cup_data = load_cups('cups.txt')
print(cup_data)

# train_auto(cup_data, 100)
train_manual(cup_data, 10)

print(cup_data)
save_data(cup_data)

play_rounds(cup_data, 50)
wow

