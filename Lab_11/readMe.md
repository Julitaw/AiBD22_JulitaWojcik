Zadanie 1<br />
Ile rekordów znajduje się w tabeli nyc_streets?<br />

SELECT COUNT(*)
FROM nyc_streets

Odp.
	19091

Zadanie 2<br />
Ile ulic w Nowym Jorku ma nazwy zaczynające się na „B”, „Q” i „M”?<br />


SELECT COUNT(name)
FROM nyc_streets
WHERE name LIKE 'B%' OR name LIKE 'Q%' OR name LIKE 'M%'


Odp.	2102


Zadanie 3<br />
Jaka jest populacja miasta Nowy Jork?<br />


SELECT SUM(popn_total)
FROM nyc_census_blocks


Odp.   8175032


Zadanie 4<br />
Jaka jest populacja Bronxu, Manhattanu i Queens?<br />

SELECT boroname, SUM(popn_total)
FROM nyc_census_blocks
WHERE boroname  like  '%The Bronx' OR  boroname  like  '%Manhattan' OR  boroname  like  '%Queens'
GROUP BY boroname

Odp.

boroname	     sum
0	Queens	    2230621
1	The Bronx	1385108
2	Manhattan	1585873


Zadanie 5<br />
Ile dzielnic ("neighborhoods") znajduje się w każdej gminie (borough)?<br />


SELECT boroname, COUNT(*)
FROM nyc_neighborhoods
GROUP BY boroname

Odp.
boroname	  count
0	Queens	        30
1	Brooklyn	    23
2	Staten Island	24
3	The Bronx	    24
4	Manhattan	    28