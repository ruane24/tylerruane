import random


def deal():
    """
    This function should perform the initial card deal for both the dealer and the player.  It should give
    both players two random cards and return the sum of those two cards

    Parameters:
        None
    Return:
        The sum of the cards after the deal
    """
    ##Your code here##
    ##identify variables for cards for dealer and player##
    random1 = random.randint (1,11)
    random2 = random.randint (1,11)
    random3 = random.randint (1,11)
    random4 = random.randint (1,11)
    CurTotal = random1 + random2
    DealerCurTotal = random3 + random4
    ##Let player know the totals of both them and the dealer##
    print("You have: " + str(CurTotal))
    print("Dealer has: " + str(DealerCurTotal))
    pass


def hit(curTotal):
    """
    This function should be used to give the player and dealer a card if they want one during the game.  It will
    take the respective players current total, deal the player one additional card by choosing a random number
    between 1 and 11, and return the new total.

    Note that if the player is dealt an 11 and it would cause them to go over 21, you should add 1 to their total instead
    since in blackjack, a player can use an ace to count as 1 or 11.

    Parameters:
        curTotal: The players current total before this card is dealt
    Return:
        The total of the player's cards after this card is dealt
    """
    ##Your code here##
    ##Get a random number for the hit card##
    NewCard = random.randint(1,11)
    playerScore = NewCard + CurTotal
    ##Change 11 to a 1 if it busts them##
    if (playerScore > 21 and NewCard == 11):
        NewCard = 1
    return playerScore
    pass


def playerTurn(playerScore):
    """
    This function will run the players turn.  It should report the player's current total and ask if they would
    like to hit or stay.  If the player types "hit", it should give the player another card, report their new score,
    and prompt them to hit or stay again.  This should repeat until the player goes over 21 or chooses to "stay".
    The player's final score should be returned

    Parameters:
        playerScore: The player's current score
    Return:
        The player's score after their turn is complete
    """
    ##Your code here##
    ##Ask if they would like to hit or stay##
    HitOrStay = input("Would you like to hit or stay?")
    while (HitOrStay != "stay" or playerScore < 22):
        hit(curTotal)
        print("You have: " + str(playerScore))
        input("Would you like to hit or stay?")
    pass


def dealerTurn(dealerScore):
    """
    This function should run the dealers turn.  We will assume the dealer will always hit if their current score is
    less than or equal to 16 and will chose to stay if their current score is 17 or greater.  This function should
    return the dealers final score.

    Parameters:
        dealerScore: The dealer's current score
    Return:
        The dealer's score after their turn is complete
    """
    ##Your code here##
    dealerScore = DealerCurTotal
    ##Give dealer their strategy##
    while (dealerScore < 22 or dealerScore > 16):
        NewDealerCard = random.randint(1,11)
        dealerScore = DealerCurTotal + NewDealerCard
        if (dealerScore > 21 and NewDealerCard == 11):
            NewDealerCard = 1
        print("Dealer has: " + dealerScore)
    pass


def main():
    """
    This is your programs main function.  It should allow you to play a simplified version of blackjack against the
    dealer.  Most of this function will simply call other functions.  It should deal cards to the player and dealer, print
    the dealers total score after the deal (this is instead of just showing the player the dealers top card as
    would happen in blackjack), run the players turn, run the dealers turn if the player didn't go over 21 (the dealer
    and player should never both go over 21 on the same turn), report the player and dealers totals, and print who won or if
    there was a tie.

    Parameters:
        None
    Return:
        None
    """
    ##Your code here##
    random1 = random.randint (1,11)
    random2 = random.randint (1,11)
    random3 = random.randint (1,11)
    random4 = random.randint (1,11)
    CurTotal = random1 + random2
    DealerCurTotal = random3 + random4
    NewCard = random.randint(1,11)
    playerScore = NewCard + CurTotal
    deal()
    playerTurn(playerScore)
    pass

#Call the main function to start the program
main()
