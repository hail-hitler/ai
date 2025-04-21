% ---------------- DYNAMIC FACTS ----------------
:- dynamic initial_state/1.
:- dynamic goal_state/1.

% ---------------- MAIN ENTRY ----------------
blocks(N, Stack) :-
    length(Stack, N),
    retractall(initial_state(_)),
    retractall(goal_state(_)),
    build_initial(Stack, InitState),
    assertz(initial_state(InitState)),
    reverse(Stack, Rev),
    build_goal(Rev, GoalState),
    assertz(goal_state(GoalState)),
    solve(Plan),
    nl, write('--- Plan ---'), nl,
    print_plan(Plan), !.

% ---------------- ACTION DEFINITIONS ----------------
% Action format: action(Name, Preconditions, AddList, DelList)
action(unstack(X,Y),
    [on(X,Y), clear(X), handempty],
    [holding(X), clear(Y)],
    [on(X,Y), clear(X), handempty]).

action(putdown(X),
    [holding(X)],
    [on(X,table), clear(X), handempty],
    [holding(X)]).

action(pickup(X),
    [on(X,table), clear(X), handempty],
    [holding(X)],
    [on(X,table), clear(X), handempty]).

action(stack(X,Y),
    [holding(X), clear(Y)],
    [on(X,Y), clear(X), handempty],
    [holding(X), clear(Y)]).

% ---------------- LOGIC ENGINE ----------------
solve(Plan) :-
    initial_state(Init),
    goal_state(Goal),
    plan(Init, Goal, [Init], [], Plan).

% Fixed plan/5 predicate with depth limit to prevent infinite loops
plan(State, Goal, _, Plan, Plan) :-
    subset_list(Goal, State).

plan(State, Goal, Visited, Acc, Plan) :-
    length(Acc, L),
    L < 20,  % Depth limit to prevent infinite loops
    action(ActionName, Preconditions, Add, Del),
    subset_list(Preconditions, State),
    apply(ActionName, State, NewState),
    \+ member(NewState, Visited),
    plan(NewState, Goal, [NewState|Visited], [ActionName|Acc], Plan).

apply(ActionName, State, NewState) :-
    action(ActionName, _, Add, Del),
    subtract(State, Del, Temp),
    union(Temp, Add, NewState).

% ---------------- SETUP FUNCTIONS ----------------
% Fixed build_initial to correctly set up the stack and clear status
build_initial([Block], [on(Block, table), clear(Block), handempty]).
build_initial([Block|Rest], State) :-
    Rest = [NextBlock|_],
    build_initial(Rest, RestState),
    subtract(RestState, [clear(NextBlock)], TempState),
    union([on(Block, NextBlock), clear(Block)], TempState, State).

% Fixed build_goal to ensure all blocks have proper clear status
build_goal([Block], [on(Block, table), clear(Block)]).
build_goal([Block, NextBlock|Rest], State) :-
    build_goal([NextBlock|Rest], RestState),
    subtract(RestState, [clear(NextBlock)], TempState),
    union([on(Block, NextBlock), clear(Block)], TempState, State).

% ---------------- UTILITIES ----------------
subset_list([], _).
subset_list([H|T], L) :- member(H, L), subset_list(T, L).

print_plan([]).
print_plan([H|T]) :- print_plan(T), capitalize(H, CH), write(CH), nl.

% Helper to capitalize the action name
capitalize(Term, CapTerm) :-
    Term =.. [Name|Args],
    atom_chars(Name, [First|Rest]),
    upcase_atom(First, CapFirst),
    atom_chars(CapName, [CapFirst|Rest]),
    CapTerm =.. [CapName|Args].