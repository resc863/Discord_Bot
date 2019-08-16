import discord
import asyncio
import os
import sys
from discord import Member
from discord.ext import commands
from itertools import cycle

moji1=None
moji2=None
moji3=None

client = discord.Client()

token = os.environ["key"]

@client.event
async def on_ready():
    print("Logged in ") 
    print(client.user.name)
    print(client.user.id)
    print("===============")
    
    channel = client.get_channel('592296776850210816')


    message = await client.send_message(channel, "레인보우 식스를 하신다면 누르세요.")
    await client.add_reaction(message, emoji="\U0001F44F")

    message = await client.send_message(channel, "레인보우 식스 정보를 수신하시려면 누르세요.")
    await client.add_reaction(message, emoji="\U0001F600")

    message = await client.send_message(channel, "캐주얼 팟 모집을 원하시면 누르세요.")
    await client.add_reaction(message, emoji="\U0001F64F")

    message = await client.send_message(channel, "랭킹 팟 모집을 원하시면 누르세요.")
    await client.add_reaction(message, emoji="\U0001F910")
    
    await client.send_message(channel, "-----------------------------------------")

    message = await client.send_message(channel, "GTA5를 하신다면 누르세요.")
    await client.add_reaction(message, emoji="\U0001F91D")
    
@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님. '
    role = discord.utils.get(member.server.roles, id="450322259660374036")
    await client.add_roles(member, role)
    
    role = discord.utils.get(member.server.roles, id="460137279533481984")
    await client.add_roles(member, role)
    

@client.event
async def on_reaction_add(reaction, user):
        
    if reaction.emoji == "\U0001F44F":
        role = discord.utils.get(user.server.roles, id="592296285994745856")
        await client.add_roles(user, role)

    if reaction.emoji == "\U0001F600":
        role = discord.utils.get(user.server.roles, id="592295677992632320")
        await client.add_roles(user, role)

    if reaction.emoji == "\U0001F64F":
        role = discord.utils.get(user.server.roles, id="592296204633636864")
        await client.add_roles(user, role)

    if reaction.emoji == "\U0001F910":
        role = discord.utils.get(user.server.roles, id="592296204633636864")
        await client.add_roles(user, role)
    
    if reaction.emoji == "\U0001F91D":
        role = discord.utils.get(user.server.roles, id="607893687472750608")
        await client.add_roles(user, role)
        
@client.event
async def on_reaction_remove(reaction, user):

    if reaction.emoji == "\U0001F44F":
        role = discord.utils.get(user.server.roles, id="592296285994745856")
        await client.remove_roles(user, role)

    if reaction.emoji == "\U0001F600":
        role = discord.utils.get(user.server.roles, id="592295677992632320")
        await client.remove_roles(user, role)

    if reaction.emoji == "\U0001F64F":
        role = discord.utils.get(user.server.roles, id="592296204633636864")
        await client.remove_roles(user, role)

    if reaction.emoji == "\U0001F910":
        role = discord.utils.get(user.server.roles, id="592296204633636864")
        await client.remove_roles(user, role)
    
    if reaction.emoji == "\U0001F91D":
        role = discord.utils.get(user.server.roles, id="607893687472750608")
        await client.remove_roles(user, role)

client.run(token)
