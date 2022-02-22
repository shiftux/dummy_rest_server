from flask import Flask
import text_replies
import os
import werkzeug
import json_logging
import logging
import sys

api = Flask(__name__)
api.debug = True

# try:
#     import googleclouddebugger
#     googleclouddebugger.enable(
#         breakpoint_enable_canary=True
#     )
# except ImportError:
#     pass

json_logging.init_flask(enable_json=True)
# json_logging.init_request_instrument(api)

logger = logging.getLogger("api-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@api.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    logger.error("trying to access inexisting route!",
                 extra={'props': {"severity": "ERROR"}})
    return "route not found!\n", 404


@api.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    logger.error("bad request!", extra={'props': {"severity": "ERROR"}})
    return "bad request!\n", 400


@api.route('/elena', methods=['GET'])
def get_elena():
    return text_replies.elena_reply()


@api.route('/sebi', methods=['GET'])
def get_sebi():
    return text_replies.sebi_reply()


@api.route('/chris', methods=['GET'])
def get_chris():
    return text_replies.chris_reply()


@api.route('/schwinggi', methods=['GET'])
def get_schwinggi():
    return text_replies.schwinggi_reply()


@api.route('/sandro', methods=['GET'])
def get_sandro():
    return text_replies.sandro_reply()


if __name__ == '__main__':
    if os.getenv('RUNNING_ON_K8S') == 'yes':
        api.run(host='0.0.0.0')
    elif os.getenv('RUNNING_IN_DOCKER') == 'yes':
        api.run(host='0.0.0.0')
    else:
        api.run()
