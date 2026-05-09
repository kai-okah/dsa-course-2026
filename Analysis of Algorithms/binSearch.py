def binSearch(a,e):
  lo = 0
  hi = len(a)-1
  while hi >= lo:
    mid =  lo+(hi-lo)//2
    if e > a[mid]:
      lo = mid+1
    elif e < a[mid]:
      hi = mid-1
    else:
      return mid
  return -1
