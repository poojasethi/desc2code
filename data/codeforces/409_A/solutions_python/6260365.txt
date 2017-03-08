a, b, v, s = raw_input(), raw_input(), 0, '[(8'
for i in range(len(a)/2):
  v += [0,1,-1][s.find(a[2*i]) - s.find(b[2*i])]
print ("TEAM " + ("2" if v > 0 else "1") + " WINS") if v else "TIE"
