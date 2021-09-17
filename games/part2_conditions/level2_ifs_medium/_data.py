from random import choice, randint

choices = ['top', 'bottom']

correct = choice(choices)

conf = {
    "map": [
        "XXXXXXXXXXX",
        "X     X   X",
        "X     L   X",
        "XP F  X  VX",
        "X     L   X",
        "X     X   X",
        "XXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 6. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": correct,
            "message": [
                f"I know the key to the {correct} lock. It's 7.",
                f"I don't know the code to the other lock.",
                f"Good luck! Bye!   (the ask() function returned '{correct}')"
            ]
        }
    ],
    "locks": [
        {
            "position": [6, 2],
            "label": "This is the top lock. Try and open it with open_lock() function",
            "code": 7 if correct == 'top' else randint(1, 99)
        },
        {
            "position": [6, 4],
            "label": "This is the bottom lock. Try and open it with open_lock() function",
            "code": 7 if correct == 'bottom' else randint(1, 99)
        }
    ]
}

