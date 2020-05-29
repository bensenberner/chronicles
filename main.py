from enum import Enum, auto


class P(Enum):
    ALICE = auto()
    BOB = auto()
    CHARLIE = auto()
    DIANA = auto()
    EVAN = auto()


person_to_interests = {
    P.ALICE: {P.CHARLIE},
    P.BOB: {P.ALICE, P.DIANA},
    P.CHARLIE: {P.ALICE},
    P.DIANA: {P.CHARLIE},
    P.EVAN: {P.DIANA}
}


def remove_person_as_potential_interest(potential_interest: P):
    for person_with_interests in person_to_interests.keys():
        if potential_interest in person_to_interests[person_with_interests]:
            person_to_interests[person_with_interests].remove(potential_interest)


def create_matches():
    """
    Given a graph that maps people to an unordered set of people in whom they are interested, this algorithm
    will first randomly pair up people who have a mutual interest, and then pair up people in which there is one sided interest,
    and then pair up people in which there is no interest
    :return:
    """
    remaining_people = set(e for e in P)
    couples = []
    # make mutual interest
    while remaining_people:
        # need to copy the set since it could change in iteration. probably not ideal.
        for random_person_a in set(remaining_people):
            for random_person_b in person_to_interests[random_person_a]:
                if random_person_a in person_to_interests[random_person_b]:
                    # we have a match! take them off the market
                    couples.append((random_person_a, random_person_b))
                    remove_person_as_potential_interest(random_person_a)
                    remove_person_as_potential_interest(random_person_b)
                    remaining_people.remove(random_person_a)
                    remaining_people.remove(random_person_b)
                    break
        # no more two way matches
        break

    # make one sided matches
    while remaining_people:
        match_occurred = False
        for person in remaining_people:
            if person_to_interests[person]:
                match_occurred = True
                interest = person_to_interests[person].pop()
                couples.append((person, interest))
                remove_person_as_potential_interest(person)
                remove_person_as_potential_interest(interest)
                remaining_people.remove(person)
                remaining_people.remove(interest)
                break
        if not match_occurred:
            break

    # make matches that neither really wanted
    while len(remaining_people) > 1:
        couples.append(
            (remaining_people.pop(), remaining_people.pop())
        )

    if remaining_people:
        print(f"{remaining_people.pop()} was unable to be matched :(")

    return couples


if __name__ == "__main__":
    couples = create_matches()
    for couple in couples:
        print(couple)
