```text
 ██████╗  █████╗
██╔═══██╗██╔══██╗
██║   ██║███████║
██║▄▄ ██║██╔══██║
╚██████╔╝██║  ██║
 ╚══▀▀═╝ ╚═╝  ╚═╝
      MODULE 4 · AI-ASSISTED SCRIPTING
```

<p align="center">
  <img src="robot.svg" alt="Robot mascot saying print hi" width="220">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue?logo=python&logoColor=white" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/modules-4%2F8%20done-brightgreen" alt="4 of 8 modules done">
  <img src="https://img.shields.io/badge/AI-assisted-8A2BE2" alt="AI assisted">
  <img src="https://img.shields.io/badge/vibes-immaculate-ff69b4" alt="Vibes: immaculate">
  <img src="https://img.shields.io/badge/dependencies-zero-success" alt="Zero dependencies">
</p>

> *Scripts that work, mostly on the first try.*
> Python, AI assistance, and a healthy amount of vibe coding.

This repository holds the hands-on labs for the **AI Assisted Scripting: Low-code Pathway**. You will use AI tools to write, improve, test and document small Python automations, then check your work against the exercise guide.

---

## 🗺️ Module progress

`Labs done  ██████████░░░░░░░░░░  50%  (4 of 8 modules)`

| Module | Topic | Status | Where to look |
|---|---|---|---|
| 1 | Tools walkthrough | ✅ No tasks | Trainer-led |
| 2 | Define an automation solution | 📝 Worksheet (write-up, no code) | [`Module-2 Lab/`](Module-2%20Lab/) |
| 3 | Generate your first script | ✅ Done | [`Module-3 Lab/tv_show_search.py`](Module-3%20Lab/tv_show_search.py) |
| 4 | Improve AI-generated code | ✅ Done | [`Module-4 Lab/improved_search.py`](Module-4%20Lab/improved_search.py) |
| 5 | Retrieve TV show data from an API | ✅ Done | [`Module-5 Lab/`](Module-5%20Lab/) |
| 6 | Externalise configuration | ⏳ Not in repo yet | Exercise guide, section 1.6 |
| 7 | Test and break the automation | ⏳ Not in repo yet | Exercise guide, section 1.7 |
| 8 | Prepare for workplace use | ⏳ Not in repo yet | Exercise guide, section 1.8 |
| Workshop | Football match monitor | ⏳ Not in repo yet | Exercise guide, section 2 |

---

## 📁 What is in here

```
.
├── EG_01_Exercise_Guide.md     # Full course exercise guide (converted from PDF)
├── hello.py                    # The obligatory first script
├── lab/                        # Setup tasks and the messy sales dataset
│   ├── Setup Task 1 - ...txt   # Launch the lab VM, mount the D: drive
│   ├── Setup Task 2 - ...txt   # Install PyCharm
│   ├── Setup Task 3 - ...txt   # Create a GitHub account (use the VM!)
│   ├── sales_messy.csv         # Original data, deliberately chaotic
│   └── sales_clean.csv         # Cleaned version (see "Known issues")
├── Module-2 Lab/               # Automation planning worksheet brief
├── Module-3 Lab/               # Search script: welcome, prompt, summary
├── Module-4 Lab/               # AI-generated script, refactored for humans
└── Module-5 Lab/               # TVMaze API script, with README and sample output
```

---

## 🚀 Quick start

You need **Python 3.7 or newer**. Nothing else needs installing: every script uses the standard library.

```bash
# Hello, world
python3 hello.py

# Module 3: search with a welcome banner and summary
python3 "Module-3 Lab/tv_show_search.py"

# Module 4: the refactored search script
python3 "Module-4 Lab/improved_search.py"

# Module 5: live TVMaze search (needs internet)
cd "Module-5 Lab" && python3 tvmaze_search.py
```

Module 5 has its own [README](Module-5%20Lab/README.md) with more detail.

---

## 🧪 Vibe check

| Check | Result |
|---|---|
| `hello.py` prints `hello` | ✅ Pass |
| Module 3 accepts a search term and prints a summary | ✅ Pass |
| Module 3 rejects an empty search term | ✅ Pass |
| Module 4 output matches the original AI script | ✅ Pass |
| Module 5 returns real shows from TVMaze | ✅ Pass |
| Module 5 says "No rating" instead of crashing | ✅ Pass |
| The AI never said "Certainly!" in the commit messages | 🤞 Unverified |

---

## 🐛 Known issues

- **The sales data is still a bit messy.** `sales_clean.csv` has four blanks where the source data was missing a value: Quantity (ORD1006), Salesperson (ORD1019), Date (ORD1021) and Order_ID (last row). Order ORD1018 is also missing from the sequence. These are left blank on purpose rather than guessed.
- **The Module 3 and Module 4 scripts simulate data.** They don't call a real service. That's intentional for those labs.
- **Module 5 needs internet access** to call the TVMaze API.
- **Module 2 is a worksheet, not code.** Its deliverable is a one-page document, and no template is included.

---

## 🤖 Working in this repo

- Use **AI tools** to generate and improve code, but **check every change** before you trust it. The guide's own rule: *AI can suggest, learners must verify.*
- Keep each lab in its own `Module-N Lab/` folder.
- Commit messages should say what changed and why.

---

## 📜 Licence and credits

Course material is © QA Limited, from the *AI Assisted Scripting: Low-code Pathway*. The lab scripts in this repository were written as learning examples.

> 🥠 *Fortune cookie says: your code will run. Eventually. Probably after one traceback.*

*This repository may contain traces of AI. Results may vary. Works on my machine.* 🧑‍💻
