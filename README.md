 Projekti idee: “Sundöö” – konsoolimäng ellujäämise simulaatorina
Loome konsoolipõhise ellujäämismängu, mis põhineb fiktiivsel stsenaariumil „Sundöö“ (“The Purge”), kus mängija peab tegema strateegilisi otsuseid, et ellu jääda piiratud aja jooksul. Mäng arvestab ressursse (nt toit, energia), riske (nt ohtlikud sündmused) ja aega. Arendust teostatakse Scrum-metoodika järgi iteratsioonide kaupa.

🌀 Scrum-metoodika kasutamine
Töö jagatakse 3 sprinti.

Iga sprindi lõpus toimuvad arutelud: kas eesmärgid on täidetud, mida saaks täiustada?

Iga iteratsiooniga lisatakse mängule uusi funktsioone.

🧩 Sprint 1: Põhistruktuuri ja algandmete loomine
🎯 Eesmärk:
Luua mängu põhiline struktuur koos järgmiste komponentidega:

Mängijal on toiduvarud, energiatase, tervis ja mänguaeg.

Iga samm kulutab ressursse; eesmärk on ellu jääda kuni aja lõpuni.

🧑‍💻 Koodi kirjutamine:
Klass Player: haldab mängija andmeid

Mängu alguses: algväärtused määratud (nt tervis 100, toit 3, aeg 10 käiku)

💬 Arutelupunktid:
Kas baasstruktuur on piisavalt paindlik lisafunktsioonide jaoks?

Kas ressursihaldus tekitab piisavalt strateegiat?

Kas lisada juba siinkohal mängijale valikuid või hoida lihtsana?

🔥 Sprint 2: Ohtude ja valikute lisamine
🎯 Eesmärk:
Tuua mängu põnevus – juhuslikud sündmused ja valikud, mis mõjutavad mängijat.

🧑‍💻 Koodi kirjutamine:
Funktsioon Event():

Näiteks: „Sind ründab röövel – kaotad 20 tervist“

Või: „Leidsid toidukoti – saad 1 toitu juurde“

Mängija saab iga käigu lõpus valida:

Puhka – taastad energiat, kuid kulub toit

Edasi liikuda – riskantsem, võib juhtuda midagi

Otsi toitu – võib õnnestuda või ebaõnnestuda

💬 Arutelupunktid:
Kas sündmused peaksid olema rohkem negatiivsed või tasakaalus?

Kas valida ainult üks tegevus või kombineerida?

Kas sündmustel peaks olema tõenäosus (nt 30% haavata, 20% leida toitu)?

⏳ Sprint 3: Mängu pikendamine ja valikute täiustamine
🎯 Eesmärk:
Lisada mõõdetav mänguaeg ja lõpetingimused, rohkem strateegilisi tegevusi.

🧑‍💻 Koodi kirjutamine:
Loendur turnsLeft: iga käik vähendab aega

Mäng lõpeb kui turnsLeft == 0 või player.health <= 0

Lisafunktsioon: Varude kogumine, Peitmine, Relvade leidmine

💬 Arutelupunktid:
Kuidas hoida mängu pinget? Kas mänguaeg piisav?

Kas tegevustel võiks olla kombinatsioone, nt „puhka ja peitu“?

Milliseid lisategevusi soovitaks meeskond?

🧠 Reflektsioon Scrum-praktikate kohta
Sprintide lõpus tehtud arutelud aitasid suunata fookust ja lisada väärtuslikke elemente mängule.

Iga iteratsioon oli loogiline samm edasi, mitte „kõik korraga“.

Meeskonna tagasiside mängis olulist rolli mängu mitmekesistamisel.

🧪 Kokkuvõte
„Sundöö“ konsoolimängu arendus on hea näide, kuidas Scrum võimaldab samm-sammult arendada mängu, millel on:

Järjest kasvav funktsionaalsus

Otsustel põhinev mängumehaanika

Iteratiivne täiustamine ja meeskonna koostöö
