# import scripts
import parameters as P
import functions as F

# functions
w1 = 0.5
w2 = 0.2
w3 = 1 - w1 - w2
old_weights = [w1, w2, w3]
old_port_val = 10,000
pred_delta_price = 100

def trainEPD(chunk):
    future_port_val = (w1*old_port_val)*(1.0527)**(1/365) + (w2*pred_delta_price) + (w3*)
    

def testEPD(chunk):
    print("test")
