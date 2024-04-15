class player:
    def __init__(self, user_name : str, questions : list, score=0) -> None:
        self.score = score
        self.id = user_name
        print(f"\n\nWelcome {self.id}, to this quiz game!")
        self.question_list = questions
        self.question_num = 0

    def still_has_questions(self) -> bool:
        return self.question_num < len(self.question_list)
        
    def next_question(self) -> str:
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num} {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer=user_answer, correct_answer=correct_answer)
    
    def check_answer(self, user_answer:str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(" Your answer is correct!")
        else:
            print(" That is a wrong answer ")
        print(f" The correct answer is: {correct_answer}")
        print(f" Your score is {self.score}/{self.question_num} \n\n\n")
