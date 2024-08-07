import json
from difflib import get_close_matches

def load_databank(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_databank(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_matches(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None

def get_answer_for_question(question: str, databank: dict) -> str | None:
    for q in databank["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    databank = load_databank('c:\\project\\AI responses\\databank.json')

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
                databank["questions"].append({"question": user_input, "answer": new_answer})
                save_databank('c:\\project\\AI responses\\databank.json', databank)
                print('Bot: Thank you')

if __name__ == '__main__':
    chat_bot()
