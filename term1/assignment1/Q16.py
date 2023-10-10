'''
Program to calculate the coding score for job applicants
'''


competency_name = ["Python", "Ruby", "Bash", "Git", "HTML", "TDD", "CSS", "JavaScript"]  #List to store each competency name
competency_score = [1, 2, 4, 8, 16, 32, 64, 128] #List to store each competancy score in the corresponding element to match the name list
applicant_skills = [] #List to store Y or N according to the user's answers in the corresponding element to match the name list

user_coding_score = 0 # variable to keep track of user's score
max_coding_score = 0 # variable to add up all scores to give the maximum possible score
additional_score = 0 # variable to add up scores which the applicant has answered "no" to

# Function to add the applicant's "Y" answer where applicable
# In the case of any other answer, or non-answer, this function will revert to the default value of "N"
def addto_applicant_skills(answer = "N"):
    applicant_skills.append(answer)


# Ask user if they have the compentencies
print("ACME would like to know which skills you have\n")
print("Answer Yes or No to indicate your skills\n")


# While loop asks user to enter yes or no for each language
# The loop keeps track of the score and also adds, Y or N in the appropriate position
# in the applicant_skills list
for i in range(len(competency_name)):
    answer = input(f"{competency_name[i]} - Enter Y or N: ")    
    if (answer.upper() == "Y"):
        user_coding_score += competency_score[i]
        addto_applicant_skills(answer.upper)
    else:
        addto_applicant_skills()
      

# Adds up the maximum possible score - this function runs each time in case the corporation decides to change the scores
for i in range(len(competency_score)):
    max_coding_score += competency_score[i]

print(f"\nYour coding score is calculated as: {user_coding_score} points.\n")


# If statement to check the user's score against the maximum score
# If the user's score is less than the maximum, a for loop is run to find the missing skills and list them
# If the user score is not lower than the maximum score a congratulations message is printed instead of the additional skills information
if (user_coding_score < max_coding_score):
    print("Suggestions for additional skills which would improve your score:\n\n")
    print(f"{'SKILL':10} : {'SCORE':>7}")
    print("----------------------")
    for i in range (len(applicant_skills)): 
        if (applicant_skills[i] == "N"):
            print(f"{competency_name[i]:10} : {competency_score[i]:>7}")
            additional_score += competency_score[i]
    print("----------------------")
    print(f"{'TOTAL':10} : {additional_score:>7}")
    print("\n")
    print(f"By learning these additional skills, your score would improve by {additional_score} points.")
else:
    print(f"Congratulations, you have all the skills necessary for ACME Corporation!")
