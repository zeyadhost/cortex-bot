import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import logging
log = logging.getLogger(__name__)

from openrouter import OpenRouter
    
load_dotenv()

client = OpenRouter(
    api_key=os.environ["HCAI_API_KEY"],
    server_url="https://ai.hackclub.com/proxy/v1",
)

class Ask(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @discord.slash_command(name="ask", description="Ask a question to the AI")
    async def ask(
        self,
        ctx: discord.ApplicationContext,
        question: discord.Option(str, "What do you want to ask?"), # pyright: ignore[reportInvalidTypeForm]
        model: discord.Option(
            str,
            "Which model to use",
        autocompletes=[
            "anthropic/claude-haiku-5.5",
            "anthropic/claude-sonnet-5.5",
            "anthropic/claude-opus-5.5",
            "openai/gpt-6-astra",
            "openai/gpt-6.1-sol",
            "openai/gpt-6-sol",
            "openai/gpt-6-luna",
            "openai/gpt-5.6-terra",
            "mistralai/mistral-large-4-0",
            "stepfun/step-5-preview",
            "deepseek/deepseek-v4.1-flash",
            "qwen/qwen3.8-max-0902",
            "qwen/qwen3.8-max-prime",
            "x-ai/grok-4.7",
            "z-ai/glm-5.3-prime",
            "z-ai/glm-5.3-flashx",
            "xiaomi/mimo-v2.6-pro",
            "xiaomi/mimo-v2.6-flash",
            "meta/muse-wonder",
            "meta/muse-spark-1.3-contributor",
            "inception/mercury-2.5",
            "inclusionai/ling-3.1-flash",
            "upstage/solar-mini4",
            "cohere/command-a-plus",
            "sakana/fugu-max",
            "sakana/fugu-ultra-v2",
            "nex-agi/nex-n2.5-pro",
        ]
        ) = "openai/gpt-6-luna" # pyright: ignore[reportInvalidTypeForm]
    ) -> None:
        await ctx.defer()
        response = client.chat.send(
            model=model,
            messages=[
                {"role": "user", "content": question}
            ],
            stream=False,
        )

        await ctx.followup.send(response.choices[0].message.content)

def setup(bot: discord.Bot) -> None:
    bot.add_cog(Ask(bot))