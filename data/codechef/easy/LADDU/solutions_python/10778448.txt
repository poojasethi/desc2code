# @author Kilari Teja
# LADDU

for Inx in xrange(0, int(raw_input().strip())):
	initParams = raw_input().strip().split(" ")

	TotalActions = int(initParams[0])
	Indian = True if initParams[1] == "INDIAN" else False

	Points = 0
	for ActionIndx in xrange(0, TotalActions):
		Actions = raw_input().strip().split(" ")
		Got = Actions[0]

		if Got == "CONTEST_WON":
			Points += 300 + ((20 - int(Actions[1])) if int(Actions[1]) <= 20 else 0)
		elif Got == "TOP_CONTRIBUTOR":
			Points += 300
		elif Got == "BUG_FOUND":
			Points += int(Actions[1])
		elif Got == "CONTEST_HOSTED":
			Points += 50

	if Indian:
		print (Points - Points%200)/200
	else:
		print (Points - Points%400)/400