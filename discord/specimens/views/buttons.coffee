spec code { ver = 5.4 | syn = utinax | sty = stan }

activate discord { ver = 1.2 }


create discord.bot('bot') [token = "dQw4w9WgXcQ"]

create discord.slash.command {
  define bot.test(ctx) {

    create discord.view 'visual' {
      create view.button 'test' {
        on test.press(ctx) {
          ctx.respond("sup")
        }
      }
    }

    ctx.respond() [view = visual]
  }
}

create discord.slash.command {
  define bot.test(ctx) {

    create discord.view 'visual' {
      create view.button 'test' [
        | style = button.style('green')
        | icon = discord.emoji(':cog:')
      ] {
        on test.press(ctx) {
          set test.icon = discord.emoji(':tick:')
          ctx.edit()[view = visual]
        }
      }
    }

    ctx.respond()[view = visual]
  }
}


bot.start()
