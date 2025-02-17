# 📌 Introduction  
This package consolidates a collection of tools and scripts I've developed to streamline workflows and improve efficiency.  
The **full source code** is available for review, ensuring transparency and eliminating concerns about its inner workings.  

---

# 🚀 Features Overview

## 🔹 Automations  
- **Quick Note Entry**  
  - Instantly inserts the current date and **Agent ID (`YOURNAME3`)** into the focused text box, for Texte/Info.  
  - Cursor is automatically positioned in the center for immediate note-taking.  

## 🔹 Hotkeys  
- `F1` – Toggle focus between **Novomind** and **ASSD**  
  - 📌 Displays information where your eyes are already focused, reducing unnecessary head movement between two monitors just to confirm a booking number or date for example.  
  - Work in Progress: Novomind window title should be **"Novomind iAGENT Desk - USERNAME"** to prevent known minor issues.
- `F2` – Open/Focus on **Notepad**  
  - ✍ Instantly start typing without using the mouse.  
- `Ctrl + Space` – **Simulated "Enter" Key**  
  - 💡 When pasting with `Ctrl + V`, keep holding `Ctrl` and press `Space` to simulate pressing `Enter`.  
  - ✅ Prevents unnecessary hand movement between keyboard and mouse.  
- `Ctrl + Left Click` – **Play/Pause Music**  
  - 🎵 Quickly pause media when answering calls without switching applications.  

### 🔹 Customizable Function Keys  
- 🔧 `F6 & F7` – Configurable hotkeys for additional functionality.  
- ❓ **Dedicated Notepad Hotkey?** *(To be determined.)*  

---

# 🛠 ViolentMonkey Scripts  
*(Supports both English & German interfaces where applicable.)*  

## **ASSD Enhancements**  
- **Auto Login**  
  - 💡 Credentials are entered in **MyToolkit** before script generation.  
  - 🔒 Credentials are automatically deleted post-generation.  
- **Auto-Open Key Sections**  
  - ✅ Automatically opens `Tagesübersicht` & `Reservations`.  
- **Hostel Index**  
  - 📋 View a **sortable, searchable list** of hostels by **name, house ID, or house number**.  
  - 🔍 Use `Ctrl + S` to open/close search and `Enter` to confirm selection.  
- **Auto-Fill Standard Booking Settings**  
  - 🏨 If no dates are set (e.g., creating a new booking from the **Reservations** tab), the system defaults to:  
    - **Arrival Date:** Today  
    - **Departure Date:** Tomorrow  
  - 📌 Automatically selects **FLEX** as the booking type.  
  - 🚀 Guest type is preselected in the background (on the second tab).  

### ⏳ **Work in Progress**  
- **Auto-Fill Standard Guest Settings** *(Pending refinement.)*  
## 🔹 Enhanced Controls  
- **Headset Control (Taskbar Quick-Access Buttons)**  
  - 📢 **Maximum Volume** – Increases volume to maximum for when you set your headset down, ensuring you hear incoming calls.  
  - 🎚 **Normal Volume** – Restores volume to a reasonable level (e.g., 40%) before answering a call.  
  - ⏳ **Work in Progress:** Play/Pause Media  

---

# 🔧 Additional Features  
- **Whitespace Removal Around Numbers**  
  - 🧹 Automatically removes spaces before and after numbers when copying booking IDs to ensure correct searches in ASSD.  
- **`Ctrl + Del` Fix for Novomind**  
  - ⌨ Enables **word-by-word deletion** as expected.  

---

# 📂 Miscellaneous  
- `F4` – **Email Response Templates Index**  

---

# 🔮 Future Features  

### ✅ Confirmed  
- **Chat Response Templates Index**  
- **Chat Response Buttons?** *(Pending further organization.)*  
- Add extension numbers to hostel index for easy copy and paste

### 🤔 To Consider  
- **Default notes in Texte Info?**  
  - Example: Auto-inserting placeholders like `Transaction ID: xxx; Email ID: xxx`  
  - Possibly an `F4` search index similar to chat responses.  
- Pressing headset button detects teams opening, minimizes it, switches to novomind, and answers the call. (need to dig up current, buggy implementation from months ago)

---

# ⚙ Setup Instructions  

## 🔹 Function Key Configuration (For Laptops)  
- If function keys (`F1–F12`) default to media and other controls, update your **BIOS settings** to prioritize function key behavior.  

## 🔹 ViolentMonkey Extension  
- Install **[ViolentMonkey](https://violentmonkey.github.io/)**, a free and open-source browser extension for running custom scripts.  
- All provided scripts are **vetted for security** and optimized for performance.  

---

## 📢 Future Improvements & Contributions  
Have suggestions or found a bug? Open an issue to share your feedback! 🚀  

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