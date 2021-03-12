====================
Grid Table
====================

using plugin -- VSCode Table Formatter

.. code-block:: word

   +
   ||Mon|Tue|Wed|Thu|Fri|
   +=
   |田中|(^^)|(xx)|(xx)|('')|(^^)|
   -+
   |鈴木|(^^)|(^^)|('')|(xx)|(^^)|
   +

//Enter command in the command palette (Ctrl-Shift-P or Cmd-Shift-P) with cursor position in table syntax. 
 =>

.. code-block:: word

   +------+------+------+------+------+------+
   |      | Mon  | Tue  | Wed  | Thu  | Fri  |
   +======+======+======+======+======+======+
   | 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
   +------+------+------+------+------+------+
   | 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
   +------+------+------+------+------+------+