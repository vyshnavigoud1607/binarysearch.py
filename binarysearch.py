def binearsearch(a,el):
  l=0
  r=len(a)

  while l<r:
    m=(l+r)//2

    if a[m]==el:
      return m
    elif  a[m]<el:
      l=m
    else:
      r=m



a=[1,2,3,4,5,6,7,8,9]
print(binearsearch(a,7))
