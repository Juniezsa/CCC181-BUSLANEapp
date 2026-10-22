# BUSLANE

A queue management system designed for Bus Passenger and Staff. It manages passenger queue, priority seats, seat and passenger counts, and it shows if the bus is still waiting for passengers, especially during peak seasons. This eliminates long waits for the next bus, crowding at the entrance, and safety risks for passengers by letting passengers prebook their seats, track their place in the line, and see which bus they can board. The Terminal Staff (Ticket Clerk, Conductor, Dispatcher) can manage the passengers efficiently during peak hours.They can check whether each passenger meant to board is already on-board and whether any passenger has left their seats, and manage no-shows and priority passengers to keep boarding fast and orderly. 

## Setting
- **Setting:** Bus terminal, especially peak seasons (holidays, long weekends, school breaks)
- **Problem Solved:** Long waits, Line-cutting, Entrance crowding, and safety risks caused by manual queue system with no way to track seats, passengers, or boarding order.

## How to run BUSLANE

### 1. Create and Activate Virtual Environment

```bash
# create 
python -m venv .venv

# activate
# Windows
.venv\Scripts\activate  
# macOS/Linux
source .venv/bin/activate       
```

### 2. Install the required packages
```bash
pip install -r requirements.txt
```

### 3. Run the app in debug mode
```bash
flask --app app run --debug
```

### 4. Open Browser
```
 http://127.0.0.1:5000
```