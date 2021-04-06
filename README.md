# MatEncrypto
Lijst me ASCII tekens:
[\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f]

Dit is de lijst van karakters (de eerste 33 karakters zijn echter niet print-baar), die deze software mogelijk zou kunnen encrypten en decrypten (versleutelen en ont-sleutelen). Ieder karakter in deze lijst heeft een rangschikking waarde, zo begin je met x00 dat is in de rangschikking de eerste waarde in de lijst (bij het programmeren is de eerste waarde in een lijst 0, de tweede 1, de derde 3 etc.) en bijvoorbeeld ‘A’ geeft als nummer in de lijst, waarde 68. De code splitst tekens in matrices van 4 rijen en een x aantal kolommen. Stel we geven mijn software als input ‘ABCDEF’ dan krijgen we hierbij de lijst [65, 66, 67, 68, 69] dit zetten we om in de Matrix 
![image](https://user-images.githubusercontent.com/55809308/113766111-5b81a180-971d-11eb-88c8-606c97190aaa.png)


Voor de overige plekken gebruik ik een ‘0’, deze wordt door de code gezien als een lege plek.

Bij deze encryptie gebruik ik een key (sleutel) die een afmeting heeft van 4x4. De key moet 4 kolommen en rijen hebben omdat het aantal rijen van 4. In het voorbeeld 'ABCDEF' gebruik ik de key: 
![image](https://user-images.githubusercontent.com/55809308/113766136-62a8af80-971d-11eb-9ed4-a3319f10ffa1.png)

Voor de versleutelde matrix uit het voorbeeld krijgen we V = K*M
Dit geeft met de code
![image](https://user-images.githubusercontent.com/55809308/113766183-6e947180-971d-11eb-9f17-9d4cea9ba104.png)


Dan zul je zien dat alle waardes anders zijn in dit voorbeeld. De nullen zijn niet meer dezelfde waarde als in matrix M, het ziet er op het eerste oog "random" uit. Wanneer je enorme berichten zal versleutelen zullen er wel overlapping komen. 

Om het bericht terug te krijgen uit de versleutelde matrix doen we M = K^-1 * V. K^-1 is de inverse van matrix K.
