
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Load environment variables
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing in .env")

# Get city from user
city = input("Which city? ").strip()

if not city:
    raise ValueError("Please enter a valid city name.")

# Create Travel Planner Agent
planner = Agent(
    role="Travel Planner",
    goal=(
        "Recommend exactly 3 interesting tourist places "
        "in the city requested by the user."
    ),
    backstory=(
        "You are an experienced travel planner who helps "
        "first-time visitors discover popular attractions. "
        "You provide short, practical recommendations "
        "with useful visiting tips."
    ),
    verbose=True,
    llm=os.getenv("MODEL", "openai/gpt-4o-mini")
)

# Create Task
task = Task(
    description=(
        "Suggest exactly 3 places to visit in {city}. "
        "For each place, provide its name, a short "
        "description, and one useful visiting tip. "
        "Do not suggest more than 3 places."
    ),
    expected_output=(
        "A numbered list containing exactly 3 places. "
        "Format: Place Name - short description - visiting tip."
    ),
    agent=planner
)

# Create Crew
crew = Crew(
    agents=[planner],
    tasks=[task],
    verbose=True
)

# Execute Crew
result = crew.kickoff(inputs={"city": city})

print("\n===== TRAVEL PLAN =====\n")
print(result)
