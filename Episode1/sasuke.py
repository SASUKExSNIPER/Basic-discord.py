import discord
client=discord.Client()



@client.event
async def on_ready():
	global role_list
	print('Logged in as: '+client.user.name)
	print('Bot ID: '+client.user.id)
	await client.change_presence(game=discord.Game(name='sasuke.py')) 
	print('------\n')
	


client.run('TOKEN') 
