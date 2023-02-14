import InsectClass as I


def main():
    choice = I.Insect
    print("I am looking at 10 Insects!")
    for x in range(10):
        choice.bug_type
        choice.length_of_flight
    print("The ", I.insect, "flew ", I.flight, " miles!")
