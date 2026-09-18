**PharmShield: Regional Medicine Supply Chain Management Engine**

*What is it?*

A client-side dashboard engineered for real-time pharmaceutical shortage tracking, multi-facility stock redistribution, and clinical formulary resilience. 
Built to comply with GS1 tracking standards, WHO Essential Medicines List (EML) protocols, and FHIR SupplyDelivery resource models.

*Core Capabilities*

- Regional Command Mesh: Visualizes network topology across multiple nodes using differential-privacy aggregation to conceal confidential and raw hospital data from 
competitors while still projecting shortage.

- Human-in-the-Loop Redistribution Solver: Calculates automated First-Expired, First-Out (FEFO) transfers between donor facilities (e.g., St. Jude) and deficit sites (e.g., Hospital Alpha), balancing transit times, cold-chain windows, and safety stock boundaries.

- Master Formulary & FEFO Registry: Dynamic CRUD management for essential medicines with configurable clinical criticality coefficients, storage requirements, and lead times.
