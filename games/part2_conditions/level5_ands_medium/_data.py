from random import choice, randint

first_code = 76
second_code = 34

correct = choice((first_code, second_code))
is_truth = choice((True, False))


friend1 = 'truth' if is_truth else 'lies'
if (is_truth and first_code == correct) or (not is_truth and second_code == correct):
    friend2 = 'first'
else:
    friend2 = 'second'

conf = {
    "map": [
        "XXXXXXXXXXXXXXX",
        "X           X X",
        "XP  F  F  F LVX",
        "X           X X",
        "XXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 10. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": None,
            "message": [
                "There are 2 codes written on the lock. You need to pick the right one",
                "People in this room will help you.",
                "(ask() function returns nothing)"
            ]
        },
        {
            "data": friend1,
            "message": [
                "The next person can sometimes tell truth, other times - lies",
                f"Today they always tell {friend1}",
                f"(ask() function returns '{friend1}')"
            ]
        },
        {
            "data": friend2,
            "message": [
                f"You need to use the {friend2} code.",
                f"(the ask() function returned '{friend2}')"
            ]
        },
    ],
    "locks": [
        {
            "label": [
                "The label on the lock reads:",
                "The first code is 76. The second code is 34",
                "You only get one try. Use the open_lock() function."

            ],
            "message_wrong_code": "This code is wrong",
            "code": correct,
            "auto_destroys": True
        },
    ]
}
