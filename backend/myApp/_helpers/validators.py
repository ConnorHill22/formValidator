
# NEEDS:
#       - isEmpty: if the value is empty send back error
#
#       - Validator: check to see if the data is appropriate for the field
#           - email is valid email
#           - password contains certain letter/character/number/length scheme
#           - Username matches character types
#           - First_Name, Last_Name length is appropriate
#
def isEmpty(data):
    # Description: Checks if None type, empty string, empty dict, empty list, tupple
    # Params: 
    #       data - the user inputed data
    # Return:
    #       True - if data is empty
    #       False - if data is not empty
    if(not data):
        return True
    else:
        return False



def preventNoSQLInject(dataType, data):
    # Description: Checks the type of the input
    # Params: 
    #       dataType (type) - The type your expecting. i.e. str, int, list, bool
    #                     Check https://docs.python.org/3.8/library/types.html for more
    #                     Ensure you enter the type not the type as a string
    #                     i.e. use str not 'str' as your parameter
    #       data - the user input data
    # Return:
    #       True - if dataType matches the data
    #       False - if the dataType doesn't match
    #
    #
    if type(data) is dataType:
        return True
    else:
        return False

