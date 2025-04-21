% Define a predicate that solves the Tower of Hanoi problem
hanoi(N) :-
    move(N, left, center, right).

% Define a predicate that prints the moves
move(0, _, _, _) :- !.
move(N, A, B, C) :-
    M is N - 1,
    move(M, A, C, B),
    format('Move disk ~w from ~w to ~w~n', [N, A, C]),
    move(M, B, A, C).
