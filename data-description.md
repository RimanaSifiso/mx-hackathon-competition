# Data Description

----

Dataset Field Descriptions
- `CustomerID:` unique alphanumeric code that identifies each unique individual (prospect customer) in the dataset. If the same entry appears more than once, it implies that the same person submitted multiple leads (car enquiries).
LeadID: number used to identify each lead (car enquiry) entry.
- `DTLeadCreated:` date and time stamp when the lead (car enquiry) was submitted by the prospect customer.
- `DTLeadAllocated:` date and time stamp when the lead was assigned to a dealership or human sales agent.
- `Dealer: `name of the dealership with which the lead (car enquiry) was associated.
- `LeadType:` website or platform where the lead was submitted (high level / less detailed).
- `LeadSource:` website or platform where the lead was submitted (more detailed).
- `Seek: shows `whether the customer was looking for a New or Used car.
- `InterestMake:` the brand of car the customer was interested in.
- `InterestModel:` the specific car model the customer was interested in.
- `OBSFullName:` full name entered by the person who submitted the lead.
- `OBSEmail:` email address entered by the potential customer when submitting the lead.
- `Domain: `domain part of the email address (after the @ symbol).
- `CellPrefix:` first two digits after the leading ‘0’ in the cellphone number entered by the customer.
CellPhoneNoLength: total number of digits in the cellphone number entered by the customer. A valid South African cellphone number typically has 10 digits (starting with ‘0’).
- `HourOfEnquiry:` hour of the day the lead was submitted (in 24-hour format).
- `DayOfEnquiry:` day of the week when the lead was submitted.
- `InFinanceProcessSystemApp:` indicates whether the finance application is started in the Finance Process System. 0 = No, 1 = Yes.
- `FinanceApplied:` indicates whether a finance application was submitted to the banks. 0 = No, 1 = Yes.
- `FinanceApproved:` indicates whether the finance application was approved by at least one bank. 0 = No, 1 = Yes.
- `VehicleSold:` indicates that the buyer accepted the finance terms from a bank, the vehicle was sold and concluded the purchase process. 0 = No, 1 = Yes. This is the target variable.