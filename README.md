# Subtable
A python program for generating text from tables

Subtable is a pretty simple utility at its heart. An object is created, with a filename as an argument. The instance parses the (presumably formatted) file, populating itself.

When asked, the instance will return a string created from the tables it generates from input. The first listed table in the input is assumed to be the master table, and is the top-level table called for generation.

A table has several types of entries:
Exactly one name, in the format of #NAME.
Zero or more subtable calls, in the format of [SUBTABLE NAME]
Zero or more entries, of any format that does not collide with the previous two, terminated by a newline.
Zero or more comments, in the format of //comment

Names must begin with an octothorpe, and are terminated by end of line. They are case-sensitive, and capitalized as a matter of style.

Subtable calls must begin with an opening square brace, and are terminated by a closing square brace. They are case-sensitive, and capitalized as a matter of style; they must match the table name they call.

Comments must begin with two forward slashes, and continue until a newline

Entries are any lines that do not start with one of the control characters/character sequences (#, [, and //), and are terminated by a newline.

All entries under a table are given equal weight. When parsing, subtable calls are replaced with the string generated from calling that subtable. This is recursive; at this time there is no infinte loop protection.

Any text before the first table name entry is ignored, 'cause where would it go?