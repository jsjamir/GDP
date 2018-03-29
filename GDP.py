# -*- coding: utf-8 -*-
import gdp
gdp.gdp_init()

gcl_name = gdp.GDP_NAME("ph.edu.upd.pcari.workshop.jasper")
skey = gdp.EP_CRYPTO_KEY(filename="ph.edu.upd.pcari.workshop.firstpem.pem",
       keyform=gdp.EP_CRYPTO_KEYFORM_PEM, flags=gdp.EP_CRYPTO_F_SECRET)

gcl_handle = gdp.GDP_GCL(gcl_name, gdp.GDP_MODE_RA, {"skey":skey})

#GDP Writing
gcl_handle.append({"data": "test10"})
exit()
