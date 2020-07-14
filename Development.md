# iSIM Development Notes 

*Composed by Phu Tran @ ATMRI (phutran@ntu.edu.sg)*

## 1. iSIM App Overview

iSIM is made of a Python backend, a web-based frontend, and a SQLite ORM database. Communications between the backend and the frontend include HTTP Request and WebSocket using the Tornado web framework.

The backend does the followings:
* Interact with the database
* Perform all the logics of air traffic simulation
* Interact with ATM algorithms built by CDR-Team@ATMRI

The frontend provides the followings:
* GUI for the preparation of scenarios data for simulation
* GUI for real-time air traffic simulation
* GUI for human-in-the-loop experiments involving Air Traffic Controllers (ATCO)

## 2. Database
## 3. Backend
### 1. BADA Aircraft  
#### Completed  
- Defined phases: inital, departure ground run, take off, initial climb, climb, cruise, descent, approach, landing, arrival ground run
- Vstall, fuel flow, mass      
#### TODO: 
- Thrust, Drag, Lift computation
- Vertical speed assignment
- Main stepping function to move the aircraft

### Flight plan
#### TODO:


## 4. Frontend