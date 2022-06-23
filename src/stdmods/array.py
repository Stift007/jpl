#
# ArrayLib
# Support for Arrays


vars = {}

def itemof(a, index):
  if len(a)<index:
    return None
  return a[index]

def arrayadd(a, *items):
  a.extend(items)
  
def arraypop(a, idx):
if len(a)<idx:
    return None
  return a.pop(idx)
  

funcs = {
  "array":lambda *s: s,
  "arrayadd":arrayadd,
  "arraypop":arraypop
  
}
