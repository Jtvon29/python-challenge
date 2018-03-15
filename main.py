# Dependencies
import csv
import os

# Files to load and output (Remember to change these) 
csvpath = os.path.join("PyBank", "budget_data_2.csv")
output_file = ("../pybank/budget_analysis_2.txt")

# Track various revenue parameters
total_months = 0
prev_revenue = 0
total_revenue = 0
month_of_change = []
rev_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


# Read the csv and convert it into a list of dictionaries
with open(csvpath,encoding="latin-1") as revenue_data:
   reader = csv.DictReader(revenue_data)

   for row in reader:

       # Track the total
       total_months = total_months + 1
       total_revenue = total_revenue + int(row["Revenue"])

       # Track the revenue change
       revenue_change = int(row["Revenue"]) - prev_revenue
       prev_revenue = int(row["Revenue"])
       rev_change_list = rev_change_list + [revenue_change]
       month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
       if (revenue_change > greatest_increase[1]):
           greatest_increase[0] = row["Date"]
           greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
       if (revenue_change < greatest_decrease[1]):
           greatest_decrease[0] = row["Date"]
           greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(rev_change_list) / len(rev_change_list)

# Generate Output Summary
output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total Revenue: ${total_revenue}\n"
   f"Average Revenue Change: ${revenue_avg}\n"
   f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
   txt_file.write(output)
