import sys
from src.logger import logging
# The sys module gives us access to system-specific parameters and functions, like exc_info() which tells us about errors.
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()        # Gets traceback(exc_tb) details when an error occurs.
    file_name=exc_tb.tb_frame.f_code.co_filename # Gets filename where error occured
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))  # Gives a detailed message with all the info about error
    return error_message

# The class CustomException inherits from Python's built-in Exception class.
# It customizes how errors are displayed by using a helper function error_message_details.
class CustomException(Exception):   # CustomException Class is inherited from an Exception class to treat it like an exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # Initializes the parent class with the error_message. This allows CustomException to behave like a normal exception when needed.
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
    # When you define a custom exception, you're creating a new type of error that’s specific to your application or domain. 
    # This makes your code more expressive and easier to debug.

if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)