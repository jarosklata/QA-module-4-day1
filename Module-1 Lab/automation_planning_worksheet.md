# Automation Planning Worksheet: Customer Enquiries

**Scenario:** A team receives a CSV file of customer enquiries each day and wants to automate finding the high-priority ones.

---

## 1. Problem

Staff read through each day's enquiries by hand to find the high-priority ones. It takes time, and the result depends on who reads them, so urgent enquiries can be missed.

## 2. Inputs

- **Daily CSV file** of customer enquiries.
- Assumed columns: enquiry ID, date received, customer name, category, and message text. The scenario doesn't list the columns, so these need checking against the real file.
- **Priority rules**, agreed with the team. For example: category is "Complaint" or "Urgent", or the message contains words such as "refund", "cancel" or "legal".

## 3. Processing

1. Read the CSV file and check that the expected columns are present.
2. Remove blank or duplicate rows.
3. Apply the priority rules to mark each enquiry as **High** or **Normal**.
4. Count the High-priority enquiries and collect their details.
5. Build a summary report.

## 4. Outputs

- **Summary report:** the number of High-priority enquiries, plus a list with ID, date, customer and category for each.
- **Notification:** an email to the responsible team when the report has High-priority items.

## 5. Suitable for automation?

**Yes.** The task runs every day, the input has a fixed structure, and the priority rules are clear. Automating it saves time and applies the rules the same way every time.

Human judgement is still needed for enquiries the rules can't classify, and for deciding how to respond.

## 6. Discussion

**Which parts are repeatable?**
Reading the file, cleaning the rows, applying the priority rules, building the summary, and sending the notification.

**Which parts require human judgement?**
Deciding whether an unclear enquiry is urgent, writing the reply to the customer, and changing the priority rules when the business needs change.

**Power Automate or Python?**
Both, in a **hybrid** approach:
- **Python** reads and cleans the CSV, applies the priority rules and builds the report, since it's good with structured text and data.
- **Power Automate** handles the scheduled run and the email notification, since it connects to mail and file storage without code.

