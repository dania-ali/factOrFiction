# BUILD_LOG.md

## Task 1
- Brief:
Goal: scaffold a minimal Flask project structure that runs locally and supports future tasks.

Constraints:
use only Flask + pytest
no analysis logic yet
no databases or APIs
keep structure beginner-friendly

Acceptances:
python app.py starts localhost:5000
GET / returns 200
pytest runs successfully
templates/ and static/ folders exist
CLAUDE.md exists and reflects project conventions

- What Claude proposed: Claude proposed a larger initial setup including /analyze routes, analyzer.py, result templates, scoring logic stubs, and multiple tests.

- What I changed before approving: I reduced the scope to only scaffolding the Flask app and basic project structure. I removed analysis logic and result pages so Task 1 stayed easier to verify.

- Verification: Ran python app.py and confirmed the homepage loads at http://localhost:5000. Ran pytest and confirmed tests execute successfully without failures.

- One thing I learned: Keeping early tasks intentionally small makes debugging easier and prevents feature creep before the foundation is stable.

---

## Task 2
- Brief
Goal: create the base homepage layout and navigation for the Fact or Fiction Flask app using Jinja templates and simple CSS.

Constraints:

* use only Flask templates and vanilla HTML/CSS
* no JavaScript yet
* no credibility scoring logic yet
* keep the layout simple, responsive, and beginner-friendly
* use a reusable base.html template
* navigation does not need multiple working pages yet

Acceptances:

* homepage renders successfully at GET /
* page includes:

  * app title
  * short project description
  * navigation bar
  * input section placeholder
  * analysis section placeholder
  * results section placeholder
* templates use base.html inheritance correctly
* CSS loads from static/style.css
* layout remains readable on desktop and mobile
 
- What Claude proposed: Claude proposed a complete implementation which includes structured sections for hero/input/analysis/results, and a detailed CSS design

- What I changed before approving: I tightened scope to prevent too much over-designing early. I removed or discouraged fake navigation pages (like About without a route), reduced styling complexity.

- Verification: Ran python app.py and confirmed homepage renders correctly at http://localhost:5000. Visually confirmed presence of title, description, navigation header, and three placeholder sections. 

- One thing I learned: Early UI tasks should prioritize structure over design

---

## Task 3
- Brief:
Goal: add a working claim submission form and connect it to Flask so user input is sent to the backend and safely returned to the template.

Constraints:
use Flask POST request handling only
no database or persistence
no analysis or scoring logic yet
keep changes minimal and surgical
do not break existing Task 1–2 functionality

Acceptances:
GET / loads successfully
POST /analyze returns status 200
submitted claim is correctly received via request.form
submitted claim is echoed back in the UI using Jinja
empty submissions do not cause server errors (no 500)
existing layout/navigation remains unchanged

- What Claude proposed: Claude proposed a surgical edit to app.py adding a POST /analyze route, extending Flask imports with request, and updating index.html to include a form and conditional rendering of the submitted claim.

- What I changed before approving: I enforced strict non-rewrite rules for app.py I also ensured the plan remained strictly data-flow focused without introducing analysis or scoring.

- Verification: Ran python app.py and confirmed form renders at homepage. Submitted multiple claims and confirmed they are echoed back correctly. Verified empty submissions do not crash the server. Ran pytest and confirmed all existing tests still pass.

---

## Task 4
- Brief:
Goal: implement a basic rule-based credibility scoring system that evaluates submitted claims using keyword matching and returns a score and explanation in UI

Constraints:
use only Python (no AI, no NLP libraries, no external APIs)
no changes to existing routing structure beyond minimal integration
no redesign of UI or layout
keep scoring logic simple and deterministic
use basic string/word matching only
do not introduce advanced analysis features (sentiment, bias detection, etc.)

Acceptances:
submitting a claim returns a score between 0–100
different keyword inputs produce different scores
label updates correctly (Likely True / Uncertain / Likely False)
analysis and results sections render correctly in UI when a claim is submitted
empty submissions do not crash the application
existing Task 1–3 functionality remains unchanged

- What Claude proposed: Claude proposed creating a new analysis.py module containing a deterministic keyword-based scoring function. The function uses a base score of 50, adjusts score using positive and negative keyword matches, clamps results between 0–100, and returns a structured dictionary with score, label, and explanation. It also updates app.py to call this function in the /analyze route and modifies index.html to conditionally render analysis and results.

- What I changed before approving: I made sure ther ewas no overengineering by making sure the scoring system remains strictly keyword-based. I confirmed that explanation logic remains simple and integration into Flask stays minimal and does not affect existing Task 1–3 behavior or UI structure.

- Verification: Ran python app.py and confirmed homepage and form still load correctly. Submitted multiple test claims and verified score, label, and explanation update dynamically in the UI. Confirmed empty submissions do not crash the server. Ran pytest and confirmed all existing tests from previous tasks still pass.

- One thing I learned: Rule-based systems should stay minimal early on so future upgrades (like real NLP or AI scoring) can replace them cleanly without refactoring the entire ap

---

## Task 5 — Example Claims for Quick Testing

- Brief:
Goal: add preset example claims users can click to instantly test the Fact or Fiction app and view different credibility outcomes without typing manually.

Constraints:
use only Flask templates and vanilla HTML/CSS
no JavaScript
reuse the existing POST /analyze flow
do not modify scoring logic
do not modify tests
keep implementation simple and beginner-friendly
manual textarea submission must continue working unchanged

Acceptances:
homepage displays multiple clickable example claims
clicking an example submits the claim through the existing Flask form flow
results page displays a populated analysis for each example
examples demonstrate different credibility outcomes
manual claim entry still works normally
existing functionality and tests remain unchanged

- What Claude proposed: Claude proposed adding a new "Try an Example" section containing multiple small POST forms with hidden claim inputs. Each example reuses the existing /analyze route and scoring system without needing JavaScript. Claude also proposed lightweight CSS styling for the example buttons.

- What I changed before approving:  I corrected wording in one example claim for readability and realism.

- Verification: Ran python app.py and confirmed the example claims render between the hero and input sections. Clicked each example and verified the app generates different credibility outcomes correctly. Confirmed manual textarea submissions still work normally. Ran pytest and confirmed all existing tests still pass.

- One thing I learned: Reusing existing backend routes keeps new features simple and lessenss the chance of adding unnecessary complexity

---

## Task 6 - UI polish
- Brief:
Goal: improve the overall UI polish and responsiveness of the Fact or Fiction app by refining spacing, typography, colors, and layout consistency while preserving the existing structure and functionality.

Constraints:
use only vanilla CSS
no JavaScript
do not change backend logic or routing
do not redesign the application structure
maintain existing sections and user flow
keep styles simple, readable, and beginner-friendly
ensure mobile responsiveness is preserved or improved
maintain sufficient color contrast for readability

Acceptances:
layout remains readable on desktop and mobile screens
spacing and alignment are visually consistent across sections
buttons, forms, and results cards use consistent styling
typography and colors improve readability without reducing accessibility
existing functionality and tests remain unchanged

- What Claude proposed: Claude proposed refining the existing CSS by standardizing spacing, improving typography hierarchy, adding a cleaner neutral color palette, improving nav alignment, styling forms and buttons, refining section cards, improving focus states for accessibility, and adding responsive mobile behavior. Claude also proposed making the results section visually distinct without modifying templates or backend logic.

- What I changed before approving: I restricted the scope to visual polish only and prevented structural redesigns, animations, JavaScript additions, or frontend frameworks. I removed unnecessary discussion around advanced CSS selectors like () and simplified the results styling approach

- Verification: Ran python app.py and manually tested the app. Verified that navigation alignment, typography, spacing, buttons, forms, example claims, and results sections remain readable and visually consistent. Submitted several example claims to confirm the UI still behaves correctly after styling changes. Ran pytest and confirmed all existing tests still pass.

- One thing I learned: CSS polish and accessibility improvements can significantly improve usability without requiring complex frameworks or big redesigns

---

## AI Workflow
- For planning I used Claude because it was good at making structured implementation plans and breaking things into manageable steps. For execution I relied on Claude's code to make code changes while I reviewed before approving implementation. For polishing, I used ChatGPT and GitHub Copilot to review plans and see where Claude was overengineering. For reviewing, I used ChatGPT to check whether each task matched the acceptance criteria. ChatGPT outperformed CLaude in task 4 when ChatGPT helped simplify the design and evaluated if the scoring logic matched the goals. I switched tools mid-task, which was during Tasks 5 and 6, where I switched to GHatGPT because Claude was making things unnecessarily complex.

---

## Reflection

- The agentic workflow let me produce a complete Flask app with multiple features and appealing style in a timeframe that would've been difficult to complete by myself. I could've eventually built the project but planning every task and writing implementation details would've taken forever. Using Claude to generate plans let me focus on evaluating decisions instead of coming up with everything from scratch over and over. However, there were multiple times when I had to step in and override claude. The biggest was scope control. Claude would propose solutions that worked but were unnecessarily more complex than what was required. Like when planning tasks regarding UI, it would suggest complex styling systems or details that were far above what was the acceptance criteria asked for. So I had to decide what was necessary now since the project was to build a small shippable app instead of a full product. The biggest thing the project revealed about me was that my judgment is more valuable than what I thought initially. It also revealed knowledge gaps. Before starting I thought the hardest part would be writing the actual code. But I learned that deciding what code should be produced was harder. I saw that I could point out when a plan was too complex or drifted too far from the criteria even if I couldnt explain why. That showed me how a big part of software development is making good decisions. I also noted gaps in my frontend knowledge, specifically around CSS organization. I needed help identifying the best implementation approach. I also noticed how I would accept AI suggestions too quick;y so I had to learn to slow down and evaluate if changes were actually solving the problem effectively. I plan to bring this workflow into my internship. On day one, I will try to understand the codebase and then use AI to help me make plans before implementing changes. I want to use AI to break down work into tasks and explain unfamiliar things. I will then review those plans critically before implementing anything. The biggest lesson I'm taking away is that AI is best when you apply human judgement as well.
