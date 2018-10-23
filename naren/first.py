import logging

class MyException(Exception):
    logging.warning("Exception details: ")
    logging.warning(Exception)


raise MyException("An exception doesn't always prove the rule!")

# print(1+4)
#
# while True:
#     try:
#         n = input("Please enter an integer: ")
#         n = int(n)
#         print(n/0)
#         break
#     except ValueError:
#         print("No valid integer! Please try again ...")
#     except ZeroDivisionError:
#         print("zero division error")
#     finally:
#         print ('bye anyways')
#
#
# print("Great, you successfully entered an integer!")