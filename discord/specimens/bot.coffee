\ extensive discord bot
\ discord.sc specimen

spec code { ver = 5.6 | syn = utinax | sty = stan }

enable sys
activate securex

locate discord { ver = 1.2 }
activate discord
activate discord.slash


create discord.bot('bot') [
  | token = securex.redact('token')
  | intents = all
  | prefix = "."
]

on bot.connect {{
  sys.out("connected")
}}

create discord.command {
  define bot.test(ctx) {
    ctx.out("sup")
  }
}

create discord.command 'sup' {
  define bot.testing(ctx, par) {
    ctx.reply("sup `par`")[mention = false]
  }
}

create discord.command 'complex' {
  define bot.multi(ctx, str('par1'), int('par2'), bool('par3')) {
    if par3 {
      if par2 > 2.0 {
        ctx.out(str)
      }
    }
  }
}

define bot.'help'(ctx) {
  ctx.reply() [embed = discord.embed() [
    | head.title = "Help"
    | body.col = 0x4090f1
    | body.text = "A demonstrative advanced Discord bot, showcasing all of the capabilities of discord.sc"
    | foot.text = "Requested by `ctx.user`",
    | foot.time = ctx.time
  ]]
}

create discord.slash.command 'commands' [desc = "view a list of available commands"] {
  define bot.view(ctx) {
    ctx.respond() [embed = discord.embed() [
      | head.title = "Commands"
      | body.col = 0xff0090
      | body.text = """
        ...
      """
      | foot.text = "Showing `body.text.len[line]` commands"
    ]]
  }
}

create discord.slash.command [desc = "get profile picture of a user in the server"] {
  define bot.pfp(ctx, discord.member(user)) {
    ctx.respond()[attach = user.avatar | ephemeral = true]
  }
}

create discord.slash.command [desc = "select a colour role to add to your profile"] {
  define bot.func(ctx, discord.option('col') [
    | name = "colour"
    | description = "pick a colour"
    | options = {blue, red, green, purple, orange, pink, yellow}
    | default = slot(blue)
    | required = true
  ]) {
    role = ctx.guild.roles#(col)
    ctx.user.addRole(role)
  }
}

on discord.message.send(ctx) {{
  sys.log("`ctx.message.sender` said `ctx.message.content` in `ctx.channel.name`")
  await bot.process(ctx)
}}

on bot.command.call(ctx) {{
  sys.log("`ctx.user` used `ctx.command.name`")
}}

on bot.interaction.call(ctx) {{
  sys.log(ctx.data)
  if ctx.valid {
    sys.log("`ctx.user` used `ctx.command.name`")
    await bot.slash.process(ctx)
  }
}}


bot.start()
