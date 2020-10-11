import discord
client=discord.Client()



@client.event
async def on_ready()
	print('Logged in as: '+client.user.name)
	print('iD: '+client.user.id)
	await client.change_presence(game=discord.Game(name='sasuke.py')) 
	print('------')
	


client.run('TOKEN') 
