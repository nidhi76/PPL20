flight(madrid,united,toronto,950).
flight(toronto,united,madrid,950).

flight(madrid,iberia,toronto,800).
flight(toronto,iberia,madrid,800).

flight(madrid,aircanada,toronto,800).
flight(toronto,aircanada,madrid,800).

flight(madrid,iberia,barcelona,120).
flight(barcelona,iberia,madrid,120).

flight(madrid,iberia,malaga,50).
flight(malaga,iberia,madrid,50).

flight(paris,united,toulouse,35).
flight(toulouse,united,paris,35).

flight(madrid,iberia,valencia,40).
flight(valencia,iberia,madrid,40).

flight(valencia,iberia,malaga,80).
flight(malaga,iberia,valencia,80).

flight(barcelona,iberia,london,220).
flight(london,iberia,barcelona,220).

flight(london,united,toronto,650).
flight(toronto,united,london,650).

flight(london,aircanada,toronto,500).
flight(toronto,aircanada,london,500).

flight(barcelona,iberia,valencia,110).
flight(valencia,iberia,barcelona,110).

airport(malaga,50,30).
airport(valencia,40,20).
airport(madrid,75,45).
airport(toronto,50,60).
airport(barcelona,40,30).
airport(paris,50,60).
airport(toulouse,40,30).
airport(london,75,80).


cheap(_,_,_,A) :-
      A=<400.

preferred(_,B,_,A) :-
      A=<400; B=aircanada.










