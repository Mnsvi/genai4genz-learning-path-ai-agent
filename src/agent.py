"""
Gen-Z Learning Path AI Agent
This agent analyzes user goals and constraints,
then autonomously plans a personalized learning path.
"""

def get_user_profile():
    """Collect user goals and constraints"""
    goal = input("🎯 What do you want to learn? ")
    level = input("📘 Your level (beginner/intermediate): ")
    time_per_day = int(input("⏱ Minutes per day you can study: "))
    return goal, level.lower(), time_per_day


def decide_learning_strategy(level, time_per_day):
    """
    Agent decision logic:
    Decides learning intensity and depth autonomously
    """
    if time_per_day < 30:
        intensity = "light"
    else:
        intensity = "regular"

    if level == "beginner":
        depth = "foundational"
    else:
        depth = "applied"

    return intensity, depth


def plan_learning_path(goal, intensity, depth):
    """
    Agent planning step:
    Creates a multi-step roadmap
    """
    plan = []

    if depth == "foundational":
        plan.append(f"Understand the basics of {goal}")
        plan.append(f"Learn core concepts and terminology in {goal}")
    else:
        plan.append(f"Review core concepts of {goal}")
        plan.append(f"Build small projects using {goal}")

    if intensity == "light":
        plan.append("Follow 15–25 minute daily micro-learning sessions")
    else:
        plan.append("Follow 45–60 minute structured daily sessions")

    plan.append("Review progress weekly and adjust learning pace")

    return plan


def act(plan):
    """
    Agent action:
    Executes by presenting the finalized learning plan
    """
    print("\n📚 Your Personalized Learning Path:\n")
    for step_number, step in enumerate(plan, start=1):
        print(f"{step_number}. {step}")


def main():
    print("🤖 Gen-Z Learning Path AI Agent\n")

    goal, level, time_per_day = get_user_profile()

    intensity, depth = decide_learning_strategy(level, time_per_day)

    learning_plan = plan_learning_path(goal, intensity, depth)

    act(learning_plan)


if __name__ == "__main__":
    main()
