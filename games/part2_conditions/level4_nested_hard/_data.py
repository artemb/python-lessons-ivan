from random import choice, randint

choices = ['top', 'bottom']

correct1 = choice(choices)
correct2 = choice(choices)

code1 = 44
code2 = 88

conf = {
    "map": [
        "XXXXXXXXXXXXX",
        "X   XXXX L  X",
        "X   L F  X  X",
        "X   XXXX L  X",
        "XP FXXXXXXXVX",
        "X   XXXX  L X",
        "X   L F  XX X",
        "X   XXXX  L X",
        "XXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 9. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": correct1,
            "message": [
                f"I know the key to the {correct1} lock. It's {code1}.",
                f"I don't know the code to the other lock.",
                f"Good luck! Bye!   (the ask() function returned '{correct1}')"
            ]
        },
        {
            "data": correct2,
            "message": [
                f"I know the key to the {correct2} lock. It's {code2}.",
                f"I don't know the code to the other lock.",
                f"Good luck! Bye!   (the ask() function returned '{correct2}')"
            ]
        },
    ],
    "locks": [
        {
            "position": [4, 2],
            "code": code1 if correct1 == 'top' else randint(1, 99)
        },
        {
            "position": [4, 6],
            "code": code1 if correct1 == 'bottom' else randint(1, 99)
        },
        {
            "position": [9, 1],
            "code": code2 if correct2 == 'top' else randint(1, 99)
        },
        {
            "position": [9, 3],
            "code": code2 if correct2 == 'bottom' else randint(1, 99)
        },
        {
            "position": [10, 5],
            "code": code2 if correct2 == 'top' else randint(1, 99)
        },
        {
            "position": [10, 7],
            "code": code2 if correct2 == 'bottom' else randint(1, 99)
        }
    ]
}
