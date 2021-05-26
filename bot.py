import discord
from discord.ext import commands
import os
PREFIX = '$'
client = commands.Bot(command_prefix = PREFIX )
client.remove_command('help')

trigeret_words = ['Shiro','Широ','shiro','широ']
goodbay_words = ['Пока','бб','ббак','пока','ББ','bb','BB']
spok_words = ['спок','спокойной ночи','сладких снов','Спокойной ночи','spok']

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

@client.event
async def on_message( message ):
	await client.process_commands(message)
	msg = message.content.lower()
	if trigeret_words in msg:
		await message.channel.send(f'Да~ Ты меня звал,{author.mention}?')
	if goodbay_words in msg:
		await message.channel.send(f'Пока,{author.mention}~')
	if spok_words in msg:
		await message.channel.send(f'Спокойной ночи,{author.mention}~')

@client.command()
async def hi( ctx ):
	author = ctx.message.author
	await ctx.send( f'**Привет, {author.mention}! Рада тебя видеть! Я бот Shiro~**' )

@client.command()
async def van( ctx ):
	author = ctx.message.author
	await ctx.send( f'**Fuck youuuu!{author.mention}**' )
	await ctx.send( 'https://tenor.com/bpiu8.gif' )
@client.command()
async def gym( ctx ):
	author = ctx.message.author
	await ctx.send( f'**Come on, lets go! {author.mention}**' )
	await ctx.send( 'https://media.discordapp.net/attachments/732325941287845931/733032131877404832/tenor_2.gif' )
#clear
@client.command()
@commands.has_permissions( administrator = True )
async def clear(ctx, amount : int ):
	await ctx.channel.purge(limit = amount)
	await ctx.send(embed = discord.Embed(description=f'**:white_check_mark: Получилось!~ Удалено {amount} сообщений~**', colour = discord.Color.green()) )

#1000-7
@client.command()
async def imghoul( ctx ):
	author = ctx.message.author
	await ctx.send( f'Я........ Гуль....')
	await ctx.send( f'https://media.discordapp.net/attachments/801689989964496926/847032579701735444/tenor.gif')
	await ctx.send( f'Le... Le... Let me die...')
	await ctx.send ( f' 1000 - 7 ' )
	await ctx.send ( f' 993 - 7 ' )
	await ctx.send ( f' 986 - 7 ' )
	await ctx.send ( f' 979 - 7 ' )
	await ctx.send ( f' 972 - 7 ' )
	await ctx.send ( f' 965 - 7 ' )
	await ctx.send ( f' 958 - 7 ' )
	await ctx.send ( f' 951 - 7 ' )
	await ctx.send ( f' 944 - 7 ' )
	await ctx.send ( f' 937 - 7 ' )
	await ctx.send ( f' 930 - 7 ' )
	await ctx.send ( f' 923 - 7 ' )
	await ctx.send ( f' 916 - 7 ' )
	await ctx.send ( f' 909 - 7 ' )
	await ctx.send ( f' 902 - 7 ' )
	await ctx.send ( f' 895 - 7 ' )
	await ctx.send ( f' 888 - 7 ' )
	await ctx.send ( f' 881 - 7 ' )
	await ctx.send ( f' 874 - 7 ' )
	await ctx.send ( f' 867 - 7 ' )
	await ctx.send ( f' 860 - 7 ' )
	await ctx.send ( f' 853 - 7 ' )
	await ctx.send ( f' 846 - 7 ' )
	await ctx.send ( f' 839 - 7 ' )
	await ctx.send ( f' 832 - 7 ' )
	await ctx.send ( f' 825 - 7 ' )
	await ctx.send ( f' 818 - 7 ' )
	await ctx.send ( f' 811 - 7 ' )
	await ctx.send ( f' 804 - 7 ' )
	await ctx.send ( f' 797 - 7 ' )
	await ctx.send ( f' 790 - 7 ' )
	await ctx.send ( f' 783 - 7 ' )
	await ctx.send ( f' 776 - 7 ' )
	await ctx.send ( f' 769 - 7 ' )
	await ctx.send ( f' 762 - 7 ' )
	await ctx.send ( f' 755 - 7 ' )
	await ctx.send ( f' 748 - 7 ' )
	await ctx.send ( f' 741 - 7 ' )
	await ctx.send ( f' 734 - 7 ' )
	await ctx.send ( f' 727 - 7 ' )
	await ctx.send ( f' 720 - 7 ' )
	await ctx.send ( f' 713 - 7 ' )
	await ctx.send ( f' 706 - 7 ' )
	await ctx.send ( f' 699 - 7 ' )
	await ctx.send ( f' 692 - 7 ' )
	await ctx.send ( f' 685 - 7 ' )
	await ctx.send ( f' 678 - 7 ' )
	await ctx.send ( f' 671 - 7 ' )
	await ctx.send ( f' 664 - 7 ' )
	await ctx.send ( f' 657 - 7 ' )
	await ctx.send ( f' 650 - 7 ' )
	await ctx.send ( f' 643 - 7 ' )
	await ctx.send ( f' 636 - 7 ' )
	await ctx.send ( f' 629 - 7 ' )
	await ctx.send ( f' 622 - 7 ' )
	await ctx.send ( f' 615 - 7 ' )
	await ctx.send ( f' 608 - 7 ' )
	await ctx.send ( f' 601 - 7 ' )
	await ctx.send ( f' 594 - 7 ' )
	await ctx.send ( f' 587 - 7 ' )
	await ctx.send ( f' 580 - 7 ' )
	await ctx.send ( f' 573 - 7 ' )
	await ctx.send ( f' 566 - 7 ' )
	await ctx.send ( f' 559 - 7 ' )
	await ctx.send ( f' 552 - 7 ' )
	await ctx.send ( f' 545 - 7 ' )
	await ctx.send ( f' 538 - 7 ' )
	await ctx.send ( f' 531 - 7 ' )
	await ctx.send ( f' 524 - 7 ' )
	await ctx.send ( f' 517 - 7 ' )
	await ctx.send ( f' 510 - 7 ' )
	await ctx.send ( f' 503 - 7 ' )
	await ctx.send ( f' 496 - 7 ' )
	await ctx.send ( f' 489 - 7 ' )
	await ctx.send ( f' 482 - 7 ' )
	await ctx.send ( f' 475 - 7 ' )
	await ctx.send ( f' 468 - 7 ' )
	await ctx.send ( f' 461 - 7 ' )
	await ctx.send ( f' 454 - 7 ' )
	await ctx.send ( f' 447 - 7 ' )
	await ctx.send ( f' 440 - 7 ' )
	await ctx.send ( f' 433 - 7 ' )
	await ctx.send ( f' 426 - 7 ' )
	await ctx.send ( f' 419 - 7 ' )
	await ctx.send ( f' 412 - 7 ' )
	await ctx.send ( f' 405 - 7 ' )
	await ctx.send ( f' 398 - 7 ' )
	await ctx.send ( f' 391 - 7 ' )
	await ctx.send ( f' 384 - 7 ' )
	await ctx.send ( f' 377 - 7 ' )
	await ctx.send ( f' 370 - 7 ' )
	await ctx.send ( f' 363 - 7 ' )
	await ctx.send ( f' 356 - 7 ' )
	await ctx.send ( f' 349 - 7 ' )
	await ctx.send ( f' 342 - 7 ' )
	await ctx.send ( f' 335 - 7 ' )
	await ctx.send ( f' 328 - 7 ' )
	await ctx.send ( f' 321 - 7 ' )
	await ctx.send ( f' 314 - 7 ' )
	await ctx.send ( f' 307 - 7 ' )
	await ctx.send ( f' 300 - 7 ' )
	await ctx.send ( f' 293 - 7 ' )
	await ctx.send ( f' 286 - 7 ' )
	await ctx.send ( f' 279 - 7 ' )
	await ctx.send ( f' 272 - 7 ' )
	await ctx.send ( f' 265 - 7 ' )
	await ctx.send ( f' 258 - 7 ' )
	await ctx.send ( f' 251 - 7 ' )
	await ctx.send ( f' 244 - 7 ' )
	await ctx.send ( f' 237 - 7 ' )
	await ctx.send ( f' 230 - 7 ' )
	await ctx.send ( f' 223 - 7 ' )
	await ctx.send ( f' 216 - 7 ' )
	await ctx.send ( f' 209 - 7 ' )
	await ctx.send ( f' 202 - 7 ' )
	await ctx.send ( f' 195 - 7 ' )
	await ctx.send ( f' 188 - 7 ' )
	await ctx.send ( f' 181 - 7 ' )
	await ctx.send ( f' 174 - 7 ' )
	await ctx.send ( f' 167 - 7 ' )
	await ctx.send ( f' 160 - 7 ' )
	await ctx.send ( f' 153 - 7 ' )
	await ctx.send ( f' 146 - 7 ' )
	await ctx.send ( f' 139 - 7 ' )
	await ctx.send ( f' 132 - 7 ' )
	await ctx.send ( f' 125 - 7 ' )
	await ctx.send ( f' 118 - 7 ' )
	await ctx.send ( f' 111 - 7 ' )
	await ctx.send ( f' 104 - 7 ' )
	await ctx.send ( f' 97 - 7 ' )
	await ctx.send ( f' 90 - 7 ' )
	await ctx.send ( f' 83 - 7 ' )
	await ctx.send ( f' 76 - 7 ' )
	await ctx.send ( f' 69 - 7 ' )
	await ctx.send ( f' 62 - 7 ' )
	await ctx.send ( f' 55 - 7 ' )
	await ctx.send ( f' 48 - 7 ' )
	await ctx.send ( f' 41 - 7 ' )
	await ctx.send ( f' 34 - 7 ' )
	await ctx.send ( f' 27 - 7 ' )
	await ctx.send ( f' 20 - 7 ' )
	await ctx.send ( f' 13 - 7 ' )
	await ctx.send ( f' 6 - 7 ' )
	await ctx.send ( f'zxc!!!' )
	

	


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
	emb.add_field( name = '{}gym'.format(PREFIX), value = '• Заглянуть в раздевалку качалки... (Делай на свой страх) •', inline=False)
	emb.add_field( name = '{}van'.format(PREFIX), value = '• Позвать Вэна Даркхолма... •', inline=False)
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
