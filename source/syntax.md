# supcode Syntax Flavours

Supcode 5.0 has 3 syntax flavours, each offering dramatically different styles, and useful for different applications.

## `utinax`

| <td colspan="2"> `Utinax One` ||
| :-- | :-- |
| description | The standard Supcode syntax.
| style | standard |
| latest revision | `one` |
| updates | Utinax remains largely unchanged from its initial release. |

### Specimen

```
spec code {
  | lan = sup | ver = 5.0
  | syn = utinax | rev = one
}

< utinax >

create struct 'demo' {
  on demo.create(ctx, str(name), par(age)[int, numc]) [(option)s] {{
    set demo.'name' = name
    set demo.'age' = round(age)
    set demo.'id' = str(ran(1000~9999))
  }}
}

< /utinax >
```

## `veritinax`

| <td colspan="2"> `Veritinax 1.0` ||
| :-- | :-- |
| description | Full, expanded syntax closely resembling English.
| style | expanded |
| latest revision | `1.0` |
| updates | ... |

## `resinax`

| <td colspan="2"> `Resinax 1.1` ||
| :-- | :-- |
| description | Highly condensed syntax not intended for human readability.
| style | condensed |
| latest revision | `1.1` |
| updates | Many newly added symbols and shortcuts. |
