# Automation Worksheet: Customer Enquiries

**Scenario:** A team receives a CSV file of customer enquiries each day and wants to automate identifying the high-priority ones.

---

## 1. What is the problem?

Each day someone reads every enquiry to find the high-priority ones. This is slow, and the result depends on who does the reading, so urgent enquiries can be missed.

## 2. What are the inputs?

- **Daily CSV file** of customer enquiries.
- Expected columns: enquiry ID, date received, customer name, category, and message text. The scenario doesn't list them, so they need checking against the real file.
- **Priority rules**, agreed with the team. For example: category is "Complaint" or "Urgent", or the message contains words such as "refund", "cancel" or "legal".

## 3. What processing is required?

1. Read the CSV and check the expected columns are present.
2. Remove blank and duplicate rows.
3. Apply the priority rules to mark each enquiry **High** or **Normal**.
4. Count the High-priority enquiries and collect their details.
5. Produce a summary.

## 4. What are the outputs?

- **Summary:** the number of High-priority enquiries, with ID, date, customer and category for each.
- **Notification:** an email to the responsible team when there are High-priority items.

## 5. Is the task suitable for automation?

**Yes.** It repeats every day, the input has a fixed structure, and the priority rules are clear. Automation applies the rules the same way every time.

Human judgement is still needed for enquiries the rules can't classify, and for deciding how to respond.

---

## Discussion

**Which parts are repeatable?**
Reading the file, cleaning the rows, applying the priority rules, building the summary, and sending the notification.

**Which parts require human judgement?**
Deciding whether an unclear enquiry is urgent, writing the reply to the customer, and changing the priority rules when the business needs change.

**Would Power Automate or Python be more appropriate?**
A **hybrid** approach fits best:
- **Python** reads and cleans the CSV, applies the priority rules and builds the summary, since it handles structured text and data well.
- **Power Automate** handles the daily schedule and the email notification, since it connects to mail and file storage without code.
