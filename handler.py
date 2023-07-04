#!/usr/bin/env python
''' Contains the handler function that will be called by the serverless. '''

import runpod

# Load models into VRAM here so they can be warm between requests


def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    print('Here is the event being handled: ', event)

    # do the things
    job_input = event["input"]
    the_number = job_input["number"]

    if not isinstance(the_number, int):
        return {"error": "Silly human, you need to pass an integer."}

    if the_number % 2 == 1:
        return True

    # return the output that you want to be returned like pre-signed URLs to output artifacts
    return False


runpod.serverless.start({"handler": handler})
