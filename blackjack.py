import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "S", "D", "C"]

deck = []
for rank in ranks:
    for suit in suits:
        deck.append(rank + "." + suit)


def value(hand):
    sumv = 0
    for card in hand:
        val = card.split(".")[0]
        if val == "J" or val == "Q" or val == "K":
            sumv += 10
        elif val == "A":
            sumv += 11
        else:
            sumv += int(val)
    return sumv


used = [False] * 52


def pick_card():
    while True:
        i = random.randint(0, 51)
        if not used[i]:
            used[i] = True
            return deck[i]


def play_blackjack():
    used = [False] * 52
    hand = [pick_card(), pick_card()]
    dealer = [pick_card(), pick_card()]
    while True:
        print("Dealer: " + dealer[0])
        print("Your hand: " + " ".join(hand))
        ui = input("Hit or Stick: ")
        if ui.lower() == "hit":
            hand.append(pick_card())
            playerV = value(hand)
            if playerV > 21:
                print("\nDealer: " + dealer[0])
                print("Your hand: " + " ".join(hand))
                print("You Bust!")
                return False
        if ui.lower() == "stick" or playerV == 21:
            print("\nDealer: " + dealer[0] + " " + dealer[1])
            print("Your hand: " + " ".join(hand))
            dealerV = value(dealer)
            playerV = value(hand)
            if dealerV >= playerV:
                return False
            else:
                return True
            return


money = 100
while money > 0:
    print("Money Remaining: " + str(money))
    bet = -1
    while bet < 0:
        bet_str = input("How much would you like to bet: ")
        try:
            tmp = int(bet_str)
            if tmp > 0 and tmp <= money:
                bet = tmp
            else:
                print("please input an amount you can afford brokie!")
        except:
            print("please input an integer number :(")

    if play_blackjack():
        print("Nice Win!")
        money += bet
    else:
        print("sorry you lost")
        money -= bet
    print("\n")

print("You got kicked out the casino!!")
