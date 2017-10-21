'''The function filter(function, list) offers an elegant way to filter out all the elements of a list,
for which the function function returns True.
The function filter(f,l) needs a function f as its first argument.
f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l.
Only if f returns True will the element of the list be included in the result list. '''


fib=[0,1,1,2,3,5,8,13,21,34,55]
output=filter(lambda x:x%2==0,fib)
print output






pentaho_acl_authorize_list=("GrantedAuthorityEffectiveAclsResolver",
                            "GrantedAuthority", "AclEntry", "IPentahoSession", "WebPentahoObjectFactory")
def stringwithg(st):
    return st.()

pentaho_acl_authorize_uppercase_list=map(uppercase,pentaho_acl_authorize_list)
print pentaho_acl_authorize_uppercase_list