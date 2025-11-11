# Assignment 3 – Django and Energy (Group 26 – CRN 45894)

## Part 1 – Cash Register System

**Description:**  
Designed and analyzed the architecture for a **Cash Register System** using the provided requirements document.  
The goal was to identify the appropriate **reference architecture** and outline how it meets the system’s needs.

**Key Decisions:**  
- Selected **Rich Client Application Architecture** as the most suitable choice.  
- This architecture allows the system to:  
  - Operate **offline or intermittently connected**, ensuring continued functionality without constant internet access.  
  - Provide a **fast, responsive interface** for immediate transactions.  
  - Interact directly with **local hardware** (printers, scanners, card readers).  
  - Synchronize with back-office servers when a connection is available.  
- The design leverages local data storage for reliability and performance while supporting synchronization for sales uploads and catalog updates.

**Outcome:**  
A well-structured rich-client model that balances **availability**, **performance**, and **maintainability**, aligning with retail point-of-sale requirements.

---

## Part 2 – Energy Efficiency (Quality Attribute Scenario)

**Description:**  
Defined a concrete **Energy Efficiency Quality Attribute Scenario** and identified relevant **architectural tactics** for a **mobile health-tracking application**.  
The analysis followed the *Energy Efficiency General Scenario* format and was submitted to Canvas as a PDF.

**Deliverables:**  
- Completed **Energy Efficiency Quality Attribute Table** (Source, Stimulus, Artifacts, Environment, Response, Response Measures).  
- Explained four key **tactics**:  
  1. **Adaptive Sampling / Duty Cycling**  
  2. **Batching and Deferred Execution**  
  3. **Energy-Aware Networking**  
  4. **Energy-Efficient UI Rendering**  
- Linked tactics to design concepts from *Software Architecture in Practice* and the *Design Concepts Catalog*.  
- Submitted the formatted document as a **PDF on Canvas**.



## Contributors
**Pranav Ashok** – Part 1 : Cash Register System  
**Ivan Arudpiragasam** – Part 2 : Energy Efficiency  
**Ahmad Amaree** – Documentation & Review