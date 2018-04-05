from __future__ import absolute_import, unicode_literals
from celery import task

import os
import json
import eth_utils
from django.db.models import Max

from web3 import Web3, HTTPProvider
from background_tasks.models import Certificate

# import web3.middleware geth_poa_middleware to handle rinkeby POA
from web3.middleware import geth_poa_middleware


@task
def fetch_certificates():
    # for web3
    # to change this if we are to switch to mainnet
    provider = HTTPProvider('https://rinkeby.infura.io/JRIhcMSUX50sCH9PKk6b')
    w3 = Web3(provider)

    # inject middleware to support POA extraData field
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)

    # change normalized address to checksum address as specified in EIP55
    contract_address = eth_utils.to_checksum_address("0x9953a35ec7b3da1c54880b4a3c401746a0f5cce8")

    # read abi
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(PROJECT_ROOT, 'abi.json'), 'r') as f:
	    abi_c = json.load(f)

    # instantiate contract
    contract = w3.eth.contract(address= contract_address, abi= abi_c)   

    # we are indexed at 1
    count = 1

    # try to get highest count from db and + 1
    try:
        count = Certificate.objects.all().aggregate(Max('certificate_id'))['certificate_id__max'] + 1

    except:
        pass


    while True:
        rec_ad = eth_utils.to_normalized_address(contract.functions.certificateToReceiver(count).call())
        rec_pf = contract.functions.certificateToReceiverProof(count).call()
        send_ad = eth_utils.to_normalized_address(contract.functions.certificateToSender(count).call())
        send_pf = contract.functions.certificateToSenderProof(count).call()
        desc = contract.functions.certificateToDescription(count).call()
        create_t = contract.functions.certificateToCreateTime(count).call()

        # no one could have made a certificate in 1970 on this contract
        if create_t == 0:
            break;

        # take the data and put into our database
        try:
            # check if the field exists if so pass
            Certificate.objects.get(certificate_id=count)

        except:      
            Certificate.objects.create(certificate_id = count,
                                       receiver_address = rec_ad,
                                       receiver_proof = rec_pf,
                                       sender_address = send_ad,
                                       sender_proof = send_pf,
                                       description = desc,
                                       create_time = create_t)
            pass

        count += 1


