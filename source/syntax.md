# supcode Syntax Flavours

Supcode 5.0 has 3 syntax flavours, each offering dramatically different styles, and useful for different applications.


## `utinax`

<table>
  <tr>
    <th colspan="2" > <h3><code> Utinax One </code></h3> </th>
  </tr>
  <tr>
    <td> description </td>
    <td> The standard Supcode syntax. </td>
  </tr>
  <tr>
    <td> style </td>
    <td> standard </td>
  </tr>
  <tr>
    <td> latest revision </td>
    <td> <code> one </code> </td>
  </tr>
  <tr>
    <td> updates </td>
    <td> Utinax remains largely unchanged from its initial release. </td>
  </tr>
</table>

### Specimen

```
spec code {
  | lan = sup | ver = 5
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

<table>
  <tr>
    <th colspan="2" > <h3><code> Veritinax One </code></h3> </th>
  </tr>
  <tr>
    <td> description </td>
    <td> Full, expanded syntax closely resembling English. </td>
  </tr>
  <tr>
    <td> style </td>
    <td> expanded </td>
  </tr>
  <tr>
    <td> latest revision </td>
    <td> <code> 1.1 </code> </td>
  </tr>
  <tr>
    <td> updates </td>
    <td>  </td>
  </tr>
</table>


## `resinax`

<table>
  <tr>
    <th colspan="2" > <h3><code> Resinax One </code></h3> </th>
  </tr>
  <tr>
    <td> description </td>
    <td> Highly condensed syntax not intended for human readability. </td>
  </tr>
  <tr>
    <td> style </td>
    <td> condensed </td>
  </tr>
  <tr>
    <td> latest revision </td>
    <td> <code> 1.6 </code> </td>
  </tr>
  <tr>
    <td> updates </td>
    <td> Many newly added symbols and shortcuts. </td>
  </tr>
</table>
