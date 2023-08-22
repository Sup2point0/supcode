# supcode

```coffee
prompt.open()
prompt.out("sup world!")
```


## Introduction

**Supcode** (stylised *supcode*) is a general-purpose text-based programming language created by [Sup#2.0](https://github.com/Sup2point0) under 2.0 Studios. It is largely based on [Scratch](https://scratch.mit.edu), [Python](https://python.org) and [Wikitext](https://mediawiki.org/wiki/Wikitext), and is itself programmed in the Origin 2 base programming language. The current major version is supcode 5.0, with the latest major release being supcode 5.7.

<table>
  <tr>
    <th colspan="2"> <h3> supcode 5.0 </h3> </th>
  </tr>
  <tr>
    <td> official name </td>
    <td> supcode </td>
  </tr>
  <tr>
    <td> format </td>
    <td> text-based </td>
  </tr>
  <tr>
    <td> level </td>
    <td> <a href="https://wikipedia.org/wiki/High-level_programming_language">high-level</a> </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Execution_(computing)">execution</a> </td>
    <td> <a href="https://wikipedia.org/wiki/Interpreter_(computing)">interpreted</a> </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Programming_paradigm">paradigm</a> </td>
    <td> multi-paradigm – <a href="https://wikipedia.org/wiki/Imperative_programming">imperative</a>, <a href="https://wikipedia.org/wiki/Event-driven_programming">event-driven</a>, <a href="https://wikipedia.org/wiki/Parallel_computing">multi-threaded</a> </td>
  </tr>
  <tr>
    <td> purpose </td>
    <td> <a href="https://wikipedia.org/wiki/General-purpose_programming_language">general-purpose</a> – games, programs, scripts </td>
  </tr>
  <tr>
    <td> syntax </td>
    <td> human-friendly – readable, intuitive, keyword-focused </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Type_system">type</a> </td>
    <td> <a href="https://wikipedia.org/wiki/Type_system#DYNAMIC">dynamic</a> </td>
  </tr>
  <tr>
    <td> indentation </td>
    <td> <a href="https://wikipedia.org/wiki/Off-side_rule">significant</a> </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Operating_system">platform</a> </td>
    <td> any </td>
  </tr>
  <tr>
    <td> programmed in </td>
    <td> Origin 2 </td>
  </tr>
  <tr>
    <td> based on </td>
    <td> <a href="https://scratch.mit.edu">Scratch</a>, <a href="https://python.org">Python</a> </td>
  </tr>
  <tr>
    <td> loosely based on </td>
    <td> <a href="https://mediawiki.org/wiki/Wikitext">Wikitext Markup</a>, <a href="https://swift.org">Swift</a>, HTML </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Filename_extension">filename extensions</a> </td>
    <td> <code>.sc</code>, <code>.sc5</code>, <code>.scx</code> </td>
  </tr>
  <tr>
    <td> other extensions </td>
    <td> <code>.scd</code>, <code>.scp</code>, <code>.scv</code>, <code>.scl</code>, <code>.scs</code>, <code>.scg</code> </td>
  </tr>
  <tr>
    <td> main <a href="https://wikipedia.org/wiki/Flavors_(programming_language)">flavour</a> </td>
    <td> <a href="source/syntax.md#utinax">Utinax One</a> </td>
  </tr>
  <tr>
    <td> other flavours </td>
    <td> <a href="source/syntax.md#veritinax">Veritinax One</a>, <a href="source/syntax.md#resinax">Resinax 1.6</a> </td>
  </tr>
  <tr>
    <td> initial release </td>
    <td> September 2021 </td>
  </tr>
  <tr>
    <td> founder </td>
    <td> <a href="https://github.com/Sup2point0">Sup#2.0</a> </td>
  </tr>
  <tr>
    <td> developer </td>
    <td> 2.0 Studios (2.0 Studios LLC) </td>
  </tr>
  <tr>
    <td> <a href="https://wikipedia.org/wiki/Integrated_development_environment">IDEs</a> </td>
    <td> <a href="suplus/supcode%20Studio">supcode Studio</a>, <a href="suplus/supcode%20Studio/supcode%20Studio%20Strium">supcode Studio Strium</a> </td>
  </tr>
  <tr>
    <td> latest release </td>
    <td> 5.7 (July 2023) </td>
  </tr>
</table>

### Aims and Improvements
Supcode is designed to be intuitive, readable, and versatile.

As a bridge of sorts between the block-based environment of Scratch and proper text-based programming languages, its structure and syntax are fairly similar. In particular, it follows a logical flow...

Supcode comes with powerful customisability and convenient shortcuts. Like Scratch, there is an extensive assortion of [extensions](extensions), both [internal](extensions/ixtensions) and [external](extensions), to allow for limitless specialisation and applications.

### Files and Applications
Supcode files use the `.sc` filename extension. Often, this has a number following it to indicate the version number (`.sc4`, `.sc5`, etc.). Extensions use the `.scx` file extension. There are also a several other file extensions for specialised cases, such as `.scd` or `.scv`, though these are rarely used.


<br>


## Specimens

```coffee
\ supcode 5.7

create struct 'SoupMachine' {
  evolve func self.create(ctx) [
    | num 'cost'
    | str 'name' = none
    | (str)s 'flavours' = ()
  ] {
    set self.'cost' = cost
    set self.'name' = { if name then name else ctx.shard.str }
    set self.'flavours' = { loop for each in flavours || case(each)[lower] }
  }
  
  define self.purchase() [
    | source
    | int 'count' = 1
    | pool[self.flavours] 'flavour' = none
  ] {
    if count < 1 {
      evoke "Can’t give that many bowls of soup!"
    }
    
    if not flavour {
      set 'flavour' = random(self.flavours)[option]
    }
    
    alt source - self.cost * count
    func.out("Here’s some flavour` soup!")
  }
}

set 'credits' = 200
set 'soupy' = SoupMachine() [
  | cost = 20
  | flavours = "tomato", "mushroom", "potato"
]

sys.out(soupy.purchase(credits, 1, "mushroom"))
```

More specimens can be found [here](specimens).
