import discord
from discord.ext import commands
import time
import random

intents = discord.Intents.default()
intents.message_content = True
 
noticias = [
    "40 por ciento de las zonas terrestres están degradadas.",
    "Desde el año 2000, el número y la duración de los períodos de sequía han aumentado un 29 % y, de no cambiar esta tendencia, la situación afectará a más de tres cuartas partes de la población mundial para el 2050.",
    "Países como Chile, Brasil y México enfrentan sequías prolongadas, mientras que naciones como Ecuador y Colombia tienen períodos de sequía influenciados."
]



bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Hola(ctx):
    await ctx.send(f'Hola, soy {bot.user}! Estoy aqui para ayudarte a saber mas sobre cuidar el medio ambiente')
    time.sleep(3)
    await ctx.send(f'En que te puedo ayudar?')

@bot.command()
async def Ayuda(ctx):
    await ctx.send(f'Hola, Aqui tienes algunas acciones que me puedes preguntar')
    time.sleep(2)
    await ctx.send(f'Lista de cosas organicas($LCorganicas)')
    await ctx.send(f'Lista de cosas inorganicas($LCinorganicas)')
    await ctx.send(f'Noticias sobre el medio ambiente($Noticias)')
    await ctx.send(f'Recomendaciones($Recomendaciones)')
    await ctx.send(f'Ideas Para Reciclar($Ideas)')

@bot.command()
async def LCorganicas(ctx):
    await ctx.send(f'cáscaras de fruta o verdura, restos de comida, cascarones de huevo, pan, tortillas, filtros para café, bolsitas de té, heces de animales, lácteos (sin recipiente), huesos, semillas, flores, pasto y hojarasca.')

@bot.command()
async def LCinorganicas(ctx):
    await ctx.send(f'Embalajes de celofán, Bolsas de plástico, Ropa de fibras sintéticas, Recipientes de PVC (bandejas, botellas, etc.), Pilas, Baterías, Tetrabricks, Botellas de cristal')



@bot.command()
async def Ideas(ctx):
    recetas = ['Macetas y jardines: Corta la parte superior de una botella de plástico y perfora agujeros en la base para el drenaje. Llena con tierra y planta tus flores o hierbas favoritas. También puedes colgarlas en la pared para crear un jardín vertical. Otra opción es usar la botella entera como sistema de autorriego.','Organizadores: Las botellas de plástico transparente pueden convertirse en organizadores para objetos pequeños como botones, monedas o llaves. Corta la base y úsala como recipiente con tapa o únelas con una cremallera para hacer un monedero.']
    elemento_aleatorio = random.choice(recetas)
    await ctx.send(f"{elemento_aleatorio}")

@bot.command()
async def Recomendaciones(ctx):
    recomendaciones = ['Separa cada residuo en un contenedor diferente de tu hogar.', "Crea abono para tus plantas con los restos de comida, poda o posos de café.", "Utiliza los complementos de tu ropa y accesorios como cremalleras y botones para otras prendas."]
    elemento_aleatorio = random.choice(recomendaciones)
    await ctx.send(f"{elemento_aleatorio}")

@bot.command()
async def Noticias(ctx):
    elemento_aleatorio = random.choice(noticias)
    await ctx.send(f"{elemento_aleatorio}")

bot.run("token")
