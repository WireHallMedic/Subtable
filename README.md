# Subtable
A python program for generating text from tables

Subtable is a pretty simple utility at its heart. An object is created, with a filename as an argument. The instance parses the (presumably formatted) file, populating itself.

When asked, the instance will return a string created from the table. Tables are divided up into tables.

A table has several types of entries:
Exactly one name, in the format of #NAME.
Zero or more subtable calls, in the format of [SUBTABLE NAME]
Zero or more entries, of any format that does not collide with the previous two, terminated by a newline.
Zero or more comments, in the format of //comment

Names must begin with an octothorpe, and are terminated by end of line. They are not case-sensitive, but capitalized as a matter of style.

Subtable calls must begin with an opening square brace, and are terminated by a closing square brace. They are capitalized as a matter of style, but are programmatically case-insensitive.

Comments must begin with two forward slashes, and continue until a newline

Entries are any lines that do not start with one of the control characters/character sequences (#, [, and //), and are terminated by a newline.

All entries under a table are given equal weight. When parsing, subtable calls are replaced with the string generated from calling that subtable. This is recursive; at this time there is no infinte loop protection.