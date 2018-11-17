Add your answers to the Algorithms exercises here.

a) O(n)

b) O(n^3)

c) O(n)

Exercise II

Given:
_n_ = the number of floors the building has
_f_ = the floor/point at which when an egg is dropped that it breaks upon impact when reaching the ground floor

Visualization:
|ground floor|     egg remains intact < _f_ =< broken egg      |_n_ floor|

To find _f_, with the least amount of eggs dropped, we would need to go to the middle floor of the building and drop the egg from there and see if it breaks when it hits the ground floor. 

If it breaks, we need to try the egg drop from the floor directly below the one we tried it on until we reach a floor that the egg does not break when dropped from that floor. The floor directly on top for that one would be _f_.

If it does not break, we need to try the egg drop from the floor directly above the one we tried it on until we reach a floor that the egg does break when dropped from that floor. The that floor would be _f_.

This would make the Time Complexity O(log n), because we don't need to drop an egg from every floor in the building to get _f_. Instead, we can start at the halfway point and immediately eliminate half of the possibilities by dropping an egg from the halfway point. The test will let us know immidiately which half of the building to consider that may contain _f_ and just keep executing the same test on the succeding floor until we find _f_.

