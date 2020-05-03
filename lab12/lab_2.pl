% Charles Kornoelje | lab12 | cs344 | 5/1/20 | Cal Uni

% a.i) 2.1
% 1) true. unify.

% 2) false. does not unify.

% 3) true. unify.

% 4) Bread = bread. unify.

% 5) false. does not unify.

% 6) false. does not unify.

% 7) X = food(bread). unify.

% 8) X = bread. unify.

% 9) X = sausage, Y = bread. unify.

% 10) false. does not unify.

% 11) false. does not unify.

% 12) X = food(X). unify.

% 13) X = food(bread), Y = drink(beer). unify.

% 14) false. does not unify.

% a.ii)
   house_elf(dobby).
   witch(hermione).
   witch('McGonagall').
   witch(rita_skeeter).
   magic(X):-  house_elf(X).
 %  magic(X):-  wizard(X).
   magic(X):-  witch(X).

% NOTE: I removed the rule with wizard because 4/5 resulted in unintended errors otherwise.
% ?-  magic(house_elf).
% false.

% ?-  wizard(harry).
% ERROR: Undefined prodecure: wizard/1 (I would argue that this means false becaus Prolog cannot assert it is true based on the KB).

% ?-  magic(wizard).
% false.

% ?-  magic(’McGonagall’).
% true.

% ?-  magic(Hermione).
% Hermione = dobby ;
% Hermione = hermione ;
% Hermione = 'McGonagall' ;
% Hermione = rita_skeeter.

%     --------------------------------------------------------------
%     |                     ?- magic(Hermione)                     |
%     --------------------------------------------------------------
%                 /      (If included in KB)           \
% Hermione = _G1 /               | Hermione = _G1       \ Hermione = _G1
%               /                |                       \
% ---------------------  ------------------        ---------------------------------------
% | ?- house_elf(_G1) |  | ?- wizard(_G1) |        |            ?- witch(_G1)            |
% ---------------------  ------------------        ---------------------------------------
%             |                  |                     /     |                     \
% _G1 = dobby |                  |     _G1 = hermione /      | _G1 = 'McGonagall'   \ _G1 = rita_skeeter
%             |                  |                   /       |                       \
%           -----                X Error          -----    -----                    -----
%           |   |                                 |   |    |   |                    |   |
%           -----                                 -----    -----                    -----
%
% Sketch adapted from: https://github.com/dragonwasrobot/learn-prolog-now-exercises/blob/master/chapter-02/exercises.pl


% Prolog does unification following four main clauses. It will unify two terms if they are constants and the same atom. If one of the terms is a variable, then the terms will unify and the variable will be instantiated to the other term. If the terms are both complex, then they unify if and only if they have the same functor and arity, their corresponding args unify, and variable instantiations are compatible. Prolog will give different answers for infinite terms based on the implementation. Prolog will reason by performing a proof search on a knowledge base to see if a query is satisfied. If you aren't getting the results you'd expect, you can try removing rules in your KB that reference an undefined prodecure or add that undefined prodecure. You could also change your version of Prolog to get different answers for infinite problems. Or declare that all unknown prediacates should fail or declare dynamic predicates in specific situations so achieve intended behavior.  

