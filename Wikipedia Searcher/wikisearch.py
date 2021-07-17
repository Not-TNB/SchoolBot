from discord.ext import commands
from decouple import config
import random as r
import wikipedia
import discord

client = commands.Bot(command_prefix="w?")

def unsure(topic):
  try: p = wikipedia.page(topic)
  except wikipedia.DisambiguationError as error: topic = error.options[0]
  return topic

def isint(s):
  try: 
    int(s); return True
  except ValueError: return False

@client.event
async def on_ready(): 
  await client.change_presence(
    status = discord.Status.online,
    activity = discord.Activity(type=discord.ActivityType.watching, name="FreeCodeCamp Tutorials")
  )
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user: return
  await client.process_commands(msg)

@client.command() #Ping (Latency)
async def ping(ctx): await ctx.send(f"🏓Pong!\nLatency: {round(client.latency * 1000)}ms")

@client.command() #Search Article
async def search(ctx, topic, sentences=2):
  embed = discord.Embed(title = "Results for: " + unsure(topic), color = 0x62f980)
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  if len(wikipedia.summary(unsure(topic), sentences=sentences)) >= 2000: embed.description = "Sorry, your request was too long, try shotening your sentence argument!"
  else:  embed.description = wikipedia.summary(unsure(topic), sentences=sentences)
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")

@client.command() #Random Article
async def random(ctx, sentences=2):
  topic = unsure(wikipedia.random())
  embed = discord.Embed(title = "Random Article: \"" + topic + "\"", color = 0x62f980)
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  embed.description = wikipedia.summary(topic, sentences=sentences)
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")

@client.command() #Set Language
async def setlang(ctx, lang=""):
  embed = discord.Embed(title = "Set Language", color = 0x62f980)
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  if lang not in wikipedia.languages().keys():
    embed.description = "Go to https://en.wikipedia.org/wiki/List_of_Wikipedias to see a list of language prefixes"
  else:
    wikipedia.set_lang(lang)
    embed.description = "Language set to: " + wikipedia.languages()[lang]
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")
    
@client.command() #Donate Link
async def donate(ctx):
  embed = discord.Embed(
    title = "Donation Landing Page", 
    description = "Sent " + str(ctx.message.author) + " to the Wikimedia Donation Landing Page",
    color = 0x62f980
  )
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  wikipedia.donate()
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")

@client.command()
async def rps(ctx, choice=""):
  player = choice.lower()
  embed = discord.Embed(title = "Rock Paper Scissors", color = 0x62f980)
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  if player not in ["rock", "paper", "scissors"]: embed.description = "You must put rock, paper or scissors as your input"
  else:
    com = r.choice(["rock", "paper", "scissors"])
    if player == com: result = "Its a draw!"
    elif (player=="rock" and com=="scissors") or (player=="paper" and com=="rock") or (player=="scissors" and com=="paper"): result = "You win!"
    else: result = "You lost!"
    embed.description = ("You chose: " + player.upper() + "\nWikipedia Searcher chose: " + com.upper() + "\nResult: " + result)
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")

@client.command()
async def dice(ctx, sides="6"):
  embed = discord.Embed(title = "Dice Roller", color = 0x62f980)
  embed.set_footer(text="Wikipedia Searcher")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRQPA8Qi7lg9kj1shVj4E4uhH6lblZKa03WOSf0Hqm_XCuQyrd3-wROXjx4qG6bol4kfA&usqp=CAU")
  if not isint(sides): embed.description = "You need to give me an integer as your input"
  else:
    result = r.randint(1, int(sides))
    embed.description = "Your dice of " + sides + " side(s) has rolled a " + str(result) + "!"
  await ctx.send(embed = embed)
  await ctx.message.add_reaction("👍")

#EASTER EGGS
@client.command() #Rickroll
async def rickroll(ctx): 
  await ctx.send(file=discord.File(r"C:\Users\trist\Desktop\Code\Python 3.x\Wikipedia Searcher\say_goodbye.jpg"))
  await ctx.message.add_reaction("👍")
@client.command() #Twerking Amogus
async def sussy_baka(ctx): 
  await ctx.send(file=discord.File(r"C:\Users\trist\Desktop\Code\Python 3.x\Wikipedia Searcher\amogus.gif"))
  await ctx.message.add_reaction("👍")
@client.command() #Return to Monke
async def reject_humanity(ctx): 
  await ctx.send(file=discord.File(r"C:\Users\trist\Desktop\Code\Python 3.x\Wikipedia Searcher\return_to_monke.jpg"))
  await ctx.message.add_reaction("👍")
@client.command() #Saddam Hussein Hiding Place
async def hiding_place(ctx): 
  await ctx.send(file=discord.File(r"C:\Users\trist\Desktop\Code\Python 3.x\Wikipedia Searcher\hiding_place.png"))
  await ctx.message.add_reaction("👍")
client.run(config("WIKI_SEARCH_TOKEN"))