

'''
# map() function
def farenheit(temp):
    return ((float(9)/5)*temp+32)
temperature=(37.3,47.5,39.2)
c=map(farenheit,temperature) #map function applies the function farenheit to all elements of the temperature tuple
print c
'''


# Map Funtion
#map function with a function as argument

pentaho_acl_authorize_list=("GrantedAuthorityEffectiveAclsResolver",
                            "GrantedAuthority", "AclEntry", "IPentahoSession", "WebPentahoObjectFactory")
def uppercase(st):
    return st.upper()

pentaho_acl_authorize_uppercase_list=map(uppercase,pentaho_acl_authorize_list)
print pentaho_acl_authorize_uppercase_list