spec code { ver = 5.6 | syn = utinax | sty = stan }

locate discord  { ver = 1.2 }
activate discord


create discord.bot 'name' [
  | token = "token"
  | intents = all
  | prefix = "prefix"
]

name.start()
