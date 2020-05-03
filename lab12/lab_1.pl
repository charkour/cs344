% Charles Kornoelje | lab12 | cs344 | 5/1/20 | Cal Uni

% Exercise 12.1

% a.i)
% Butch is a killer.
killer(butch). 
% it is a fact. person and procedure

% Mia and Marsellus are married.
married(mia, marsellus). 
% the two are married, fact.

% Zed is dead.
dead(zed).
% fact. 

% Marsellus kills everyone who gives Mia a footmassage.
kills(marsellus, X) :- givesFootmassage(X, mia).
% Everyone is represented by the X, X giving mia a foot massages
% implies that marzellus will kill X. Rule.

% Mia loves everyone who is a good dancer.
loves(mia, X) :- goodDancer(X).
% A rule also involing everyone.

% Jules eats anything that is nutritious or tasty.
eats(jules, X) :- nutritious(X); tasty(X).
% This rule includes an or statement so I used a semicolon.
% If anything is nutritious or tastey, then it implies Jules will eat it.

% a.ii)
   wizard(ron).
   hasWand(harry).
   quidditchPlayer(harry).
   wizard(X):-  hasBroom(X),  hasWand(X).
   hasBroom(X):-  quidditchPlayer(X).

% wizard(ron).
% true. given

% witch(ron).
% Error: undefined prodecure: witch/1.
% witch is not defined

% wizard(hermione).
% false.
% Info about hermione is not present so no inference can be made. 

% witch(hermione).
% Error: undefined prodecure: witch/1.
% witch is not defined

% wizard(harry).
% true.
% harry is a player so that implies he has a broom
% it is a fact he has a wand; therefore, he is a wizard.

% wizard(Y).
% Y = ron ;
% Y = harry.
% both are wizards.

% witch(Y).
% Error: undefined prodecure: witch/1.
% Impossible to know if anyone is a witch because the prodecure is not defined.
% so nobody is a witch.

% prolog comes up with the answers by assessing the knowledge base
% when the user asks a question.
