[Station-Layouts](Game/Station-Layouts)
{: .label .label-blue }

## Warehouse
```mermaid
flowchart TD

Hall <--> Processing <--> Medical

Hall2 <--> Medical

Hall3 <--> Treatment <--> Stasis

Entry <--> Hall(( )) <--> Hall2(( )) <--> Hall3(( )) <--> Hall4(( )) <--> Maintenance

Hall <--> Security <--> Command

Hall2 <--> Lounge["Staff Lounge"]

Hall3 <--> Mess
```