from agents import Agent, Runner,function_tool, RunContextWrapper
import asyncio
from connection import config
from dataclasses import dataclass

@dataclass
class user_info:
    name:str
    uid:int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[user_info])-> str:
    return f"user {wrapper.context.name} is 35 Years old."

async def main():
    user = user_info(name= "sehrish", uid=102)

    agent = Agent [user_info](
        name="Assitant",
        instructions="use the fetch_user_age tool and always only say exactly  what the tool returns. ",
        tools=[fetch_user_age]
    )
    result = await Runner.run(
        starting_agent=agent,
        input="what is the age of the user? ",
        context=user,
        run_config=config

    )
    print(result.final_output)

if __name__ == "__main__":
        asyncio.run(main())