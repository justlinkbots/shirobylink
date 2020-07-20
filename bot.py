import discord
from discord.ext import commands
import os
PREFIX = '$'
client = commands.Bot(command_prefix = PREFIX )
client.remove_command('help')

#trigeret_words = ['Shiro','Широ','shiro','широ']
#goodbay_words = ['Пока','бб','ббак','пока','ББ','bb','BB']
#spok_words = ['спок','спокойной ночи','сладких снов','Спокойной ночи','spok']

@client.event
async def on_ready():
	print ('Бот Shiro запущен! ВНИМАНИЕ! Копируя данный программный код без согласия разработчика, вы нарушаете авторские права!')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))
@client.event
async def on_command_error(ctx, error):
	pass

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description ='** :x: Ой!~ Такой команды не существует...**', colour = discord.Color.red()))
        await ctx.send(embed = discord.Embed(description ='** Напиши $help, чтобы узнать существующие команды~**', colour = discord.Color.red()))

#@client.event
#async def on_message( message ):
#	await client.process_commands(message)
#	msg = message.content.lower()
#	if msg in trigeret_words:
#		await message.channel.send(f'Да~ Ты меня звал,{author.mention}?')
#	if msg in goodbay_words:
#		await message.channel.send(f'Пока,{author.mention}~')
#	if msg in spok_words:
#		await message.channel.send(f'Спокойной ночи,{author.mention}~')

@client.command()
async def hi( ctx ):
	author = ctx.message.author
	await ctx.send( f'**Привет, {author.mention}! Рада тебя видеть! Я бот Shiro~**' )

@client.command()
async def ЗОО( ctx ):
	author = ctx.message.author
	await ctx.send( f'**Fuck youuuu!{author.mention}**' )
#clear
@client.command()
@commands.has_permissions( administrator = True )
async def clear(ctx, amount : int ):
	await ctx.channel.purge(limit = amount)

	await ctx.send(embed = discord.Embed(description=f'**:white_check_mark: Получилось!~ Удалено {amount} сообщений~**', colour = discord.Color.green()) )


#kick
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )
async def kick( ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)
	await member.kick (reason = reason)
	await ctx.send (f'**Выгнала {member.mention} за плохое поведение >:з**')
#ban
#@client.command( pass_context = True)
#@commands.has_permissions( administrator = True )

#async def ban(ctx, member: discord.Member, *, reason = None):
#	emb = discord.Embed( title = 'Бан >:(', colour = discord.Color.red() )
#	await ctx.channel.purge(limit = 1)
#	await member.ban( reason = reason )
#	emb.set_author( name = author.name_url, icon_url =author.avatar_url )	
#	emb.add_field( name = '_____', value = 'Выгнала {}'.format(member.mention))
#	await ctx.send( embed = emb)

#mute
@client.command()
@commands.has_permissions( administrator = True )
async def mute(ctx, member: discord.Member):
	await ctx.channel.purge(limit=1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Шизоид 🐒')
	await member.add_roles( mute_role )
	await ctx.send(embed = discord.Embed(description=f'**:white_check_mark: {member.mention} увезли в дурку... Жаль~ **', colour = discord.Color.green()) )

#autorole
@client.event
async def on_member_join(member):
	channel = client.get_channel(732317365898838137)
	role = discord.utils.get(member.guild.roles, id = 732331509910077521)
	await member.add_roles( role )

#help
@client.command()
async def help(ctx):
	emb = discord.Embed( title = 'Команды бота', description ='Функционал будет расширяться! (Наверное...)' , colour = discord.Color.blue() )
	emb.set_footer(text = 'Created by 𝓙𝓾𝓼𝓽 𝓛𝓲𝓷𝓴 ♥#3337 ©')
	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.add_field( name = '{}hi'.format(PREFIX), value = '• Поздороваться с ботом :3 • ', inline=False)
	emb.add_field( name = '{}clear'.format(PREFIX), value = '• Очистка чата (Только для администраторов) •', inline=False)
	emb.add_field( name = '{}kick'.format(PREFIX), value = '• Кикнуть >:( (Только для администраторов) •', inline=False)
	emb.add_field( name = '{}mute'.format(PREFIX), value = '• Отправить в дурку ебать (Только для администраторов) •', inline=False)
	await ctx.send( embed = emb)
@clear.error
async def perm_error(ctx,error):
    if isinstance (error, commands.MissingRequiredArgument):
    	await ctx.send(embed = discord.Embed(description='**:x: Ой!~ Ты забыл указать колличество сообщений~**', colour = discord.Color.red() ))
    if isinstance (error, commands.MissingPermissions):
    	await ctx.send(embed = discord.Embed(description='**:x: Ой!~ Только админы могут это делать! Извини~**', colour = discord.Color.red() ))

@kick.error
async def kick_error(ctx,error):
	if isinstance (error, commands.MissingPermissions):
		await ctx.send(embed = discord.Embed(description='**:x: Ой!~ Только админы могут это делать! Извини~**', colour = discord.Color.red() ))

@mute.error
async def mute_error(ctx,error):
	if isinstance (error, commands.MissingPermissions):
		await ctx.send(embed = discord.Embed(description='**:x: Ой!~ Только админы могут это делать! Извини~**', colour = discord.Color.red() ))
#@ctx.error
#@ctx.error
#async def ctx_error(ctx,error):
	#if isinstance (error, commands.CommandNotFound):
	#await ctx.send(embed = discord.Embed(description=f':negative_squared_cross_mark: Ой!~ Такой команды не существует!~ Напиши $help, чтобы узнать доступные команды~ ') )	 
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
