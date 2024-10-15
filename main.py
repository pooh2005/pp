import os
import discord
from discord.ext import commands

from myserver import server_on

intents = discord.Intents.default()
intents.members = True  # เปิดการใช้งาน event ที่เกี่ยวกับสมาชิก

bot = commands.Bot(command_prefix="!", intents=intents)

# เมื่อมีสมาชิกใหม่เข้าร่วมเซิร์ฟเวอร์
@bot.event
async def on_member_join(member):
    role_name = "Verifed | ยืนยัน"  # ชื่อยศที่ต้องการมอบให้สมาชิกใหม่
    role = discord.utils.get(member.guild.roles, name=role_name)
    
    if role:
        await member.add_roles(role)
        print(f"มอบยศ {role_name} ให้กับ {member.name} เรียบร้อยแล้ว")
    else:
        print(f"ไม่พบยศ {role_name} ในเซิร์ฟเวอร์นี้")

# เริ่มบอท

server_on()

bot.run(os.getenv('TOKEN'))
