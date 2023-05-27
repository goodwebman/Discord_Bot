import disnake
from disnake.ext import commands

import datetime

bot = commands.Bot(command_prefix=';', help_command=None, intents=disnake.Intents.all())

TWITCH_BAN_WORDS = ['даун', 'негр', 'черномазый', 'черный', 'чёрный', 'хач', 'аутист', 'дебил', 'педик', 'гомик', 'пидорас', 'натурал']

#  --------------------------------------------------------- Event -------------------------------------------------------


@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work!')



@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(member.guild.roles, id='айди вашей ролли')
    channel = bot.get_channel('id servera')

    embed = disnake.Embed(
        title = 'Новый участник на сервере!',
        description= f'{member.name}#{member.discriminator}',
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)



@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for content in message.content.split():
        if content.lower() in TWITCH_BAN_WORDS:
            await message.delete()
            await message.channel.send(f'{message.author.mention} такие слова запрещены!')



@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author}, у вас недостаточно прав для выполнения данной команды!')
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f'Правильное использование команды {ctx.prefix}{ctx.command.name} {ctx.command.brief}'
        ))

#  --------------------------------------------------------- /Event -------------------------------------------------------


#  --------------------------------------------------------- Bot command -------------------------------------------------------


@bot.command(aliases=['кик','кикаю'])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member : disnake.Member, *, reason='Нарушение правил.'):
    await ctx.send(f'Администратор {ctx.author.mention} исключил пользователя {member.mention}')
    await member.kick(reason=reason)



@bot.command(aliases=['бан', 'банчик', 'баня'])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason='Нарушение правил.'):
    await ctx.send(f'Администратор {ctx.author.mention} забанил пользователя {member.mention}')
    await member.ban(reason=reason)

#  --------------------------------------------------------- /Bot command -------------------------------------------------------



#  --------------------------------------------------------- Slash_command -------------------------------------------------------


@bot.slash_command()
async def timeout(interaction, member: disnake.Member, time: str, reason: str): # ОБЯЗАТЕЛЬНО АНАТАЦИЮ К МЕМБЕРУ!!!!!!
    time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
    await member.timeout(reason=reason, until=time)
    cool_time = disnake.utils.format_dt(time, style='R')
    embed = disnake.Embed(title='Mute', description=f'{member.mention} has been muted out {cool_time}', color=0x00ff00)
    await interaction.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command()
async def untimeout(interaction, member: disnake.Member):
    await member.timeout(reason=None, until=None)
    await interaction.response.send_message(f'Размутил дурочка {member.mention}', ephemeral=True)



@bot.slash_command()
async def avatar(interaction, member: disnake.Member = None):
    user = member or interaction.author
    embed = disnake.Embed(title='Avatar', color=0x2f3136)
    embed.set_image(url=user.display_avatar.url)
    await interaction.response.send_message(embed=embed)



@bot.slash_command()
async def clear(interaction, amount : int):
    await interaction.response.send_message(f'Deleted {amount} message')
    await interaction.channel.purge(limit=amount + 1)




@bot.slash_command()
async def question(inter, ask : str):
    if ask.lower() == 'кб что?':
        info = 'кб сосатб))00)'

    await inter.send(info)




@bot.slash_command()
async def streamers_info(inter, streamer_nick : str):
    if streamer_nick.lower() == 'братишкин' or streamer_nick.lower() == 'brff':

        info = 'Родился Владимир Семенюк в городе Москва 20 мая 1998 года. Учился в одной из средних школ столицы. Однако учебу не жаловал. При каждом удобном случае старался избегать занятия. Все-таки он школу окончил. Даже поступил в высшее учебное заведение. Был план выучиться на программиста, но что-то пошло не так. Занятия парень перестал посещать, и был исключен из университета.'
        embed = disnake.Embed(title='Братишкин', description='ШЕФ', color=0x2f3136)
        embed.set_image(url='https://medialeaks.ru/wp-content/uploads/2021/10/snimok-ekrana-2021-10-08-v-17.27.06.jpg')

    elif streamer_nick.lower() == 'мазелов' or streamer_nick.lower() ==  'mzlf':

        info = 'Парень родился 28 апреля 1999 г. в столице России. Рос в хорошей семье. Родители старались научить сына этикету и правилам хорошего тона. Возможно, поэтому MAZELLOVVV так вежлив с аудиторией. \n Илья учился на экономиста. Он имеет соответствующий диплом. Интересно, что парень вел прямую трансляцию во время экзамена. Однако по профессии никогда работать не хотел. Ему нравилась работа в интернете, и он знал, что обязательно свяжет с ней свою жизнь.'
        embed = disnake.Embed(title='Птички летят бомбить поросят', description='кеквв', color=0x2f3136)
        embed.set_image(url='https://i.pinimg.com/originals/c4/c3/48/c4c34849e871b2df70c1cedea99c76d5.jpg')

    elif streamer_nick.lower() == 'гвин' or streamer_nick.lower() == 'gwin':

        info = 'Александр Гвинский, ну чисто пузо. Смешной уверенный в себе добряк'
        embed = disnake.Embed(title='Гвин', description='пиво', color=0x2f3136)
        embed.set_image(url='https://images.genius.com/2967194c302771214dbb99753520414d.400x400x1.jpg')

    elif streamer_nick.lower() == 'дрейк' or streamer_nick.lower() == 'drake':

        info = 'Настоящее имя – Денис Коломиец. Родился парень 20 августа 2003 года в городе Санкт-Петербург. Свою стримерскую карьеру он, как и многие, начинал с элементарного прохождения любимых игр. Он играл Counter-Strike, Standoff и другие игры. После того, как аудитория на Твиче стала расти, Денис решил выходить в прямые эфиры для общения со зрителями. На таких эфирах парень получал неплохие донаты, также, помимо всего этого, он иногда обозревал различные видео с Ютуба.'
        embed = disnake.Embed(title='Дрейк', description="God's plan?", color=0x2f3136)
        embed.set_image(url='https://sun9-east.userapi.com/sun9-41/s/v1/ig2/LS8-VBmpeLIUv-F5M_5gPWvAw6eGmJf_VhyXkRN2YlWpoFW91puD9GH6thvRP8e17GLHvxi9LXMKfpD9UYJ1dOJp.jpg?size=510x681&quality=95&type=album')

    await inter.send(info, embed=embed)


#  --------------------------------------------------------- /Slash_command -------------------------------------------------------


with open('own_token.txt', 'r', encoding='utf-8') as file:
    token = file.readline()

   
if __name__ == '__main__':
    bot.run(token)
