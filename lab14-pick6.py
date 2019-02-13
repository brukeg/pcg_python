"""

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times,
with the ticket cost and payoff below. A ticket contains 6 numbers, 1 to 99, and the number of matches
between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers
are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2]
and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings
(the sum of all expenses and earnings).

- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be
used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket)
which returns the number of matches between the winning numbers and the ticket.

Steps
1. Generate a list of 6 random numbers representing the winning tickets
2. Start your balance at 0
3. Loop 100,000 times, for each loop:
4. Generate a list of 6 random numbers representing the ticket
5. Subtract 2 from your balance (you bought a ticket)
6. Find how many numbers match
7. Add to your balance the winnings from your matches
8. After the loop, print the final balance

Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses.
Calculate your ROI, print it out along with your earnings and expenses.
"""

import random

# picks a winning ticket with 6 random numbers in it
winning_ticket = [random.randint(1, 99) for n in range(6)]

# generate a list of lotto ticket lists
tickets = [[random.randint(1, 99) for n in range(6)] for n in range(100000)]


def pick6(w, t):
    """
    calculates the number of matches between pick6 soultion and tickets
    and returns payout and roi
    """
    sub_balance = 0
    match_list = []
    for lists in t:
        """ checks for matches in each list by order and value """
        index = 0
        matches = 0
        for value in lists:
            if value == w[index]:
                matches += 1
                index += 1
            else:
                index += 1
        match_list.append(matches)
        sub_balance -= 2

    winnings = 0
    for i in match_list:
        """ asses the winnings based on the match_list """
        if i == 1:
            winnings += 4
        elif i == 2:
            winnings += 7
        elif i == 3:
            winnings += 100
        elif i == 4:
            winnings += 50000
        elif i == 5:
            winnings += 1000000
        elif i == 6:
            winnings += 25000000
        else:
            winnings += 0

    return sub_balance + winnings, (winnings + sub_balance)/sub_balance

# test list:
# print(pick6([1, 2, 3], [[1, 2, 3], [1, 3, 3], [0, 0, 0]]))
