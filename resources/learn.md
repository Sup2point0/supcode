# Learn X in Y Minutes, Where X = supcode

Here’s a whirlwind tour to see what supcode is all about. This is *not* in-depth – it just demonstrates the basic syntax of supcode, the core ideas, and some cool novel features. If you’ve learnt a programming language before, it shouldn’t be difficult to pick up at all. That being said, supcode has quite a few quirks and a whole lotta syntactic sugar that can get pretty deep. Let’s go!

> [!TIP]
> It’s probably better to view this page on the [supcode site](https://sup2point0.github.io/supcode/spin) where there’s syntax highlighting :v

```
\ COMMENTS start with a backslash

\\
   multi-line comments start and end
   with double backslashes
\\

\\\
indentation is optional,
   but we like 3-space indentation ;)
\\\

"double quotes are used for STRING literals"

"""triple double quotes
allow strings to span multiple lines"""

\ output to console
sys.out("sup world!")


\ SECATORS denote sections in code
<sec 'variables'>

   \ VARIABLES can be created without a value
   create var 'sup'
   
   \ give it a value
   set sup = 2.0
   
   \ change its value
   alt sup + 6.9
   
   \ variable initialisation can be condensed
   set 'soup' = "yum"
   
   \ single quotes denote SHARDs, identifiers for objects
   \ single and double quotes are *not* interchangeable
   \ single quotes must be used when an object is created
   set 'new' = "shiny!"
   set new = "shinier!!"
   
   \ shards can have hyphens
   set 'suppety-sup' = 2
   sys.out(suppety-sup) \ -> 2

</sec>


<sec 'functions'>

   \ create a new FUNCTION
   create func 'yo'
   
   \ CALL a function
   yo() \ -> none
   
   \ use DEFINE to omit shard quotes
   define say-yo() {
      \ return a value
      out "yo"
   }
   
   sys.out(yo()) \ -> yo
   
   \ core positional-only PARAMETERS, separated by commas
   define whats-good('person', 'punct') {
      out "sup " + person + punct
   }
   
   whats-good("iTechnicals", "!") \ -> sup iTechnicals!
   
   \ configurational parameters, separated by pipes
   define wahey() ['is-awesome' | 'is-sad'] {
      if is-awesome {
         out "everything is awesome"
      elif is-sad |
         out "winter sadness"
      }
   }
   
   wahey()[true, is-sad = false] \ -> everything is awesome
   
   \ provide default values to make parameters optional
   define say-this('lang' = "supcode") [
     | 'thought' = "cool"
   ] {
      out lang + " is " + thought
   }
   
   say-this() \ -> supcode is cool
   say-this()[thought = "wack"] \ -> supcode is wack
   
   \ everything in supcode is an object
   \ functions can be stored in variables
   set 'dangerous-object' = say-this
   dangerous-object("Ruby")["pretty"] \ -> Ruby is pretty

\ generic secator closing tag
</>


<sec 'structs'>

   \ STRUCTS represent types of objects
   \ everything is an object, and every object belongs to a struct
   "woah" is str \ -> true
   2.0 is int \ -> false
   true is bool \ -> true
   
   \ create a struct
   create struct 'Tutorial'
   
   \ create an instance of a struct
   set 'this' = create Tutorial
   
   \ define attributes (variables, functions, nested constructs) of the struct
   evolve struct Tutorial {
   
      \ create attributes
      'version'
   
      \ use EVOLVE to redefine an existing object
      \ this overrides what `create Tutorial` does
      evolve action create self(ctx) [
        | 'version'
      ] {
         \ set instance attribute
         set self.version = version
      }
   
      \ create a method (still called a function)
      define self.check-version() {
         out self.version > 2.0
      }
   
      \ create a private function (never enforced)
      define self..update-version() {
         alt this.version + 0.1
      }
   }
   
   \ use the struct
   set 'new-tutorial' = Tutorial()[version = 2.0]
   new-tutorial..update-version()
   if new-tutorial.check-version() {
      sys.out("tutorial updated~")
   }
   
   \ INHERIT from other structs
   create struct 'Advanced-Tutorial' [Tutorial] {
      evolve create self(ctx) [version] {
         \ access attributes of superclass
         sup()[version = version +1]
      }
   }
   
   </>
   
   
   <sec 'classes>
   
   \ use classes to organise variables
   create class 'config' {
      set 'indentation' = 3
      set 'whitespace' = "spaces"
   }
   
   \ use dot notation to access attributes
   config.whitespace \ -> "spaces"
   sys.out(config.indentation +1) \ -> 4

</>


\ close all unclosed secators, if any
<//>
```
