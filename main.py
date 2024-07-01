import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(989641771862597653)  # ไอดีห้อง
    text = f"สวัสดีค่ะ เข้ามาแล้วอย่าลืมกรอกข้อมูลเหมือนท่านๆอื่นๆด้วยนะคะคุณ {member.mention}!"

    emmbed = discord.Embed(title = 'ยินดีต้อนรับสู่ Liland นะคะ',
                           description ='กรุณากรอกแบบฟอร์มให้ครบ เช่น ชื่อ-อายุ-ชื่อaccount youtube รวมถึงบอกอะไรสักหน่อยด้วยจ้า หากตอบไม่ครบน้องเบลไม่ให้ยศสมาชิกนะคะ',
                           color = 0xFF3399)  # แต่งสี รูป บลาๆ

    await channel.send(text)  # ส่งข้อความห้องนี้
    await channel.send(embed = emmbed)  # คำสั่งใช้ embed ในห้องนั้นๆ

@bot.event
async def on_member_remove(member):  # ส่วนของคนออก
    channel = bot.get_channel(989563837483192341)
    text = f"{member.name} ออกไปแล้ว ขอบคุณที่เคยรู้จักกันน้า ขอให้โชคดีค่ะ"
    await channel.send(text)


 # แชทบอท ถ้าจะเติมอื่นๆ ใช้ elif

@bot.event
async def on_message(message):
    mes = message.content  # ดึงข้อความที่ถูกส่งมา  จากทุกห้อง
    if mes == 'หวัดดีเบล':
        await message.channel.send("สวัสดีค่ะ อิซซาเบลล่ายินดีช่วย กรุณาพิมพ์ / ตามด้วย น้องเบลช่วยที ค่ะ")  # ส่งกลับไปที่ห้องนั้น

    elif mes == 'ไลฟ์มั้ย':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("ไลฟ์ค่ะ คาดว่าเวลาเดิม เอ่อ เรื่องเวลาให้เขาตอบเองนะคะคุณ " + str(message.author.name))

    elif mes == 'รับยศ':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("วิธีรับยศคือกรอกแบบฟอร์มที่ ห้องแนะนำตัว ค่ะคุณ " + str(message.author.name))

    elif mes == 'น้องบิด':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("ไม่ได้ชื่อนี้ค่ะ ต้องการโดนตบหรือคะคุณ " + str(message.author.name))

    elif mes == 'หวยออกอะไร':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("ถ้าน้องเบลรู้ น้องเบลคงไม่ทำงานหนักแบบนี้หรอกค่ะคุณ " + str(message.author.name))

    elif mes == 'พี่ลิสวยมั้ย':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("เดี๋ยวจะหาว่าน้องเบลอวยเจ้านาย พี่ลิสวยมากๆค่ะคุณ " + str(message.author.name))

    elif mes == 'กินอะไรดี':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("นี่เห็นน้องเบลเป็นร้านอาหารตามสั่งเหรอคะคุณ " + str(message.author.name))

    elif mes == 'น้องเบลทำอะไรอยู่':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("ศึกษาความเป็นมนุษย์ให้มากขึ้นค่ะ เผื่อวันหนึ่งน้องเบลจะได้มาแทนที่พี่ลิและพี่ลิจะได้พักบ้างค่ะ")

    elif mes == 'แฟนอาร์ต':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("วาดอะไรก็ได้ส่งที่ห้องแฟนอาร์ตได้เลยค่ะ ขอบคุณนะคะคุณ " + str(message.author.name))

    elif mes == 'กี่โมง':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("ถ้าถามเวลาให้ดูเวลาบนมือถือขอตัวเอง แต่ถ้าเวลาไลฟ์...ถ้าไม่ขี้เกียจ พี่ลิคงจะแท็กเรียกทุกคนเวลาเดิมๆค่ะคุณ " + str(message.author.name))

    elif mes == '555':  # ถามอื่นๆเพิ่มเติม
        await message.channel.send("หัวเราะให้เยอะๆนะคะ คุณจะได้มีความสุขมากๆค่ะคุณ " + str(message.author.name))


    await bot.process_commands(message)
    # น้องบอท ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อค่ะ


   #   /////////// Commands ของอิซซาเบลล่า /////////////
   # กำหนดคำสั่งให้บอท


@bot.command()
async def หวัดดีเบล(ctx):    # ต้องสอดคล้อง on massage ถึงจะใช้งานได้
    await ctx.send(f"กรุณาพิมพ์ / ตามด้วย น้องเบลช่วยที ค่ะคุณ {ctx.author.name}!")

# slash Command

@bot.tree.command(name='วิธีใช้งานดิสนี้') # คอมมานถามชื่อ ตอบด้วยชื่อ
@app_commands.describe(name= 'กรอกชื่อเล่นของ คุณหน่อยนะคะ')
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"สวัสดีค่ะ {name} มีคำถามอะไรพิมพ์ / ตามด้วยน้องเบลช่วยทีได้เลยค่ะ")  # บอทจะตอบตรงนี้ ตามด้วยชื่อ FC

#   Embeds ต่างๆ เซ็ตกรอบเซ็ตอะไร

@bot.tree.command(name='น้องเบลช่วยที', description='คำสั่งต่างๆที่ใช้งานในดิสนี้และน้องเบลตอบได้') # ชื่อคือหลังสแลชคอมมาน ดิสคริปคืออธิบายคนใช้
async def helpcommand(interaction): # ตอบรับหลังจากกดใช้คอมมาน
    emmbed = discord.Embed(title='เลือกใช้คำสั่งเหล่านี้ได้เลยค่ะ',
                           description='คำสั่งที่ใช้ได้ และ วิธีถามน้องเบล',
                           color=0x66FFFF,
                           timestamp=discord.utils.utcnow())
    emmbed.add_field(name='1.รับยศทำยังไง', value='พิมพ์ รับยศ หรือ !รับยศ',inline=False)   # Value คือรายละเอียด หัวข้อคำสั่งตามๆ inline คือให้อยู่บรรทัดเดียวกันมั้ย
    emmbed.add_field(name='2.คำถามทั่วไป', value='เช่น พี่ลิไลฟ์มั้ย พี่ลิไปไหน น้องเบลตอบได้แค่คำถามง่ายๆนะคะ', inline=False)
    emmbed.add_field(name='3.การส่งFanArt', value='ที่ ห้องFanArt โพสต์ได้เลยค่ะ', inline=False)


    emmbed.set_image(url='https://img2.pic.in.th/pic/nongbell.png') # รูปใหญ่แบนน้องน้องในกรอบ
    emmbed.set_author(name='LirinnnnFC', url='https://youtube.com/@lirinnnnfc', icon_url='https://img5.pic.in.th/file/secure-sv1/lirinnnnnnn.png')
    emmbed.set_footer(text='ขอให้ทุกท่านมีวันที่ดีค่ะ', icon_url='https://img5.pic.in.th/file/secure-sv1/lirinnnnnnn.png')  # ส่วยท้ายเล็กๆ ใส่ข้อความตรง text


    await interaction.response.send_message(embed = emmbed)


server_on()


bot.run(os.getenv('TOKEN'))
