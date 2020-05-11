% Charles Kornoelje | lab13 | cs344 | Calvin University | 05/10/20

% Exercise 13.1

% a.i) 3.2
directlyIn(katarina,olga).
directlyIn(olga,natasha).
directlyIn(natasha,irina).

in(X,Y) :- directlyIn(X,Y).
in(X,Y) :- directlyIn(X,Z), in(Z,Y).

% a.ii) 4.5
   tran(eins,one).
   tran(zwei,two).
   tran(drei,three).
   tran(vier,four).
   tran(fuenf,five).
   tran(sechs,six).
   tran(sieben,seven).
   tran(acht,eight).
   tran(neun,nine).

listtran([],[]).
listtran([X|Tx],[Y|Ty]) :- tran(X,Y), listtran(Tx,Ty).

% Prolog does recursion by trying to solve the base case first, and then move onto the resursive part which will work its way back to the base case. In the list example, I started by defining the base case. And then I thought of how I could translate the first element, and then pass the rest onto another function call. Eventually the tail would be empty, and the base case would be invoked.


% b)
% Yes, prolog implements a version of generalized modus ponens. Modus poenens states that if the conditional statement "if p then q"
% is given, then p holds, and q can be inferred. The variable and instatiation can be shown by the example below. 
% "If X listens to music, then X plays air guitar" and "X listens to music", we can conclude that "X plays air guitar". The variable X
% can be instantiated to mia or jody. 

   listens2Music(mia).
   listens2Music(jody).
   playsAirGuitar(X):-  listens2Music(X).

% ?- playsAirGuitar(X)
% X = mia ; jody
