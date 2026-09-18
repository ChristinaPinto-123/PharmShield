**PharmShield: Regional Medicine Supply Chain Management Engine**

*What is it?*

A client-side dashboard engineered for real-time pharmaceutical shortage tracking, multi-facility stock redistribution, and clinical formulary resilience. 
Built to comply with GS1 tracking standards, WHO Essential Medicines List (EML) protocols, and FHIR SupplyDelivery resource models.

---

*Core Capabilities*

- Regional Command Mesh: Visualizes network topology across multiple nodes using differential-privacy aggregation to conceal confidential and raw hospital data from 
competitors while still projecting shortage.

- Human-in-the-Loop Redistribution Solver: Calculates automated First-Expired, First-Out (FEFO) transfers between donor facilities (e.g., St. Jude) and deficit sites (e.g., Hospital Alpha), balancing transit times, cold-chain windows, and safety stock boundaries.

- Master Formulary & FEFO Registry: Dynamic CRUD management for essential medicines with configurable clinical criticality coefficients, storage requirements, and lead times.
---
*System Workspaces*

1. Regional Command 
- Metric Strips: Active cluster risk ratios, upstream supply disruption alerts, chronic SKU count, and 30-day stockout mitigation rates.

- Network Mesh Canvas: Interactive node topology showing real-time connectivity between the central buffer hub and regional clinical facilities.

- Incident Feed: Filterable split view sorting acute localized imbalances from chronic systemic market deficits.

  <img width="1890" height="847" alt="image" src="https://github.com/user-attachments/assets/ab7d30e2-bc9d-41de-a229-dc9652cdffed" />




2. Facility Drill-Down 
- Operational Telemetry: Real-time calculation of usable units, reserved buffer, average daily consumption (ADC), and Days of Stock (DoS).

- Demand Shock Simulator: Dynamic slider modeling consumption spikes (e.g., epidemic surges, mass casualty incidents) that instantly recalculates stockout probabilities, and countdown timers.

- FEFO Batch Inspector: Lot-level expiry tracking color-coded by remaining shelf life.

  <img width="1890" height="847" alt="image" src="https://github.com/user-attachments/assets/03bc6df5-8fd1-4219-841a-d5096634ef5a" />

  
3. Formulary & Inventory Management 
- Formulary CRUD: Add, modify, or decommission SKUs with therapeutic classes, storage constraints, and criticality weights.

- Inventory Adjustment Journal: GS1-compliant journal entries for inward receipts, consumption spikes, quarantine holds, and audit reconciliations.

<img width="1890" height="577" alt="image" src="https://github.com/user-attachments/assets/4250e5c3-59de-46b7-9795-9057ea261778" />

4. Intervention Workspace
- Interactive Transfer Rebalancer: Multi-variable slider adjusting transfer payloads between donor and recipient facilities while continuously enforcing safety-stock floors.

- Pooled Procurement Desk: Demand consolidation interface routing tenders to central medical stores.

<img width="1890" height="847" alt="image" src="https://github.com/user-attachments/assets/2b5720af-f8ec-4bde-b8a6-d147edb0d603" />

  5. Audit & Compliance Trail 
- Cryptographic timeline capturing actor identity, system daemon operations, model divergence telemetry, and transfer hashes with filterable CSV export.

  <img width="1890" height="445" alt="image" src="https://github.com/user-attachments/assets/171af8c8-eca1-4497-85ec-7014ceec75c9" />




  

