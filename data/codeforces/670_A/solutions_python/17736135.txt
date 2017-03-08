x=int(raw_input())
k=x%7
y=(x//7)*2
yr_min=max(0,k-5)+y
yr_max=y+(k if k<3 else 2)
print yr_min, yr_max