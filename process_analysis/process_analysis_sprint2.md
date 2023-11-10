# Process Model Analysis Document

### Definition of our Process:
Our current process is structured around 3 weekly meetings focused on code discussion, design reviews, problem-solving, task allocation, and progress tracking. Each meeting involves a note-taker documenting discussions in our meeting_notes.md file and a SCRUM master who translates these notes into tasks or issues on our GitHub Projects kanban board. These tasks are then assigned to team members based on their specific roles within the web server project.

### Process Elements Description:
The process begins with the meetings, where tasks are identified and assigned. Each task corresponds to a specific part of the webserver, and the responsible team member addresses these tasks in their own branches, followed by creating a pull request (PR). Our PR process is structured with a template that includes sections for description, changes made, testing status, and additional information. We utilize GitHub labels like features, bugs, documentation, etc., for categorization. Automated checks via GitHub Actions run tests and linting on PRs.

### Process vs. Process Model:
The process is the actual activities and tasks we perform (meetings, coding, PRs), while the process model is the theoretical framework, in our case, an Agile/SCRUM methodology, that guides these activities. Our model emphasizes continuous integration, regular meetings, and iterative development but sometimes diverges from ideal practices due to project constraints or team dynamics.

### Original Process Description:
Initially, our project lacked a formalized review process. We did not have a PR template, automated testing via GitHub Actions, or a specific template for code reviews. We lacked structure and it was messy.

### Evolution of Process:
Over time, we introduced a PR template, a formal code review template, and integrated GitHub Actions for automatic testing and linting. These additions were aimed at improving our workflow's efficiency and ensuring code quality.

### Reasons for Changes:
These changes were implemented to streamline our process, reduce manual effort, and maintain high standards of code quality. The automation of tests and linting helped us focus more on core development tasks and less on routine checks.

### Current Challenges:
Our current challenges include an incomplete comment section for reviews and a lack of styling in HTML with CSS. Feedback from Sprint 1 highlighted the absence of a substantial code review process and user stories.

### Proposed Improvements:
To address these issues, we propose conducting more regular and documented code reviews on branches, involving every team member in the PR review process. Implementing a more structured approach to HTML/CSS styling is also a priority.

### Implementation Strategy:
Implementing these improvements will require a more active and involved effort from each team member. Specific roles or tasks, such as code reviewers or UI/UX specialists, might be assigned. We plan to monitor these changes through our regular meetings and SCRUM updates, ensuring each enhancement aligns with our overall project goals and agile methodology.