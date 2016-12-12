import discord
import asyncio
client = discord.Client() #Defind 'client' this is what you'll use to have a chat with Discord!
token = 'MjU3NTk4MDQ4MzQxOTgzMjM2.Cy9CYw.BU4NcbBb3Er3amOBZuPZk4iOmZ8'

print("Booting...")


@client.event
async def on_ready(): #Anything below is run when the bot logs into Discord's servers
    print("Logged into Discord - Bot is ready!")
    await client.change_presence(game=discord.Game(name="FlareFM"))


@client.event
async def on_message(message): #This is fired everytime a new message is sent either via PM or a server the bot is in. #message.content is a string of what the message is.
    if message.content.startswith("!manky"): #Check if the message begins with '!hello'
        await client.send_message(message.channel, ":wave: Hello there!") #Send a message to the channel the '!hello' message came from.

@client.event
async def on_message(message):
    if message.content.startswith("!helptest"):
        print("HELP COMMAND EXECUTED")
        await client.send_message(message.channel, "Available Commands: `!hello`, `helptest`, `shutdown`")

@client.event
async def on_message(message):
    if message.content.startswith("!shutdown"):
        print("Shutting down on request of Discord user. Shutdown initiated at  <TIMEHERE>")
        await client.logout()
        await client.send_message(message.channel, ":wave: Goodbye!")



client.run(token)
