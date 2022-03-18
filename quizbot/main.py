import nextcord
from nextcord.ext import commands
import time
from keep_alive import keep_alive
from discord.player import FFmpegOpusAudio
from discord.player import FFmpegPCMAudio


client = nextcord.Client()
client = commands.Bot(command_prefix="+")

@client.event
async def on_ready():
    print(f'Zalogowano:  {client.user}')


obrazki = {"1":"1.png", "2":"2.png", "3":"3.png", "4":"4.png", "5":"5.png", "6":"6.png", "7":"7.png", "8":"8.png", "9":"9.png","10":"10.png", "11":"11.png", "12":"12.png", "13":"13.png","14":"14.png", "15":"15.png", "16":"16.png", "17":"17.png", "18":"18.png", "19":"19.png", "20":"20.png", "21":"21.png", "22":"22.png","23":"23.png", "24":"24.png", "25":"25.png", "26":"26.png", "27":"27.png", "28":"28.png", "29":"29.png", "30":"30.png", "31":"31.png", "32":"32.png", "33":"33.png", "34":"34.png", "35":"35.png", "36":"36.png", "37":"37.png",
"38":"38.png", "39":"39.png", "40":"40.png", "41":"41.png",
"42":["42.png", "43.png", "44.png", "45.png", "46.png", "47.png"],
"43":["48.png", "49.png", "50.png", "51.png", "52.png"],
"44":["53.png", "54.png", "55.png", "56.png", "57.png"],
"45":["58.png", "59.png", "60.png", "61.png", "62.png"],
"46":"63.png", "47":"64.png", "48": "65.png", "49":"66.png",
"50":"67.png", "51":"68.png",}


zbiory_nazw = {"1":"Estonia, Rumunia, Kolumbia, Parawgwaj, Dania, Wenezuela",
"2":"Izrael, Tanzania, Antigua i Barubda, Czechy, Surinam",
"3":"Jordania, Zambia, Gwatemala, Chile, Belgia", "4":"Haiti, Kambodża, Ekwador, Francja, Wyspy Świętego Tomasza i Książęca", "5":"Sri Lanka, Niemcy, Boliwia, Belize, Tunezja", "6":"To"


, "7":" Kostaryka, Bahamy, Dominikana, Jamajka, Kanada",
  "8":"Paragwaj, Brazylia, Trynidad i Tobago, Urugwaj, Argentyna"


, "9":"Holadnia, Hiszpania, Mołdawia, Andora, Bułgaria", "10":"Kenia, Sahara Zachodznia, Seszele, Liberia, Rwanda", "11":"Wietnam, Nepal, Chiny, Singapur, Korea Północna", "12":"Syria, Armenia, Indonezja, Irak, Gruzja",
"13":"Polska, Estonia, Meksyk, Sierra Leone, Barbados",
"14": "Płock, Poznań, Warszaw, Kraków, Gniezno",
"15": "Bydgoszcz, Wrocław, Gdańsk, Białystok, Szczecin",
"16": "Łódź, Zamość, Lublin, Pruszków, Dąbrowa Górnicza",
"17": "Daleszyce, Elbląg, Babimost, Cegłów, Aleksandrów Kujawski",
"18": "Iłowa, Jawor, Frampol, Garwolin, Hrubieszów",
"19": "Łańcut, Mirsk, Koluszki, Nowa Sól, Lipiany",
"20": "Sanok, Świerzawa, Pionki, Oborniki, Radymno",
"21": "Zabrze, Żory, Wadowice, Tczew, Wąsosz",
"22": "Cintra, Kovir i Poviss, Temeria, Redania, Aedirn",
"23": "Liga z Hengfors, Verden, Lyria i Rivia, Skellige, Cidaris",
"24": "Toussaint, Novigrad, Kaedwen, Zerrikania, Nilfgrad",
"25": "Ofir, Brokilon, Góry Sine, Mahakam, Dol Blathanna",
"26": "Komandos w twoim domu, Sex flary i valentine, Szybowcowe chłopaki, M10 szturmowy, Bofors w minutę",
"27": "Zrzuty i krokodyl, Avre, Boys, Doktryna Przełamania, Szybowiec z krokodylem",
"28": "Kultura miśków, Ruch LGBT, Aseksualność, Biseksualność, Flaga osób interpłciowych",
"29": "Flaga osób niebinarnych, Flaga lesbijek, Flaga osób panseksualnych, Flaga gejów, Flaga osób demiseksualnych",
"30": "Flaga osób genderfluid, Flaga osób agender, Flaga osób poliseksualnych, Flaga osób genderqueer, Flaga osób transpłciowych",
"31": "Templariusze, Rycerze Tau, Lazaryci, Joannici, Bożogrobcy",
"32": "Krzyżacy, Zakon św. Tomasza z Akki, Zakon Monte Gaudio, Kalatrawensi, Rycerze Chrystusowi",
"33": "Mercedariusze, Zakon szkrzydła św. Michała, Zakon Avis, Zakon z Alcantara, Zakon Santiago",
"34": "Podaj daty wydania, możesz się pomylić o rok",
"35": "KO, PIS, Lewica, PIS, PIS, KP",
"36": "Zamość, Kraków, Rzeszów, Łódź, Lublin",
"37": "Niemcy, USA, Polska, Rosja, Francja, Wielka Brytania",
"38": "P-26A-33, P-26B-35, P-26A-34 M2",
"39": "M4A3 (76) W, M4A2 (76) W, M4A1 (76) W",
"40": "Ostwind II, Wirbelwind, Ostwind",
"41": "T-34 (1942), T-34E STZ, T-34 (1941), T-34 (1940), T-34-57",
"42": "Zgaduj zgadula: Mordhau, Total war Medieval II, Fallout 76, Chivarly II, Total war Attilla, Fallout 4",
"43": "Wojna 100 letnia ziomalu, Bitwa pod Azincourt, Bitwa o Auray, Bitwa pod Sluys, Bitwa o śledzie, Oblężenie Orleanu",
"44": "Bitwa pod Warną - 1444, Bitwa pod Koźminem - 1497 , Bitwa pod Grunwaldem - 1410, Bitwa pod Koronowem - 1410, Bitwa pod Chojnicami - 1454",
"45": "Agir, Dagda, Balor, Lug, Oisin",
"46": "Moskwa, Berlin, Wilno, Madryt, Berno",
"47": "Helsinki, Paryż, Belgrad, Skopje, Lizbona",
"48": "Bruksela, Amsterdam, Praga, Podgorica",
"49": "San Marino, Sarajewo, Bratysława, Zagrzeb, Lublana",
"50": "Ankara, Oslo, Kijów, Mińsk, Dublin",
"51": "Wiedeń, Luksemburg, Valletta, Bukareszt, Kiszyniów",}

dobre_zbiory = {"1":"Paragwaj, Wenezuela, Kolumbia, Rumunia, Estonia, Dania",
                "2":"Antigua i Barbuda, Surinam, Czechy, Tanzania, Izrael",
                "3":"Gwatemala, Chile, Belgia, Zambia, Jordania",
                "4":"Francja, Haiti, Ekwador, Kambodża, Wyspy Świętego Tomasza i Książęca",
                "5":"Belize, Boliwia, Tunezja, Sri Lanka, Niemcy", "6":"Grenada, Peru, Czarnogóra, Togo, Pakistan", "7":"Bahamy, Jamajka, Dominikana, Kostaryka, Kanada",
                "8":"Argentyna, Brazylia, Trynidad i Tobago, Paragwaj, Urugwaj",
                "9":"Bułgaria, Andora, Hiszpania, Holadnia, Mołdawia",
                "10":"Seszele, Sahara Zachodnia, Liberia, Kenia, Rwanda",
                "11":"Korea Północna, Chiny, Wietnam, Nepal, Singapur",
                "12":"Gruzja, Armenia, Syria, Irak, Indonezja",
                "13":"Barbados, Meksyk, Estonia, Polska, Sierra Leone",
              
             
                "14": "Warszawa, Kraków, Gniezno, Płock, Poznań",
                "15": "Gdańsk, Szczecin, Bydgoszcz, Wrocław, Białystok",
                "16": "Dąbrowa Górnicza, Lublin, Łódź, Zamość, Pruszków",
                "17": "Aleksandrów Kujawski, Babimost, Cegłów, Daleszyce, Elbląg",
                "18": "Frampol, Garwolin, Hrubieszów, Iłowa, Jawor",
                "19": "Koluszki, Lipiany, Łańcut, Mirsk, Nowa Sól",
                "20": "Oborniki, Pionki, Radymno, Sanok, Świerzawa",
                "21": "Tczew, Wadowice, Wąsosz, Zabrze, Żory",
                "22": "Temeria, Redania, Kovir i Poviss, Aedirn, Cintra",
                "23": "Lyria i Rivia, Skellige, Cidaris, Liga z Hengfors, Verden",
                "24": "Kaedwen, Novigrad, Nilfgard, Toussaint, Zerrikania",
                "25": "Góry Sine, Dol Blathanna, Mahakam, Ofir, Brokilon",
                "26": "Bofors w minutę, Szybowcowe chłopaki, M10 szturmowy, Komandos w twoim domu, Sex flary i valentine",
                "27": "Avre, Boys, Zrzuty i krokodyl, Szybowiec z krokodylem,  Doktryna Przełamania",
                "28": "Ruch LGBT, Aseksualność, Biseksualność, Flaga osób interpłciowych, Kultura miśków",
                "29": "Flaga lesbijek, Flaga osób niebinarnych, Flaga gejów, Flaga osób demiseksualnych, Flaga osób panseksualnych",
                "30": "Flaga osób poliseksualnych, Flaga osób transpłciowych, Flaga osób genderqueer, Flaga osób agender, Flaga osób genderfluid",
                "31": "Rycerze Tau, Lazaryci, Joannici, Bożogrobcy, Templariusze",
                "32": "Zakon Monte Gaudio, Krzyżacy, Zakon św. Tomasza z Akki,  Rycerze Chrystusowi, Kalatrawens","33": "Zakon Avis, Zakon z Alcantara, Zakon Santiago, Zakon szkrzydła św. Michała, Mercedariusze",
                "34": "Daty wydania: coh2 - 2013, coh1 - 2006, aoe hd - 1999, aoe definitive edition - 2019, HOI IV - 2016, EU IV - 2013",
                "35": "PIS, Lewica, PIS, KP, KO, PIS",
                "36": "Łódź, Lublin, Zamość, Kraków, Rzeszów",
                "37": "Polska, Rosja, Wielka Brytania, Francja, Niemcy, USA`",
                "38": "P-26A-34 M2, P-26A-33, P-26B-35",
                "39": "M4A1 (76) W, M4A3 (76) W, M4A2 (76) W",
                "40": "Wirbelwind, Ostwind, Ostwind II",
                "41": "T-34 (1940), T-34 (1941), T-34 (1942), T-34E STZ,  T-34-57",
                "42": "Total war Medieval II, Total war Attilla, Chivarly II, Mordhau, Fallout 4, Fallout 76",
                "43": "Bitwa o Auray, Bitwa pod Sluys, Bitwa pod Azincourt, Oblężenie Orleanu, Bitwa o śledzie",
                "44": "Bitwa pod Grunwaldem - 1410, Bitwa pod Warną - 1444, Bitwa pod Koronowem - 1410, Bitwa pod Chojnicami - 1454, Bitwa pod Koźminem - 1497",
                "45": "Balor, Agir, Dagda,Oisin, Lug",
                "46": "Berno, Madryt, Berlin, Moskwa, Wilno",
                "47": "Lizbona, Belgrad, Helsinki, Paryż, Skopje",
                "48": "Praga, Podgorica, Budapeszt, Bruksela, Amsterdam",
                "49": "Zagrzeb, Bratysława, Lublana, Sarajewo, San Marino",
                "50": "Dublin, Kijów, Mińsk, Oslo, Ankara",
                "51": "Valletta, Kiszyniów, Bukareszt, Luksemburg, Wiede",}


@client.command()
async def znaki(ctx, czas):
  losowanie = random.randrange(1,45)
  picture = obrazki[f"{losowanie}"]

  channel = ctx.message.author.voice.channel
  await channel.connect()

  if losowanie == 42 or losowanie == 43 or losowanie == 44 or losowanie == 45:
    for e in picture:
      with open(f"{e}", "rb") as f:
        await ctx.send(file=nextcord.File(f))

  else:
    with open(f"{picture}", "rb") as f:
      await ctx.send(file=nextcord.File(f))

  await ctx.send("Poniżej są podane nazwy w losowej kolejności: ")
  await ctx.send(zbiory_nazw[f"{losowanie}"])
  await ctx.send(f"Masz {czas}s czasu!!!")

  song = "milionerzy" + ".mp3"
  source = FFmpegOpusAudio(song)
  ctx.voice_client.play(source)


  time.sleep(int(czas))
  await ctx.send("_5_")
  time.sleep(1)
  await ctx.send("_4_")
  time.sleep(1)
  await ctx.send("_3_")
  time.sleep(1)
  await ctx.send("_2_")
  time.sleep(1)
  await ctx.send("_1_")
  time.sleep(1)
  await ctx.send("_0_")
  time.sleep(1)
  await ctx.send("Koniec czasu!")
  await ctx.send(dobre_zbiory[f"{losowanie}"])

  await ctx.guild.voice_client.disconnect()



@client.command()
async def rozbudzenie(ctx, ilość):

  for word in range(int(ilość)):
    await ctx.reply("grubson")
    await ctx.reply("szanty")


@client.command()
async def skip(ctx):
   await ctx.guild.voice_client.disconnect()


@client.command()
async def pomodoro(ctx, czas):
  time.sleep(int(czas))
  await ctx.send("Koniec nauki!!!")
  await ctx.send("Zaczynamy przerwę!")
  time.sleep(1200)
  await ctx.send("Koniec przerwy!")


  
keep_alive()
client.run("OTMwMDkxNjczMjUyNDI1Nzc4.Ydw1Xw.lUohCbSV2ctHUutsrKT0jEsEMKo")
