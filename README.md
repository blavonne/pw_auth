# pwauth
PW auth through python + selenium, promo activation and gifts sending via java script
1. project directory should include file passwords.txt file formatted as:

* (line1) login
* (line2) password
* (line3) login
* (line4) password
* etc.

2. project directory should include file pins.txt file formatted as:

* PROMO123
* PROMO456

2. this code makes auth on Perfect World (ru official) per Selenium during reading login and password from passwords.txt
3. then it activates promos from pins.txt
4. then it activates script to send all gifts to personages reproduced in variable allowed in pinsAndGifts.js
5. it also creates log formatted as `^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3})\s*(\S*)\s*-\s*(\S*)\s*-\s*(.*)$`
