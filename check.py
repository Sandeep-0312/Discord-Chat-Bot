import json
from difflib import get_close_matches

def load_databank(file_path: str) -> dict:
    print(f"Loading databank from: {file_path}")
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(f"Databank loaded: {data}")
    return data

def save_databank(file_path: str, data: dict):
    print(f"Saving databank to: {file_path}")
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Databank saved: {data}")

def find_best_matches(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.9)
    return matches[0] if matches else None

def get_answer_for_question(question: str, databank: dict) -> str | None:
    for q in databank["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    file_path = 'c:\\project\\AI responses\\databank.json'
    databank = load_databank(file_path)

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match = find_best_matches(user_input, [q['question'] for q in databank["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, databank)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                print(f"Adding new question and answer to databank: {user_input} -> {new_answer}")
                databank["questions"].append({"question": user_input, "answer": new_answer})
                save_databank(file_path, databank)
                print('Bot: Thank you')

if __name__ == '__main__':
    chat_bot()
