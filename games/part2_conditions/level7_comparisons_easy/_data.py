from random import choice, randint

code = randint(1, 10)

conf = {
    "map": [
        "XXXXXXXXXXX",
        "X      L  X",
        "X      X VX",
        "X      L  X",
        "X      XXXX",
        "X         X",
        "XXXXXXXX  X",
        "XP     F  X",
        "XXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": code,
            "message": [
                f"If the code is between 1 and 5, it opens the top lock.",
                f"If the code is greater than 5, it opens the bottom lock.",
                f"(ask() function returns '{code}')"
            ]
        },
    ],
    "locks": [
        {
            "position": [7, 1],
            "code": code if code <= 5 else randint(99, 999)
        },
        {
            "position": [7, 3],
            "code": code if code > 5 else randint(99, 999)
        },
    ]
}
