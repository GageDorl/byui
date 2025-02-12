def main():
    print("""This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
na means you neither agree nor disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.\n""")

    score = ask_questions()
    print(f"\nYour score is {score}.\nA score below 30 may indicate problematic low self-esteem.")



def ask_questions():
    score = 0
    questions = [
        ['I feel that I am a person of worth, at least on an equal plane with others.', 'positive'],
        ['I feel that I have a number of good qualities.', 'positive'],
        ['All in all, I am inclined to feel that I am a failure.', 'negative'],
        ['I am able to do things as well as most other people.', 'positive'],
        ['I feel I do not have much to be proud of.', 'negative'],
        ['I take a positive attitude toward myself.', 'positive'],
        ['On the whole, I am satisfied with myself.', 'positive'],
        ['I wish I could have more respect for myself.', 'negative'],
        ['I certainly feel useless at times.', 'negative'],
        ['At times I think I am no good at all.', 'negative']
    ]

    for index , question in enumerate(questions):
        print(f"{index+1}: {question[0]}")
        response = input("Enter your response: ")
        if question[1] == 'positive':
            match response:
                case 'D': score += 1
                case 'd': score += 2
                case 'na': score += 3
                case 'a': score += 4
                case 'A': score += 5
        else:
            match response:
                case 'D': score += 5
                case 'd': score += 4
                case 'na': score += 3
                case 'a': score += 2
                case 'A': score += 1
        
    return score

if __name__ == "__main__":
    main()