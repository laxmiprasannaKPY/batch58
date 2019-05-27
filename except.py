import logging
logging.basicConfig(level=logging.WARN,
    filename="log.txt",
    format=("%(asctime)s==>%(levelname)s-->%(message)s-->%(name)s")
    )
logging.info("program strted")
try:
    print("welcome")
    logging.info("program strted")
    a=input("Enter a vlaue:")
    logging.debug("a value enterd:%s"%a)
    b=input("Enter b value:")
    logging.debug("b value enterd: %s"%b)
    a=float(a)
    logging.debug("a converted value:%s"%a)
    b=float(b)
    logging.debug("b converted value:%s"%b)
    res=a/b
    print("result=%s"%res)
    logging.debug("result=%s"%res)
    logging.info("program completed")
except ZeroDivisionError as err:
    logging.error(err)
    print("expecting b!=0")
except ValueError as err:
    logging.error(err)
    print("expecting digits only for a,b")
except Exception as err:
    print(err)
    logging.error(err)
    print("something went wrong, contact with admin.")
except:
    logging.error("some system level issue raised")
    print("some issue in your machine")
    