[Station-Layouts](Game/Station-Layouts)
{: .label .label-blue }

## Mansion
```mermaid
graph LR    

subgraph H1[House F1]

  

Entry <--> Hall

Hall <--> Kitchen

Hall <--> SQ[Servants Quarters]

SQ <--> Kitchen

Hall <--> DR[Dining Room]

Hall <--> TR[Trophy Room]

Hall <--> Basement

DR <--> TR

Hall <--> ER[Entertaining Room]

  

end  

Hall <--> Balcony

  

subgraph H2[House F2]

Balcony <--> RR[Reading Room]

Balcony <--> MB[Master Bedroom]

Balcony <--> SR[Sun Room]

Balcony <--> SPR[Spare Room]

end
```