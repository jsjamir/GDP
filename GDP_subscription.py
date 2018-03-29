# -*- coding: utf-8 -*-
import gdp
from random import *
def write_config(filename):
    r = open(filename, 'r')
    gcl_input = r.readline().rstrip('\n')
    pem_input = r.readline().rstrip('\n')
    r.close
    return gcl_input, pem_input

gdp.gdp_init()
random_int =  randint(1,100)
gcl_input, pem_input = write_config("inputs.txt")
print "gcl: [%r]" % gcl_input
print "pem: [%r]" % pem_input

gcl_name = gdp.GDP_NAME(gcl_input)
skey = gdp.EP_CRYPTO_KEY(filename=pem_input,
       keyform=gdp.EP_CRYPTO_KEYFORM_PEM, flags=gdp.EP_CRYPTO_F_SECRET)

gcl_handle = gdp.GDP_GCL(gcl_name, gdp.GDP_MODE_RA, {"skey":skey})

#GDP Reading
gcl_handle.subscribe(3, 0, None)

while True:
    event = gcl_handle.get_next_event(None)
    if event['type'] == gdp.GDP_EVENT_EOS:
        break
    print event['datum']['data']

exit()
