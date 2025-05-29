import os
import asyncio
import disnake

from context.summary_collector import ai_summary
from context.text_collector import ai_context
from disnake.ext import commands
from dotenv import load_dotenv

from ai import ai_answer


load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())


@bot.event
async def on_ready() -> None:
    """
    Printing in the console that the bot is ready
    :return: None
    """
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(ctx) -> None:
    """
    All the logic when a message is sent on the discord server
    :param ctx:
    :return: None
    """

    if ctx.channel.id == int(os.environ.get("START_CHANNEL_ID")):
        await start_message(ctx)
        return

    if ctx.channel.type != disnake.ChannelType.private:
        return

    if not ctx.content.startswith(bot.command_prefix):
        response = await ai_answer(ctx.content or "")
        response = dict(response).get('answer')
        
        await send_pv_message(ctx, response)
        return

    await bot.process_commands(ctx)


@bot.command(name="start")
async def start(ctx) -> None:
    """
    Sends the start message to the user
    :param ctx:
    :return: None
    """
    await start_message(ctx)


@bot.command(name="context")
async def context(ctx) -> None:
    """
    Sends to the user all the context files names
    :param ctx:
    :return: None
    """
    await send_pv_message(ctx, "\n ".join(list(ai_context.keys())))


@bot.command(name="sum")
async def file_sum(ctx, *, file_name: str) -> None:
    """
    Sends to the user the summary of the given file
    :param ctx:
    :param file_name: string representing the name of the context file
    :return: None
    """
    response = await sum_ai_response(file_name)
    await send_pv_message(ctx.message, response)


async def start_message(ctx) -> None:
    """
    Sends the start message privately to the user
    :param ctx:
    :return: None
    """
    content: str = """
        **__Welcome to CoSup Gaming AI__**
    
        If you need help use the command **/start**
    
        **__How does it work:__**
    
            **/context** to get all context files that are supported
            **/sum file_name** to get the summary of the file
    
            **__To ask a question about a certain file use this syntax:__**
    
                ** question**
    
                **__example:__**
                    handbook When will I get paid ?
    """
    await send_pv_message(ctx, content)


async def send_pv_message(ctx, message_content: str) -> None:
    """
    Sends message_content privately to the user
    :param ctx:
    :param message_content: string containing the message that will be sent to the user
    :return: None
    """
    if os.environ.get("IN_DEV"):
        message_content = """# BOT IN TESTING PROCESS  DON'T USE THE BOT
        """ + message_content

    await ctx.author.send(message_content)


async def sum_ai_response(user_context: str) -> str:
    """
    Getting the summary of the given file
    :param user_context: string representing the name of the context file
    :return: string containing the summary of the given file
    """
    return ai_summary.get(user_context.lower()) or "Bad context file name"


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
