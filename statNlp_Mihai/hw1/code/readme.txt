
How to run:
1. please unzip and cd to this folder
2. Type “sbt run” and please follow the instructions on screen.


FYI

1. Dependencies can be found in build.sbt (just logging)
2. rest is all classic SCALA file structure. 
3. actual code can be found in /src/main/scala/
4. the input files (Eg brown corpus etc ) can be found in:/src/main/resources/
5. have added case folding (to lowercase) to qn1.1
6. Expected Scala version is 2.11.8 and Java 1.8



Results:

top 10 most frequent words are :
the -> 6386
of -> 2861
and -> 2186
to -> 2144
a -> 2130
in -> 2020
for -> 969
that -> 829
is -> 733
was -> 717


POS top 10 :
nn -> 13160
in -> 10616
at -> 8893
np -> 6866
nns -> 5066
jj -> 4391
cc -> 2664
vbd -> 2524
nn-tl -> 2486
vb -> 2440

word-POS top 10 :
the/at -> 5558
of/in -> 2716
and/cc -> 2115
a/at -> 1988
in/in -> 1828
to/to -> 1222
for/in -> 905
to/in -> 880
The/at -> 775
is/bez -> 729

top 10 most similar words to "home" are :
apartment -> 2.2284981541410005
vacation -> 2.0209083879159992
grocery -> 1.9732463156500009
grandmother -> 1.9136072188709992
porch -> 1.8850352974429998
bedroom -> 1.8471661033730002
clinic -> 1.8275722513049997
mom -> 1.7578488197510003
store -> 1.724475192735
mother -> 1.695437455011001

top 10 most dissimilar words to "home" :
shit -> -1.152438419035001
violation -> -0.9720028775530005
framework -> -0.6195070145559998
mechanism -> -0.6139887267019999
teaspoon -> -0.5902105458839989
treaty -> -0.5765439130040002
violate -> -0.559643511639
sanction -> -0.5544015728880001
imply -> -0.5091616554680003
implement -> -0.5032906530570002
