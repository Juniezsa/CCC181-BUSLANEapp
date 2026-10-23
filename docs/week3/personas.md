# Person 1

## Oberin Dallas, the Person Waiting

> "Prepared and arrived early at the Bus terminal to avoid the rush hour and crowding, since it's a school break. But upon arriving I have to stand to wait and be in line for hours for the next bus. Also try to claim my place, by keeping my arms spread open, so no person can cut in-line when the bus arrives."

| | |
| --- | --- |
| **Photo or sketch** | ![Oberin going home for school break](docs/week3/images/going-home-oberin.jpg) |
| **Age, role and background** | Age: 21<br> 3rd-year Information Technology student;<br> Boards in a house <br> Hometown is 400km away<br> goes back to their hometown during school breaks, long weekends, and asynchronous weeks |
| **Goals** | 1. Be able to start or be inline for the bus while still in their boarding house or preparing <br> 2. Know what time and if they are next to board the bus |
| **Frustrations** | 1. They are not able to predict when the next bus will arrive <br> 2. Long wait times in the bus terminal and not certain if they are able to board the bus <br> 3. Crowding, cutting in line and "siksikan" when a bus finally arrives |
| **Devices and context** | Mid-range Android Phone on Mobile Data or Public Wifi; Cleaning their Boarding house, packing their clothes and things, getting ready to go to the bus terminal |
| **Tech comfort** | **High** — Is comfortable managing new websites in google chrome |
| **Accessibility needs** | Slow signal at some areas in the city <br> Has about 2-3 large bags to carry |

### Scenario

Oberin wakes up at 3 AM to pack and head to the bus terminal early. Knowing it's school break, peak season, and the terminal will be crowded, they open **BUSLANE** and see an incoming `Non-Stop Aircon Bus`. They prebook a spot and receive a ticket: "🎫 #45 on the line | Next Bus to Board | Estimated Boarding Time: 4:30 AM." With about 40 minutes to spare, Oberin finishes getting ready. Their phone chimes with "📢 30 minutes before boarding," and again on the way with "📢 20 minutes before boarding." At the terminal, they sit down and wait. When the bus arrives, the app notifies them: "Please proceed to area 13 and wait for boarding." Oberin goes straight to boarding without lining up or waiting for the next bus.


### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| Join the line for an incoming bus and get a ticket number | Join | FR-01 |
| Check my queue position, whether I am next to board, and my estimated boarding time | My place | FR-02 |
| Receive reminders and the boarding area when the bus arrives | Notifications | FR-04 |
| Join the priority lane (for priority passengers) | Join (priority option) | FR-07 |
| See remaining seats and cancel my spot if plans change | Bus details / My place | FR-08 |

### What this means for my interface

1. Because Oberin wants to be in line before he leaves his boarding house, my interface must let him join the queue for a specific bus (like the Non-Stop Aircon Bus) in two or three taps and immediately give him a ticket number.
2. Because Oberin wants to be in line before he leaves his boarding house, my interface must let him join the queue for a specific bus (like the Non-Stop Aircon Bus) in two or three taps and immediately give him a ticket number.
3. Because he carries 2-3 large bags and may have a weak signal, my interface must use large tap targets and keep his last-known ticket visible when the connection drops.

# Person 2

## Christian Gomes, the Staff Member

> "We are prepared for the crowd during peak seasons, but you won't really be able to predict what will happen, especially during boarding, everyone try to board as soon as possible."

| | |
| --- | --- |
| **Photo or sketch** | ![Sir Christian waiting at the entrance and counting passengers and checking tickets](docs\week3\images\SirChristian-counting-passengers.jpg) |
| **Age, role and background** | Age: 32 <br> Ticket Conductor; <br> Manages crowded bus terminal during peak seasons for about 8 years <br> Experienced different company systems during peak hours |
| **Goals** | 1. Instantly know how many has boarded and available seats <br> 2. Can easily manage on who can board or go inside the bus <br> Can efficiently give tickets to passengers |
| **Frustrations** | 1. Passenger says a seat is reserved, end with the people waiting for that person <br> 2. Has to constantly move through aisle just to count available seats and passengers, also asking if a seat is already occupied |
| **Devices and context** | Low-range Android Phone on Mobile Data or Public Wifi; counting passengers as well checking and giving passenger tickets |
| **Tech comfort** | **Medium** — is able to navigate through devices if taught properly, can learn quick and get used to systems |
| **Accessibility needs** | One hand is busy handing out and checking tickets <br>  Slow signal at some areas in the city/municipality |

### Scenario

During peak seasons, the bus terminal is always crowded with passengers. Sir Christian, a dispatcher, always has a hard time managing the people boarding: many try to get a seat as soon as possible to avoid waiting, and he has to keep track of how many passengers have boarded and how many seats are left. Now, instead of managing a large crowd trying to get in, Sir Christian opens the **BUSLANE Operator Dashboard** and goes to the "Notify Passengers" section. He selects the `Non-Stop Aircon Bus`, and only the passengers meant to board that bus are notified to line up. As a result, he no longer has to control a crowded line at the bus entrance, and he can count and monitor each passenger who boards.


### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| See the waiting passengers for a bus in order | Boarding list | FR-03 |
| Mark a passenger as `Boarded` with one tap | Boarding list | FR-03 |
| Re-send a notification to a late passenger and mark `No Show` after 20-30 minutes | Notify Passengers | FR-05 |
| Set the bus status (arriving, boarding, en route) | Bus status | FR-06 |
| Select a bus and notify only the passengers meant to board it | Notify Passengers | FR-04 / FR-05 |

### What this means for my interface

1. Because Sir Christian must track each passenger while handing out tickets, my interface must have a one-tap `Boarded` button for each passenger in the boarding section.
2. Because there is no guarantee that a passenger will show up on time, my interface must let him re-send the notification and only enable the `No Show` button after approximately 20-30 minutes, so he can then call the next passenger.
3. Because the conductor stays with the bus for the whole trip, my interface must let the conductor set the bus and passenger status (arriving, boarding, en route).