# Import the os module. OS will allow us to create file path to access the csv file
import os

# Import csv module to read CSV file in python once it is located by OS
import csv

# Create the file path (using os) to access the csv file (csv_path ='.\Resources\budget_data.csv'). Path MUST start from the current location.
csv_path = os.path.join('.\Resources', 'budget_data.csv')

# Read the csv file using csv module
with open(csv_path) as file:

    # Open the file using csv.reader, specifing variable that holds contents and the delimiter  
    csvreader = csv.reader(file, delimiter=',')

    #next to skip the first line (header); # print to confirm
    csv_header=next(csvreader)
    
    # Set variables for data analysis
    numMonths = 0
    totalProfitloss = 0
    prevMonthProfitOrLoss = 0
    curMonthProfitOrLoss = 0
    monthlyChangeProfitOrLossList = []
    monthlyChangeProfitLossMonthsList = []

    # Loop to read the data
    for line in csvreader:
        #Print each line
        # print(line)

        # Increment the month count to track the number of months included in the budget
        numMonths = numMonths + 1

        # Sum second index (profit/losses) in each line, convert second index to integer
        totalProfitloss = totalProfitloss + int(line[1])

        # Set curMonthProfitOrLoss
        curMonthProfitOrLoss = int(line[1])

        # For the first line, do not do the calculation, only set the previous month profitloss as current month profitloss for next month
        if numMonths == 1:
            prevMonthProfitOrLoss = curMonthProfitOrLoss
            
        else:
            
            # Calculate monthly change profit or loss for every line
            monthlyChangeProfitLoss = curMonthProfitOrLoss - prevMonthProfitOrLoss
            
            # Add monthly change profit or loss to monthlyChangeProfitOrLoss List
            monthlyChangeProfitOrLossList.append(monthlyChangeProfitLoss)

            # Reset prevMonthProfitOrLoss for next line
            prevMonthProfitOrLoss = curMonthProfitOrLoss

             # Add month (index) from each line to monthlyChangeProfitOrLossMonth List; later PRINT the list to check it.
            monthlyChangeProfitLossMonthsList.append(line[0]) 

# Create and add to textToPrint variable so that we can export results to output.txt in Analysis folder and print to console
textToPrint = "Financial Analysis\n"
textToPrint += "--------------------------\n"
textToPrint += (f"Total Months: {numMonths}\n")

# Print total amount of profit loss over entire period.
textToPrint += (f"Total: ${totalProfitloss}\n")
        
# Calculate, round by 2, and print average monthly change profit or loss
averageChange = sum(monthlyChangeProfitOrLossList)/len(monthlyChangeProfitOrLossList)
averageChange = round(averageChange,2)
textToPrint += (f"Average Change: ${averageChange}\n")

# Find greatest increase in profits, print to confirm
greatestIncreaseProfit = max(monthlyChangeProfitOrLossList)

# Find greatest decrease in profits, print to confirm
greatestDecreaseProfit = min(monthlyChangeProfitOrLossList)

# Find and print the corresponding month for the greatest increase and decrease in profits. This we are going to do by first finding out the index value of greatest increase or decrease in profits in the monthlychangeprofitloss list. Then we will use the SAME index value to pull the corresponding month from the monthlychangeprofitloss months list.
maxIndex = monthlyChangeProfitOrLossList.index(greatestIncreaseProfit)
maxMonth = monthlyChangeProfitLossMonthsList[maxIndex]
textToPrint += (f"Greatest Increase in Profits: {maxMonth} (${greatestIncreaseProfit})\n")
    
minIndex = monthlyChangeProfitOrLossList.index(greatestDecreaseProfit)
minMonth = monthlyChangeProfitLossMonthsList[minIndex]
textToPrint += (f"Greatest Decrease in Profits: {minMonth} (${greatestDecreaseProfit})")

# Output textToPrint variable to output.txt file
with open("Analysis/output.txt","w") as txt_file:
    txt_file.write(textToPrint)

print(textToPrint)