import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from functions import get_formatted_data, get_help_message

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define os intents
intents = discord.Intents.default()
intents.message_content = True  # Habilita a leitura do conteúdo das mensagens

# Define o prefixo dos comandos do bot e os intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content_lower = message.content.lower()

    # Mensagem de ajuda se a mensagem contiver 'c3po'
    if 'c3po' in content_lower:
        await message.channel.send(get_help_message())

    # Identifica a categoria e realiza a busca
    words = message.content.split()
    response_sent = False
    
    # Combina as palavras para formar possíveis nomes
    for i in range(len(words)):
        for j in range(i, len(words)):
            query = ' '.join(words[i:j+1])
            for category in ['people', 'planets', 'starships']:
                response = get_formatted_data(category, query)
                if "I couldn't find any information on that." not in response:
                    await message.channel.send(response)
                    response_sent = True
                    break
            if response_sent:
                break
        if response_sent:
            break
    
    await bot.process_commands(message)

@bot.command(name='hi')
async def hi(ctx):
    response = "Hi, I'm C3PO"
    await ctx.send(response)

@bot.command(name='show_help')
async def show_help(ctx):
    await ctx.send(get_help_message())

# Executa o bot
bot.run(TOKEN)
