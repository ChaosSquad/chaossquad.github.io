## General
Conquest is the default game mode of the CastleConquest 2 project.
It is a further development of the game mode from the old "BurgConquest" (official name of CastleConquest 1)

It is about capturing and holding flags.
If the attackers manage to hold enough flags for a certain time, they win, otherwise the defenders win.

## Summary
There are two teams: attackers and defenders.
The attackers start in a dedicated attacker spawn. The defenders, on the other hand, start in the castle.

There are several flags in the castle. These belong to the defenders at the start.

The aim of the attackers is to hold more than half of all flags for 5 minutes. If they succeed, they win the game.

However, the attackers have a time limit of 30 minutes. If they do not manage to fulfill this condition by then, the defenders win.

## Rules
#### Teams
- Defenders: Have to prevent the attackers from capturing the castle
- Attackers: Have to capture the castle

#### Timers
There are two mutually exclusive times.

The game time counting down when the attackers don't have the required amount of flags to win.
When the game time has expired, the attackers lose and the defenders win.
The game time is paused as long as the flag timer is active.

The flag timer is counting down then the attackers have the required amount of flags to win
When the flag timer has expired, the attackers win and the defenders lose.
The flag timer is counting up when until it has reached 5 minutes when it is not active.

If one of the timers expires, an overtime can be triggered under certain circumstances. If the overtime is active, the corresponding timer is stopped until the overtime has ended. See section Overtime for more information.

#### Required flags
Required flags for the attackers: More than half of all flags.

The default map has 6 flags. Therefore, the attackers need to hold at least 4 flags to meet the required flags amount.

#### Overtime
Overtime can be triggered if a team is currently capturing so many flags that the timer condition for the team could still be fulfilled if nothing changes in the current situation.

For example, if the attackers have 3/6 flags and are currently capturing 1 flag and the game time expires while they are still capturing that flag, the game time will pause so that the attackers can finish capturing this flag, which will enable the flag timer.

Another example, if the attackers currently have all 6/6 flags but the defenders are currently capturing 2 flags at the same time and the flag timer expires, the flag timer will pause so that the defenders can finish capturing both flags which would stop the flag timer.

For the overtime system, "a team is currently capturing a flag" when the team has any progress on it (States: Capturing, Uncapturing, IDLE with progress).

#### Spawning
Attackers will always spawn in the attacker spawn.

Defenders can spawn in two different locations. Either in the castle or in the outposts near the villages outside.
When the attackers have half of the flags or more (one less than the win condition), they are forced to spawn outside the castle. If not, they can decide if they want to spawn in the castle or outside using the `/changerespawn [inside|outside]` command.

#### Money
Players can earn money by killing players, capturing flags or supporting the team.
There is also a balancer system which supports players by giving them money when they are to weak.

Money can be used to purchase equipment and tools to break into or to repair the castle.
