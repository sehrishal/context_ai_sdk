from agents import Agent, Runner
from connection import config
import asyncio

# instructions of llm context de raha hay agent ko
agent = Agent(
    name="politeAssistant",
    instructions="user ka name sehrish hai. Hamesha polite raho our har jawab mein 'sehrish'keh kar bulao."
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="who is the founder of pakistan?",
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

