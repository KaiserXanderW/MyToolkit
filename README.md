# 📌 Introduction  
This is a collection of tools I've developed and consolidated into one package.  
The full source code is available for review to ensure transparency and dispel any concerns regarding its inner workings.  

---

# 🚀 Features Overview  

## 🔹 Extra/Easier Controls  
- **Headset Control (Single-click buttons attached to the taskbar)**  
  - 📢 **Maximum Volume** – Increases volume when you set your headset down so you can hear incoming calls.  
  - 🎚 **Normal Volume** – Restores volume to a reasonable level (e.g., 40%) before answering a call.  
  - ⏳ **Work in Progress:** Play/Pause Media  

## 🔹 Automations  
- **Quick Note Entry**  
  - Instantly inserts the current date and **Agent ID (`YOURNAME3`)** into Texte/Info.  
  - Cursor is automatically positioned in the center for immediate note-taking.  

## 🔹 Hotkeys  
- `F1` – Toggle focus between **Novomind** and **ASSD**  
  - 📌 Information appears where your eyes are already looking, avoiding unnecessary head movement.  
  - 🔄 If multiple windows are open, press `F1` a few times until Novomind is in focus.  
- `F2` – Open/Focus on **Notepad**  
  - ✍ Quickly start typing without using the mouse.  
- `Ctrl + Space` – **Simulated "Enter" Key**  
  - 💡 When pasting with `Ctrl + V`, keep holding `Ctrl` and press `Space` to simulate pressing `Enter`.  
  - ✅ Avoids moving your hand off the mouse to confirm entries.  
- `Ctrl + Left Click` – **Play/Pause Music**  
  - 🎵 Answer calls without switching to the media player.  

### 🔹 Customizable Function Keys  
- 🔧 `F6 & F7` – Configurable hotkeys for additional functionality.  
- ❓ **Hotkey for Notepad?** *(To be determined.)*  

---

# 🛠 ViolentMonkey Scripts  
*(Supports both English & German elements where applicable.)*  

## **ASSD Enhancements**  
- **Auto Login**  
  - 💡 Credentials are entered in MyToolkit before script generation.  
  - 🔒 Credentials are automatically deleted after generation.  
- **Auto Open Key Sections**  
  - ✅ `Tagesübersicht` & `Reservations` open automatically.  
- **Hostel Index**  
  - 📋 View a sorted, searchable list of hostels by **name, house ID, or house number**.  
  - 🔍 Use `Ctrl + S` to open/close search.  
- **Auto Fill Standard Booking Settings** *(Reworded for clarity)*  
  - 🏨 If no dates are set (e.g., when creating a new booking from the reservations tab), the system defaults to:  
    - **Arrival Date:** Today  
    - **Departure Date:** Tomorrow  
  - 📌 Automatically selects **FLEX** as the booking type.  
  - 🚀 Guest type is preselected in the background (on the second tab).  

### ⏳ **Work In Progress**  
- **Auto Fill Standard Guest Settings** *(Pending refinement.)*  

---

# 🔧 Additional Features  
- **Whitespace Removal Around Numbers**  
  - 🧹 Automatically removes spaces when copying booking numbers.  
- **Ctrl + Del Fix for Novomind**  
  - ⌨ Enables **word-by-word deletion** as expected.  

---

# 📂 To Categorize  
- `F4` – **Email Response Templates Index**  
- **Chat Response Templates Index**  
- **Chat Response Buttons?** *(Needs further organization.)*  

---

# ⚙ Setup Instructions  

## 🔹 Function Key Configuration (For Laptops)  
- If function keys (`F1–F12`) are secondary (e.g., default to volume control), update your **BIOS settings** to reverse this behavior.  

## 🔹 ViolentMonkey Extension  
- Install **[ViolentMonkey](https://violentmonkey.github.io/)**, a free and open-source browser extension that runs custom scripts.  
- All scripts provided here are **vetted for security** and optimized for efficiency.  

---

## 📢 Future Improvements & Contributions  
Have a suggestion or found a bug? Open an issue to share your feedback! 🚀  

--------------------------
My Words:
# Introduction
This is a collection of tools I've developed over the past months, brought together into one convenient package.
All the code is here to review in order to dispel suspicion as to the inner workings of this program.

# List of features

## Extra/Easier Controls
- Headset Control (Single click buttons attached to taskbar)
  - Maximum volume (this is for when you set your headset down, so when it rings, you hear the ringer)
  - Normal volume(this is to bring it to a normal level (40%?) before answering the call)
  - Work in Progress: play/pause media

## Automations
- Shortcut for inserting current date and Agent ID (YOURNAME3) for notes in Texte/Info, then places cursor in the center for immediate note taking

## Hotkeys
- F1 switches focus between Novomind and ASSD
  - (I don't have them on seperate screens anymore, as information often has to be compared, so pressing the hotkey and the information appears where my eyes are already looking is easier than moving my eyes to the other monitor and moving them back again.
  - (sometimes you've opened multiple windows and and when a call comes, its easy to hit F2 once or twice until Novomind appears)
- F2 opens/focuses on notepad
  - don't have to move your mouse to open and then move your hand to the keyboard. quickly start typing after hitting F2, as your fingers are already on your keyboard. 
- Ctrl+Space = Enter
  - When pasting with Ctrl+V, can release V while still holding down Ctrl and the hit enter, which simulates hitting the enter key. This negates the need to take your hand off the mouse to hit the enter key.
- Ctrl+Left Click = Play/Pause music
  - Dont have to navigate to audio player or move mouse to the play/pause before answering call)

- a row should have settable F hotkeys, like F6 and F7
- hotkey for notepad?

## ViolentMonkey Scripts (english vs german for some of these elements?)
- ASSD - Auto Log in
	- Enter Credentials in MyToolkit window before generating the script to include that. After generation, credentials are automatically deleted from MyToolkit.
- ASSD - Auto Open Tagesübersicht and Reservations
- ASSD - Hostel Index
	- Lists all hostels, sorted by name, house ID or house number. Also searchable. Ctrl+S to open and close search.
- ASSD - Auto Fill Standard Booking settings (reword this)
  - This auto selects the booking type as FLEX, if no dates are set(like when creating a new booking from the reservations tab vs creating a booking with dates set in the Tagesübersicht) it'll auto select todays date as arrival and tomorrows date as the departure date, also guest type is auto selected in the background(the second tab)
- Work In Progress
  - ASSD - Auto Fill Standard Guest Settings (reword)

# Other
- Whitespace around numbers removal
  - If only numbers are copied, automatically removes whitespace around booking numbers 
- Ctrl+Del fix for Novomind
  - Can delete the last word, one word at a time, like it should. 


# to categorize
- F4 Email Response Templates Index
- Chat Response Templates Index
- Chat reponse buttons?

# Setup
- if using a laptop and their function keys are secondary, you'll have to access the bios and reverse that default setting.
- install ViolentMonkey extension. This is a free and open source software that executes custom scripts, which in this case are vetted for security and provided by us.