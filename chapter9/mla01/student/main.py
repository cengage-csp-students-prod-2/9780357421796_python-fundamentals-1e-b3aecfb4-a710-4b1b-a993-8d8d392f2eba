class EmailNotValidError():
    """ Raised when the target email is not valid """



def is_email_valid(mailing_list):
    """
      Your docstring documentation starts here.

      For more information on how to proper document your function, please refer to the official PEP8:
       https://www.python.org/dev/peps/pep-0008/#documentation-strings.

   """

for key, email in  # Loop through the mailing list:

    if '@' not in  # Check if the email contains an @:

        raise  # Raise an EmailNotValidError exception if the @ is not present



def is_email_valid_extended(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """


    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:

        # Loop through the mailing list
        for key, email in # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:


        return # Return a user-friendly message to cast the exception



def is_email_valid_extended_finally(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:
        # Loop through the mailing list
        for key, email in  # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:

        # Print a user-friendly message to cast the exception
    finally:

        return # Return the id of the users with valid email
