# Proposed Application: BUSLANE

| | |
|---|---|
| **Student name** | Bacus, Juniezsa Cassandra C. |
| **Section** | CS3A |
| **GitHub username** | fried.ShangHai |
| **Date submitted** | 2026-10-26 |

---

## 1. Problem Statement

### 1.1 Background

> Bus terminal crowding happens at provincial bus terminals, especially during peak seasons like holidays, school breaks, and long weekends. Passengers wait for hours without knowing when the next bus will arrive or whether they can board it, and when a bus finally pulls in, they rush the entrance to get a seat, only to find none left or to see someone cut in line. This affects commuters and students going home, and also the conductors and terminal staff who must manage the crowd, and one misstep or a flare of anger can turn it into a safety risk. I came across this problem when a friend and blockmate experienced it every time they went home, and when we observed students on the MSU-IIT Cats page asking during long weekends and school breaks whether the terminal is crowded, has long lines, or has a bus available.

### 1.2 Evidence from research


| Method | Who / where | Key finding |
|---|---|---|
| Interview | 3rd year Computer Science Student; Boarder | During peak season (school breaks), she has to spread her arms at some point during boarding so no one will cut in line.  |
| Interview | 3rd year Information Technology Student | At some point during regular bus trip with multiple stops, the bus becomes crowded and some passengers have to stand in the aisle. |
| Observation | MSU-IIT Cats FB page during Christmas Break | Students who have to go to their hometown ask in the page if the line is still long or if the bus terminal is packed. Some complain that they had been waiting for hours in the line |

### 1.3 Point-of-view (POV) statement

> **Commuters** (student boarders, employees assigned away from home, people on vacation) going home during peak season need a way to secure a place in the bus line and know when they will board, before arriving at the terminal, because waiting for hours without knowing if a seat is available forces them to stand in a crowd, guard their spot, and rush the entrance, which makes them anxious and creates a safety risk for everyone.

### 1.4 "How might we…?" question

> How might we let commuters join the bus line remotely and track their queue position in real time so that they can wait anywhere, such as at their boarding house, and head to the terminal only when their boarding time is near, allowing conductors to call passengers in order with guaranteed presence and a fair, organized line?

### 1.5 Self-check

- [x] Names a real user group
- [x] States a need, not a feature
- [x] Rests on an insight from research
- [x] Is narrow enough to act on and open enough to allow different ideas

---

## 2. Target-User Profile

### 2.1 Primary persona

| | |
|---|---|
| **Name, age** | Gabriel Reyes, 22 |
| **Role / background** | 4th year College student; Is a student Boarder for 4 years and always goes back to his hometown when there is a school break or long weekend |
| **Goals** | 1. Secure a place in the bus line while still at his boarding house.<br>2. Know whether he is next to board and at what time.<br>3. Board and get a seat without having to guard his place in line. |
| **Frustrations / pain points** | 1. He can't predict when the next bus will arrive.<br>2. He waits hours at the terminal without knowing if he can board.<br>3. When a bus arrives, people crowd the entrance ("siksikan") and cut in line. |
| **Context of use** | Mid-range Android phone on mobile data or public Wi-Fi. He uses the app while packing and cleaning his boarding house, on the way to the terminal, and while waiting at the terminal. Peak days are school breaks and long weekends, often early in the morning (e.g., 3 AM). |
| **Accessibility considerations** | Slow or unstable signal in some parts of the city. He carries 2-3 large bags, so he needs large tap targets and quick, one-handed actions. High tech comfort, but the screens should still be simple. |
| **Current workaround** | He arrives at the terminal hours early, stands in line, and at some point has to spread his arms to keep others from cutting in. He also asks on the MSU-IIT Cats page whether the terminal is crowded. |

### 2.2 User groups and stakeholders

| Group | Who | Relationship to the app |
|---|---|---|
| Primary users | Commuters going home during peak season: student boarders, employees assigned away from home, and people on vacation | Use the app to join the bus line remotely, track their position, and receive boarding notifications. |
| Secondary users | Bus conductors and terminal staff or dispatchers | Use the app to see who is waiting, call passengers in order, mark them as `Boarded` or `No Show`, and update bus status (arriving, boarding, en route). |
| Stakeholders | Bus companies and terminal operators; local government or the transport regulator (e.g., LTFRB); drivers | Approve and run the system, are affected by crowding and safety at the terminal, and may need queue and boarding data for reports. |

### 2.3 Organizational needs

- **Safety and order:** Reduce crowding and line-cutting at the entrance, especially during peak seasons, so the terminal is safer for passengers and staff.
- **Compliance with the Data Privacy Act of 2012 (RA 10173):** Collect only the minimum personal data needed (e.g., name and contact number), get consent, store data securely, and delete or anonymize it after the trip. Priority passengers' ID details should be checked in person and not stored in the app.
- **Fit with existing operations:** The system should work alongside current practices (paper tickets, fare collection on the bus, a conductor crew assigned to each bus) and not require new hardware or heavy training. Conductors should be able to use it with a few taps while handing out tickets.
- **Low cost:** Use a simple, low-cost web app that works on basic phones and weak connections, since small terminals may not have a big budget.
- **Reporting:** Give operators simple counts of passengers per bus, boarded vs. no-show, and peak times, so they can plan how many buses to dispatch.
- **Where user and organizational needs may conflict:**
  - Passengers want guaranteed seats, but operators can't promise this when a bus is nearly full or priority passengers join. The app should show remaining seats and warn passengers early, with the next bus offered as an option.
  - Passengers want flexibility to come late, but operators need buses to leave on time. The `No Show` timer (about 20-30 minutes, with repeated notifications) balances both.
  - Operators want data, but passengers want privacy. Collect only what's needed and explain why.

---

## 3. Proposed Application

### 3.1 Concept

> BUSLANE is a mobile web app that lets passengers join the line for an incoming bus from wherever they are. Gabriel opens it at his boarding house, picks the next available bus (like a `Non-Stop Aircon Bus`), and gets a ticket number, his position in line, and an estimated boarding time. The app sends notifications ("30 minutes before boarding," "20 minutes before boarding") so he can finish packing and arrive at the terminal on time. When the bus arrives, it tells him which boarding area to go to. On the other side, the conductor uses the app to call passengers in order, mark them as `Boarded` or `No Show`, and update the bus status (arriving, boarding, en route).

### 3.2 Value proposition

> For **commuters going home during peak season** who **need a way to secure a place in the bus line and know when they will board**, **BUSLANE** is a **mobile web app for queueing and boarding** that **lets them join the line remotely, track their position in real time, and be notified when it is their turn**. Unlike **standing in line at the terminal for hours or asking Facebook pages if the terminal is crowded**, it **gives each passenger a fair, numbered place in line and tells them exactly when and where to board.**

### 3.3 Value Proposition Canvas

| User side | Product side |
|---|---|
| **Jobs:** Get home during school breaks and long weekends; get a seat on the next available bus; carry 2-3 large bags to the terminal; avoid being cut in line | **Features (MVP):** Remote queue joining with a ticket number; live queue position and "next to board" status; estimated boarding time; conductor boarding list with a one-tap `Boarded` button.<br>**Later versions:** Timed notifications and boarding-area alerts; `No Show` handling; bus status updates; priority lane; remaining-seats display and cancel spot |
| **Pains:** Can't predict when the next bus arrives; waits hours without knowing if he can board; crowding and line-cutting when the bus pulls in; has to guard his place with his arms; weak signal in some areas | **Pain relievers (MVP):** Estimated boarding time and "next to board" status; fixed ticket numbers so no one can cut in; lightweight pages that work on weak connections.<br>**Later versions:** Notifications so he doesn't have to stand and wait |
| **Gains:** Arrives at the terminal only when it's almost his turn; boards calmly with a seat; feels the line is fair; less stress traveling with heavy bags | **Gain creators (MVP):** Live position and estimated time so he knows when to leave; large, easy-to-tap buttons.<br>**Later versions:** Timed reminders ("30 / 20 minutes before boarding"); boarding-area instructions; separate priority and regular tickets; remaining-seats display |

### 3.4 Existing applications (from your application analysis)

| Existing app | What it does well | Where it falls short | How your app differs |
|---|---|---|---|
| Facebook pages and group chats (e.g., MSU-IIT Cats page) | Free, familiar, and quick for asking whether the terminal is crowded | Answers are unofficial, can be outdated, and don't reserve a place or give a boarding time | BUSLANE gives a real ticket, a live queue position, and an official boarding time |
| Online bus booking platforms (e.g., BusX, bus company websites) | Let passengers book a seat in advance with a fixed schedule | Built for scheduled reservations, not for managing the walk-in line and boarding order at a terminal; may require payment and fixed trips | BUSLANE manages the day-of queue, notifications, and conductor boarding, including `No Show` handling |
| Paper tickets and manual lines at the terminal | Simple, no phone needed | Passengers must be physically present for hours, and line-cutting and crowding are common | BUSLANE lets passengers wait anywhere and keeps the order fair |

### 3.5 Technology choice

**Options considered:** 
* Option A: Progressive Web App (PWA) built with Flask, Jinja2, Bootstrap 5, and vanilla JavaScript.
* Option B: Native Mobile App (Flutter or Android Kotlin) with Firebase backend.
* Option C: Single Page Application (React / Next.js) with Node.js / Express REST API.

**Weighted decision matrix** (scores 1-5, higher is better):

| Option | Solves the problem ×3 | Team skills ×2 | Cost ×2 | Privacy ×2 | Time to MVP ×1 | Total /50 |
|---|---|---|---|---|---|---|
| A: PWA | 5 × 3 = 15 | 4 × 2 = 8 | 5 × 2 = 10 | 4 × 2 = 8 | 5 × 1 = 5 | **46** |
| B: Native app | 5 × 3 = 15 | 2 × 2 = 4 | 3 × 2 = 6 | 3 × 2 = 6 | 2 × 1 = 2 | 33 |
| C: SPA | 5 × 3 = 15 | 3 × 2 = 6 | 4 × 2 = 8 | 4 × 2 = 8 | 3 × 1 = 3 | 40 |

**Chosen technology and rationale:** A PWA. It runs in Chrome on Gabriel's mid-range Android phone with nothing to install, which suits peak-day crowds and a small terminal budget. It supports push notifications for the "30 / 20 minutes before boarding" reminders and can cache his ticket and queue position to stay usable on weak signal. The same web app can serve both passengers and conductors, which keeps development simple. No emerging technology is needed.

---

## 4. Preliminary Requirements

### 4.1 Functional requirements (user stories)

| ID | User story | Priority (MoSCoW) |
|---|---|---|
| FR-01 | As a **commuter going home**, I want to join the line for an incoming bus from my boarding house and get a ticket number so that I secure my place before I arrive at the terminal. | Must |
| FR-02 | As a **commuter**, I want to see my queue position, whether I am next to board, and my estimated boarding time so that I know when to leave for the terminal and whether I can board this bus. | Must |
| FR-03 | As a **conductor**, I want a list of waiting passengers in order, with a one-tap `Boarded` button for each so that I can track who has boarded while handing out tickets. | Must |
| FR-04 | As a **commuter**, I want to receive notifications ("30 minutes before boarding," "20 minutes before boarding") and the boarding area when the bus arrives so that I don't have to keep checking the app or guard my place in a crowd. | Should |
| FR-05 | As a **conductor**, I want to re-send a notification to a late passenger and press `No Show` only after about 20-30 minutes so that I can call the next passenger without being unfair to someone running late. | Should |
| FR-06 | As a **conductor**, I want to set the bus status (arriving, boarding, en route) so that passengers always see where their bus is in the trip. | Should |
| FR-07 | As a **priority passenger** (senior citizen, PWD, pregnant woman), I want to join a separate priority lane with my own ticket (e.g., P-03) so that I can board first, while regular ticket numbers stay unchanged. | Could |
| FR-08 | As a **commuter**, I want to see how many seats are left on a bus before I join, and cancel my spot if my plans change so that I don't wait for a full bus and my spot can go to the next passenger. | Could |
| FR-09 | As a **terminal operator**, I want reports on passengers per bus, boarded vs. no-show, and peak times so that I can plan how many buses to dispatch. | Won't (this time) |

### 4.2 Non-functional requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Performance | A queue position change (for example, when the conductor marks a passenger as `Boarded`) appears on passengers' phones within 5 seconds, and each page loads in under 3 seconds on a 3G mobile connection. |
| NFR-02 | Usability | A new passenger can join the queue and get a ticket in 3 taps or fewer, and all main buttons are at least 48 x 48 px so they can be tapped easily while carrying bags. |
| NFR-03 | Security / privacy | The app collects only the data needed (name and contact number), asks for consent before saving it, and deletes or anonymizes passenger data within 30 days after the trip, in line with the Data Privacy Act of 2012 (RA 10173). |
| NFR-04 | Compatibility | The app works in the latest two versions of Chrome on Android 8 or later, and the last-known ticket and queue position stay visible for at least 10 minutes if the connection drops. |

### 4.3 MoSCoW summary

- **Must have:** Join the queue remotely with a ticket number (FR-01); live queue position, "next to board" status, and estimated boarding time (FR-02); conductor boarding list with a `Boarded` button (FR-03).
- **Should have:** Timed notifications and boarding area (FR-04); `No Show` handling with re-notify and a 20-30 minute wait (FR-05); bus status updates (FR-06).
- **Could have:** Priority lane with separate tickets (FR-07); remaining seats display and cancel spot (FR-08).
- **Won't have (this time):** Operator reports and analytics (FR-09), online payment of fares, and SMS fallback notifications.

---

## 5. Minimum Viable Product (MVP)

### 5.1 MVP features

1. **Join the queue remotely:** A passenger picks the next incoming bus, joins the line in 3 taps or fewer, and gets a ticket number.
2. **Live queue position and estimated boarding time:** The passenger sees their position, whether they are next to board, and an estimated boarding time that updates within 5 seconds of a change.
3. **Conductor boarding list:** The conductor sees waiting passengers in order and marks each one as `Boarded` with one tap, which updates the passengers' queue positions.

### 5.2 Out of scope

- Timed notifications and boarding area alerts: they need a service worker and extra testing, so they come right after the MVP. For now, passengers see their status by opening the app.
- `No Show` handling with re-notify and bus status updates: the conductor can handle late passengers in person for now.
- Priority lane: it adds rules to the queue order, so it is saved for a later version.
- Seat count and cancel spot: they depend on bus capacity data, which the MVP does not track.
- Operator reports: they are not needed to solve the core problem.
- Online payment of fares: passengers keep paying the conductor on the bus.
- SMS fallback notifications: they cost money per message and are not needed for the first version.

### 5.3 Constraints and assumptions

- **Constraints:** One semester to deliver; a small student team; free or low-cost hosting; no integration with the terminal's existing systems; no access to real bus location data.
- **Assumptions:**
  - Passengers have an Android phone with mobile data or Wi-Fi, and use Chrome.
  - Each bus has a conductor who is willing to use the app while handing out tickets.
  - The terminal or bus company allows a pilot test with one route or one bus.
  - Passengers still show a ticket and pay the conductor on the bus as they do now.
  
### 5.4 Feasibility check (TELOS)

| Dimension | Key question | Your assessment |
|---|---|---|
| **Technical** | Can I build it with my skills and tools? | **High:** Flask, Jinja2, Bootstrap 5, and JavaScript fetch are standard, robust tools that cover the three MVP features. Live updates use simple polling every few seconds, so no advanced tools are needed. |
| **Economic** | Do the benefits justify the costs? | **High:** Uses open-source software and a free or low-cost hosting tier. The benefit is less crowding and waiting for passengers and a more organized boarding process for conductors. |
| **Legal** | Does it comply with law and policy (e.g., RA 10173)? | **High:** Complies with RA 10173 by collecting only a name and contact number, asking for consent, and deleting or anonymizing data within 30 days. Priority IDs are not stored because the priority lane is out of scope. |
| **Operational** | Will people use it, and can it be run? | **Medium:** Solves a documented pain point, since passengers already ask about the terminal on Facebook and the conductor needs only one tap per passenger, with no installation required. The main risk is getting a terminal or conductor to try it, so plan a small pilot. |
| **Schedule** | Can I deliver the MVP this semester? | **High:** The MVP has only three Must features and no notifications or payments, which leaves time at the end for testing with real users. |

**Verdict:** **Feasible if the scope stays at the three Must features and a conductor is available for a pilot test.** The project is well-bounded and uses proven technology. If time runs short, drop the estimated boarding time and keep position tracking.

---

## Submission Checklist

- [x] File saved as `activities/proposed-application/README.md` in my CCC181 repository
- [x] All `[bracketed placeholders]` replaced and guidance blockquotes removed
- [x] Sections 1–5 complete
- [x] Images (if any) placed in `images/` and displaying correctly on GitHub