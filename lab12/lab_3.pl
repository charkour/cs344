% Charles Kornoelje | lab12 | cs344 | 5/3/20 | Cal Uni

% Implements the "Burn the Witch" sketch from Money Python's The Holy Grail.
% She is indeed a witch.


witch(X) :- burns(X), female(X).
burns(X) :- wooden(X).
wooden(X) :- floats(X).
floats(X) :- sameweight(duck, X).
sameweight(duck, woman).
female(woman).

% ?- witch(woman). --> true.



% Referenced this when I was stuck. Turns out a just spelled 'burns' two different ways...
% https://github.com/Risto-Stevcev/prolog-monty-python/blob/master/monty-python.pl
