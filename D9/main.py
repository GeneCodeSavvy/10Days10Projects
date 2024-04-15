import data
import question_model
import quiz_brain

question_bank : list = []
for i in data.question_data:
    text = i["text"]
    answer = i["answer"]
    question = question_model.question(q_text=text, q_answer=answer)
    question_bank.append(question)

harsh = quiz_brain.player(user_name="GeneCodeSavvy", questions=question_bank)
while harsh.still_has_questions():
    harsh.next_question()
print("You have completed the QUIZ")
print(f"Your final score is {harsh.score}/{harsh.question_num}")
    

#print(question_bank)