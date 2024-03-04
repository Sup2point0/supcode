## `send`
Sends a message to a channel.

```coffee
func discord.channel.send(str 'content' = none) [
  | react = none
  | stickers = none
  | attach = none
  | embed = none
  | embeds = none
  | view = none
  | views = none
  | delete = 0.0
]
```

### Inputs
| input | aliases | type | description |
| :---- | :------ | :--- | :---------- |
| `react` | `reactions` | [`discord.(emoji)s`](emoji.md) | Reaction(s) to add. |
| `sticker` | `stickers` | [`discord.(sticker)s`](sticker.md) | Sticker(s) to add. |
| `attach` | `attachments` | [`discord.(asset)s`](asset.md) | Attachment(s) to upload. |
| `embed` | `embeds` | [`discord.(embed)s`](embed.md) | Embed(s) to add. |
| `view` | `views` | [`discord.(view)s`](view.md) | View(s) to add. |
| `delete` | `delete_after` | `float`, `datix.time`, `datix.date`, `datix.datetime` | The duration after which to delete the message. |

### Example
```coffee
discord.channel(...).send("sup") [
  | attach = sys.file('sup.svg')
  | embed = discord.embed() [...] {...}
  | view = discord.view() [...] {...}
]
```

<br>
---
<br>

## `reply`
Replies to a message.

```coffee
func discord.message.reply(str 'content' = none) [
  | mention = false
  | react = none
  | stickers = none
  | attach = none
  | embed = none
  | embeds = none
  | view = none
  | views = none
  | delete = 0.0
]
```
