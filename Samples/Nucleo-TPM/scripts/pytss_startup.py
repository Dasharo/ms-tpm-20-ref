import sys
from tpm2_pytss import *

ectx = ESAPI('device:/tmp/ttydevice')

#ectx = ESAPI(sys.argv[1])

#ectx.startup(TPM2_SU.CLEAR)




