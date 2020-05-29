"""
Ben: [
        (
            start=Friday 8:00pm,
            end=Friday 11:00pm
        ),
        (
            start=Saturday 8:00pm,
            end=Saturday 11:00pm
        ),
        (
            start=Sunday 8:00pm,
            end=Sunday 11:00pm
        ),
    ]

Shan: [
    (
        start=Saturday 6:00pm,
        end=Saturday 7:30pm
    )
]

Bob: [
    (
        start=Sunday 9:00pm,
        end=Sunday 10:45pm
    )
]


POSSIBLE APPROACHES:
(assuming we have different ranges)
1. sort people by the number of available minutes they have (how picky people are), creates a list of people P
2. Pick the most picky person (least available minutes), call them P_a
3. go through the rest of the sorted list (from most picky to least picky), checking to see if any overlap exists between
"""

"""
Morning: 9:00am -- 12:00pm
Afternoon: 2:00pm -- 5:00pm
Evening: 7:00pm -- 10:00pm

Everyone picks TWO periods
Ben: ["Sat Evening", "Sun Afternoon"]
Shan: ["Fri Evening", "Sun Evening"]
Bob: ["Sat Evening", "Sun Morning"]
Alice: ["Friday Morning", "Sun Evening"]

# initial thoughts:
# TODO: WHAT AM I GOING TO DO ABOUT PREFERENCE???
there are 8 different periods from which to choose
some periods are going to be more popular than others

1. Match everyone's first preference
2. Any leftovers, match according to second preference
3. match randomly
Consideration: minimize the number of leftovers between steps

Algorithm:
1. Go through everyone's first period preferences, count them up, sort the periods by count
    e.g. ["Sunday Morning": 2, "Saturday Morning": 5, "Friday Night": 8, "Saturday Night": 21, ...]
2. Find all the people with the least common preference (Sunday morning in the above example), and pair them up
    TODO: pair them up using INTERESTS???
    at first this will be random
    TODO: what about gender???
3. Go through the rest of the preferences, pairing up people with those preferences
"""