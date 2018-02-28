#!/usr/bin/python

import csv
import sys
from datetime import date
from datetime import timedelta


def main():
	csvFileName = "SP500TR.csv"
	endDate = date.today()
	startDate = date(endDate.year - 20, endDate.month, endDate.day)
	monthlyInvestement = 300
	initialInvestement = 0
	if len(sys.argv) != 6 :
		print "Usage: " + sys.argv[0] + " [start date: year-month-day] [end date: year-month-day] [data file] [initial investement] [monthly investement]"
		# Will use default parameters instead of returning
		print "Will run with default parameters: " + str(startDate) + " " + str(endDate) + " " + csvFileName + " " + str(initialInvestement) + " " + str(monthlyInvestement)
		# return
	else:
		startDate = date(int(sys.argv[1].split('-')[0]), int(sys.argv[1].split('-')[1]), int(sys.argv[1].split('-')[2]))
		endDate = date(int(sys.argv[2].split('-')[0]), int(sys.argv[2].split('-')[1]), int(sys.argv[2].split('-')[2]))
		csvFileName = sys.argv[3]
		initialInvestement = int(sys.argv[4])
		monthlyInvestement = int(sys.argv[5])

	totalMoney = initialInvestement
	totalMoneySaved = totalMoney;
	actualStartDate = None

	with open(csvFileName, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		first = True
		lastValue = 0
		for row in reader:
			if first:
				first = False
				continue
			year = row[0].split('-')[0]
			month = row[0].split('-')[1]
			day = row[0].split('-')[2]
			currentDate = date(int(year), int(month), int(day))
			value = row[1]
			if currentDate > startDate and currentDate < endDate:
				if actualStartDate == None:
					actualStartDate = currentDate
				currentValue = float(row[1])
				if lastValue > 0:
					factor = currentValue / lastValue
					totalMoney *= factor
				totalMoney += monthlyInvestement
				totalMoneySaved += monthlyInvestement
				lastValue = currentValue

	totalProfit = (totalMoney - totalMoneySaved) / totalMoneySaved
	timeDiff = endDate - actualStartDate
	yearsSaved = timeDiff.total_seconds() / 60 / 60 / 24 / 365
	annualProfit = totalProfit / yearsSaved

	print "Checking data from " + str(actualStartDate) + " to " + str(endDate)
	print "Using initial investement of " + str(initialInvestement) + " and monthly savings of " + str(monthlyInvestement)
	print "Total profits " + str(totalProfit * 100) + " %, when annualized for " + str(yearsSaved) + " years makes annual profit of " + str(annualProfit * 100) + " %"
	print "Initial investement " + str(initialInvestement) + " and total money with savings would been " + str(totalMoneySaved) + " but invested would have been " + str(int(totalMoney))


main()
