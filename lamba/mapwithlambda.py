# lambda function syntax-lambda argument_list: expression

celsius=[39.2,37.5,38.9,40.2]
fahrenheit=map(lambda x:(float(9)/5*x+32),celsius)
print fahrenheit





#creating another list from fahrenheit list
celsius=map(lambda y:(float(5)/9)*(y-32),fahrenheit)
print celsius






#map() can be applied to more than one list. The lists have to have the same length. map() will apply its lambda function to the
# elements of the argument lists, i.e. it first applies to the elements with the 0th index,
# then to the elements with the 1st index until the n-th index is reached

salary=[20000,35000,45000]
bonus=[5000,12000,17000]
netsalary=map(lambda salary,bonus:salary+bonus,salary,bonus)
print netsalary





#To convert the strings in the given list into uppercase

pentaho_acl_authorize_list=("GrantedAuthorityEffectiveAclsResolver",
                            "GrantedAuthority", "AclEntry", "IPentahoSession", "WebPentahoObjectFactory")

pentaho_acl_authorize_uppercase_list=map(lambda s:s.upper(),pentaho_acl_authorize_list)
print pentaho_acl_authorize_uppercase_list