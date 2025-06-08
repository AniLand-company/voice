import disnake
from disnake.ext import commands
import json
import asyncio
from typing import Dict, Optional, List
# Код на Boosty
    @commands.slash_command(name="voice", description="Настройка системы приватных комнат")
    @commands.has_permissions(administrator=True)
    async def voice(self, inter: disnake.ApplicationCommandInteraction):
# Код на Boosty
def setup(bot):
    bot.add_cog(VoiceRoomSystem(bot))
    bot.add_cog(VoiceSetup(bot))
