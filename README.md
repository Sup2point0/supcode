<h1 align="center"> supcode </h1>

<div align="center">

*deliciously flavourful code*

</div>

> [!Note]
> Properly renovating this repository at some point in the imminent future!

---

<div align="center">

[tour](welcome/whirlwind-tour.md) · [grammar](spec/grammar.md)

</div>

supcode is designed to be unique. It’s weird, it’s wacky, and it’s wonderful. Why do stuff the boring way, when we could instead try out crazy new things?

```
activate sys


create struct 'Portal' [Core]
{
   Core 'core'
   bool 'active'

   evolve create self(Core 'core') [
     | bool 'active' = FALSE
   ] {
      set self.core = core
      set self.active = active
   }

   func[Core] self.spin()
   {
      out self.core
   }
}

on activate
{
   set portal = Portal[str]("sup world")[active = TRUE]
   sys.out(portal.spin())
}
```

> [!Tip]
> Check out more of what supcode can do in [A Whirlwind Tour of supcode](welcome/whirlwind-tour.md)!

<table>
  <tr>
    <th colspan="2"> <h3> supcode 6.9 </h3> </th>
  </tr>
  <tr>
    <td> latest release </td>
    <td> 6.9 (concept) </td>
  </tr>
  <tr>
    <td> typing </td>
    <td> dynamic with opt-in static </td>
  </tr>
  <tr>
    <td> paradigm </td>
    <td> all of them </td>
  </tr>
  <tr>
    <td> purposes </td>
    <td> anything you could dream up </td>
  </tr>
  <tr>
    <td> syntax </td>
    <td> flavourful, flexible, fun </td>
  </tr>
  <tr>
    <td> whitespace </td>
    <td> insignificant </td>
  </tr>
  <tr>
    <td> inspired by </td>
    <td> C#, CSS, Haskell, HTML, Python, Ruby, Rust, Swift, TypeScript, Wikitext Markup </td>
  </tr>
  <tr>
    <td> conception </td>
    <td> September 2021 </td>
  </tr>
</table>
