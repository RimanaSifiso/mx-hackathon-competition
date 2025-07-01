# Ideas on data exploration on data and analysis

-----

**`CustomerID and LeadID`**


Between CustomerID and LeadID, we it is possible that the same customer may come back again, but now in a different lead, perhaps in a different dealership. 

_Is the CustomerID **consistent**?_ Consistent in a sense that each customer is given a unique ID, and ID's are not generated on the fly, thus potentially leading to the same person having different IDs?

If so, then we can investigate: 

1) Which customers have two or more leads?
2) Are these customers likely to buy the vehicle?
3) Are customers who have two or more leads more likely to buy than those with one lead only?

**`DTLeadCreated` and `DTLeadAllocated` **

The date the lead was created is important, as it may capture some time series information regarding customer sentiments towards a product

If date the lead allocated is to be used, perhaps we can measure the time between when the lead was created, and when the lead was alloacted, it may have some relationship with whether the prospect customer ends buying the car or not. 

Assumption, the more the time it takes for the lead to be allocated to the sales agent, the more likey is the prospect customer is to lose intereset in buying the car, this could be that the prospect customer has found other deals that were interested and were responded to in time.

**`OBSFullName`**

Maybe here we can detect whether the name entered is proper or not, perhaps those that enter proper names (without symbols, and perhaps and name and a surname) are more likely to buy, since they are more likely to be serious about what they are doing. (Not a good way to put it, but yeah.)

- proper name supplied: bool
- full names: bool 

**`OBSEmail`**
Same here, we check proper emails, and whether or not email was provided

- email type: `gmail` 0 = not gmail, 1 = gmail
- proper email supplied: bool


**`Dealer`**

- Extract dealer group (e.g., Motus, Renault, ...)
- Extract dealer subgroup (e.g., Motus Toyota, ...)
- Extract dealer city (e.g., Germiston, Kempton Park, ...) This, however, may lead to bias models. For instance, suppose cities situated in high class such as Bryanston lead to more car sales than others, it may be biased to such cities, and sales agents may in fact end up minding more prospect customers from such cities than others, thus leading to more biases
- Extract ...?

Alternatively, use bag of n-words, or onehot word embeddings

**`LeadSource`**









