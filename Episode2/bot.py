import discord
client=discord.Client()


@client
async def name(self, ctx):
    embed = Embed(title="Title", color=ctx.author.color, description="SASUKE")
    embed.add_field("field 1", "value")
    embed.add_image(url="LINK URL ON HERE")
    embed.add_footer(text="TEXT FOOTER ON HERE ")
    await ctx.send(embed=embed)
 



  idchannel = client.get_channel('id channel')  
  await client.join_voice_channel(idchannel)
  print('Bot joined the channel')
