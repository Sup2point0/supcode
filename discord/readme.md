# discord.sc 1.2

An endorsed supcode extension for interacting with the [Discord API](https://discord.com/developers/docs), specifically for creating bots.


## Subextensions

### [`slash`](slash)
Slash commands implementation and functionality.


## Intrinsics

### [`disflux`](disflux)
Discord-specific errors.


## Quick Specimen
Here’s a quick showcase of a simple Discord bot:

```coffee
spec code { ver = 5.6 | syn = utinax | sty = stan }

activate discord { ver = 1.2 }

create discord.bot('demo') [token = discord.token('dQw4w9WgXcQ')] {
  create discord.command 'sup' {
    define demo.sup(ctx) {
      ctx.reply("sup")
    }
  }
}

demo.start()
```

Many more examples can be found in [specimens](specimens).


## Syntax
discord.sc encourages an object-oriented syntax style, although supports various others too.

Throughout this repository all code blocks will use CoffeeScript syntax highlighting, which is highly flexible and perfect for adding contrast, while not (significantly) disrupting or detracting from any semantics of the code.
