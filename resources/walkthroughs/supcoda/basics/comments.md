# Comments

Comments are denoted by a leading `\`, which negates any code following it.

```
\ comments look like this
```

Leaving a space after the slash is good practice for readability.

Comments can also be used to temporarily ‘comment out’ and negate code for testing purposes.

```
\ this code won't run
\sys.exit()
```

In this case, often no space is left to indicate that the code has only been temporarily commented out.

> In Supcode Studio, this also allows the syntax highlighter to detect it as commented-out code, and highlight it differently. [^0]

Generally, comments are placed on their own line, but they can also be placed inline with other code.

```
prompt.out("sup")  \ outputs "sup"
```

To place it between elements of code, a second `\` can be used to end the comment.

```
func("sup", 2.0 \ like so \ , true)
```

However, this is highly discouraged, as it leaves the code quite unreadable.

> Its intended use is for single-line Supcode. Although, even then comments are rarely used, since the code is not intended for human reading.

Comments can span multiple lines if necessary. This is denoted by double `\` both at the start and end of the comment segment.

```
\\ multi-line comments
spanning multiple lines
look like this \\
```

Their main use is for opening information at the top of a section, or commenting out entire chunks of code at once.

```
\\
demonstrative
comment
version 2.1.6
\\
```

If it is the latter, the chunk is usually indented by one layer.

```
\\
  Indentation allows the code to be easily identified
  With a keyboard shortcut, this is all automatic
\\
```

---

When commenting out code, it may be useful to comment certain lines back in, to test them individually. This can be done using breaks in the comments.

To indicate a comment segment with breaks, triple `\` are used. Single-line and multi-line breaks are denoted in the same way as their usual comment counterparts.

```
\\\
  Multi-line comments with breaks
  look like this
  
  This code will run
  \prompt.out("break")
  
  and so will this section
  \\
    ...
  \\
  Again, indentation is automatic with a keyboard shortcut
\\\
```

To demonstrate its use in an actual sample of code:

```
define func(some) {
  \\\
    try {
    \\
      set 'zero' = 0
      func.out(some / zero)
    \\
    evade |
      func.exit()
    }
  \\\
}
```

Here, the code originally within the try segment has been isolated, so that it will output its error rather than silently exiting the function.

---

Empty single-line breaks are often used to indicate paragraphs or sections in particularly long comments. Of course, a line space can be used too, but those can sometimes be omitted transferring documents in certain ways, so leaving a character ensures that doesn’t occur.

```
\\\
  For example, if you have a long chunk of comments at the start of a document to explain its purpose and function, you can use breaks to paragraph the text.
  \
  Like this!
  \
  This makes the text easier to read and the paragraph breaks more distinguishable.
\\\
```

[^0]: this depends on syntax highlighter support
