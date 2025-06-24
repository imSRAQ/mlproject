import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_no = exe_tb.tb_lineno
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_no, str(error)
    )

    return error_message


class CustomeException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self, ):
        return self.error_message
    

# To check whether exception.py file working or not
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divisible by zero")
#         raise CustomeException(e,sys)