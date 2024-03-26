[Station-Layouts](Game/Station-Layouts)
{: .label .label-blue }

## Military Base
```mermaid
graph TD

Checkpoint <--> Parade

Checkpoint <--> Watchtower  <--> Security <--> Bunks <--> Maintenance <--> Command <--> Medical <--> Checkpoint

Watchtower <--> Parade

Security <--> Parade

Bunks <--> Parade

Maintenance <--> Parade

Command <--> Parade

Medical <--> Parade
```
