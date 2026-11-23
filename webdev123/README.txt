INFIX & POSTFIX UPDATE

Copy these files into your EXISTING Flask project:
  app.py -> project root (replace existing app.py)
  templates/works.html -> templates/works.html
  templates/infix-postfix.html -> templates/infix-postfix.html (new)
  static/style.css -> static/style.css

Included app.js and linked-list.html are unchanged copies; replacement is optional.
Keep your existing other templates and static/assets/background.mp4.
This ZIP is an update package, not a replacement for your complete website.

Run as usual: python app.py
Open http://127.0.0.1:8000/works or http://127.0.0.1:8000/infix-postfix

Converter runs in Python with node-based linked lists for operators and output.
Supports variables, numbers, + - * / ^, and parentheses.
Exponentiation ^ is right-associative. Use (0 - A) for unary minus.
Examples:
(A+B+C)*D -> A B + C + D *
A*(B+C)/D -> A B C + * D /
(A*(B+C^D)) -> A B C D ^ + *
